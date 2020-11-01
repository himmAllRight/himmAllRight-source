+++
title   = "Automated Nativefier App builds"
date    = "2020-10-30"
author  = "Ryan Himmelwright"
image   = "img/posts/automated-nativefier-app-builds/troll_closeup.jpeg"
caption = "Kill Devil Hills, NC"
tags    = ["Linux", "containers", "Fedora", "Ansible",]
draft   = "True"
Comments = "True"
+++

Many applications we use today are just fancy web pages wrapped up in a desktop
shell. Most people even skip the shell and just run 'webapps' as another tab in
the web browser. Personally, I prefer to have dedicated app windows opened for
my essential tools. So, I love [nativefier]() to create desktop versions of my
favorite web tools. My only problem with it... is that it can be a pain to
setup. Lets fix that.

<!--more-->

## How I use nativefier

So, I use nativefier. This is particularly being a linux user. While MacOS has
some applications in the AppStore that I don't have an equivelant for, they are
usually just a wrapper around the same functionality that the webpage has, that
I can save in the dock. Using nativefier, I am able to have "desktop" versions
of these apps on other platforms that don't have a Linux desktop version, *or*
even create desktop versions for web applications that do not have a desktop
version on *any* platform. I have even used nativefier on my Mac to create
desktop apps I got used to using on Linux.

### What Apps I use it for

*Screenshot of one of my nativefier app?*

Basically, I use nativefier for all of the web services with a missing linux
client, or tools that I use a lot. Most days, I usually use the following:

- Pocket - to read articles
- Pocketcasts - to listend to synced podcasts between my phone and computer
- Fastmail - For my personal email and calendar
- homeassistant - To control parts of my house (mostly lights and temp)
- Notion - My [notes and planning tool]()
- Soundcloud - For music while working

Also, while not used every day, I have made notion apps for twitch and icloud.
These are both apps that exist on other desktops but don't have a Linux build.

### How I make them like normal apps

THere are a few thing I do to help make these apps *feel* more like a normal,
native application.

#### Desktop Files

*Screenshot of apps being listed in search?*

The first, and argualy most important step I take is creating a [desktop
entity](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html)
for each nativefier build. A desktop entity defines something as an application
in Gnome and KDE Plasma environments, allowing it to show up in menus and
launchers. Defining an entity for the nativefier builds tells the system to to
treat the build as a normal application, which is what the want.

#### Icons

The second thing I've more recently started doing is making sure that I use
proper icons when I run nativefier. I already needed the icon for creating the
desktop entity, but I noticed it wouldn't always match in the dock once the
application opened. This extra step help everything look more cohesive.

### How I usually create them

*Not sure what image to put here...*

While the extra works helps to make them really feel like desktop applications,
it add a bunch of steps to the creation process. When I want to make a new
nativefier app, I usually have to:

- Install nativefier and it's dependencies (usually in a podman container)
- Build the application to a Build directory
- Find an icon for the application and add it to my `~/.local/share/icons/` dir
- Create a new `.desktop` file for the application.
    - Fill out the description
    - Change the exec paths.
    - Add the icon path
- Verify it works (something is usually missing)

To save some time when setting up a new system, I will often copy the builds
directories along with the desktop and icon files. However, even that can be
quite tedious to move all the files to the correct space, and often changing
all the path values if they differ at all. For example, if the new system has a
different username, I have to update all of the desktop files.

So... lets automate the process.

## Using a podman container instead

Before automating the steps, there's one more improvement to my normal steps I
want to make. Instead of installing nativefier from a normal `npm` install, I
want to switch to building with an ephemeral nativefier container. This have
several benefits, including not having to install dependencies, and always
using the latest version for the automation. Plus, containers are fun.

After some tweaking, I was able to get a nativefier container building apps on
my desktop using podman, by tweaking the suggested [docker instructions]() into
the following command:

```bash
# Pull the Image
podman pull jiahaog/nativefier

# Run a build for a container
podman run --rm  -v ICONS_DIR src -v NATIVEFIER_BUILD_DIR target jiahaog/nativefier --icon /src/ICON --name NAME -p linux -a x64 URL /target
```
This command had a few parameters that need to be swapped:

- `ICONS_DIR`: the directory that contains the desired application icon to build
with.
- `NATIVEFIER_BUILD_DIR`: the directory to save the application builds.
- `ICON`: The filename of the image to use for the icon
- NAME: The name of the application (ex: `pocket` or `homeassistant`)
- `URL`: The *url* of the webapp to build

This spins up a podman container, passes our variables through, and builds a
nativefier app. After finishng, the container automatically deletes itself.

## Automating the process

Now that we've figured out how to run nativefier with podman, we can focus on
writing the automation. Like I have [done in the past](), I will be
implementing the automation by added in a new role to use in my ansible
playbooks. If you are unfamilary with roles, you might want to checkout the
[quickstart post]() I wrote earlier this year.

To start, I'll create a new role, with `tasks`, `defaults`, `files`, and
`template` sub directories.

### Vars

To start, lets define the default variables we will use in tasks and template:

```yaml
user: "{{ ansible_user_id }}"  # User to run as
nativefier_build_dir: "/tmp/"  # Location to build apps at
nativefier_dir: "/home/{{ user }}/Builds/" # Location to move completed builds
icons_dir: "/home/{{ user }}/.local/share/icons/" # App Icon location
applications_dir: "/home/{{ user }}/.local/share/applications/" # desktop entry location
```

We will define one more variable which won't have a default, `nativefier_apps`. However, I'll
talk about that later when we add the role to a playbook.

### Templates

Now, lets create the one template we need for this role: the generic
`application.desktop` file. Create a new file in the `templates` directory
named `nativefier.desktop.j2` and paste the following contents:

```ini
[Desktop Entry]
Name={{ item.name }}
Comment=Nativefier app for {{ item.name }}
Exec={{ nativefier_dir }}/{{ item.name }}-linux-x64/{{ item.name }}
Terminal=false
Type=Application
Icon={{ item.icon }}
Categories=Multimedia;
TryExec={{ nativefier_dir }}/{{ item.name }}-linux-x64/{{ item.name }}
```

This template will take the variables for each nativefier app we define in the
playbook, and use them to fill out a desktop file for each app.


### Files

*Screenshot of icon folder?*

Before writing tasks, there is one more role directory to fill: `files`. For
this role, we might want to include the icon files we intend to use for the
applicatons. So, create a `files` directory in the role, and fill it with the
logo files to use (likely `png`).


### Tasks

Lastly, lets write some tasks. So, create and open up a `main.yml` file under the
tasks sub directory.

The first tasks will just check and ensure that the directories we intend to
use exist. This is generally good practice to prevent playbooks breaking from
missing directories:

```yaml
- name: "Ensure Icon dir exists"
  file:
    path: "{{ icons_dir }}"
    state: directory

- name: "Ensure applications dir exists"
  file:
    path: "{{ applications_dir }}"
    state: directory

- name: "Ensure {{ nativefier_build_dir }} exists"
  file:
    path: "{{ nativefier_build_dir }}"
    state: directory

- name: "Ensure {{ nativefier_dir }} exists"
  file:
    path: "{{ nativefier_dir }}"
    state: directory
```


#### Managing Icon Files

Next, lets add a small task that will copy the icons we included with the role,
to the user's local icon folder:

```yaml
- name: Move icons to local folder
  copy: src="{{ item.icon }}" dest="{{ icons_dir }}/{{ item.icon }}"
  loop: "{{ nativefier_apps }}"

```

This will ensure that all the icons are already in place when we build both the
nativefier app and the `.deskop` files.

#### Automating the podman builds

We can now define a few tasks that will pull and run the nativefier container
using podman. *(Note: This could be done with docker... but I use podman XD)*:

```yaml
- name: Pull down nativefier container image
  shell: "podman pull jiahaog/nativefier"

- name: Build Nativefier app via podman
  shell: "podman run --rm --security-opt label=disable -v {{ icons_dir }}:/src -v {{ nativefier_build_dir }}:/target jiahaog/nativefier --icon /src/{{ item.icon }} --name {{ item.name}} -p linux -a x64 {{ item.url }} /target"
  loop: "{{ nativefier_apps }}"

- name: Clean out nativefier dir
  become: true
  file:
    path: "{{ nativefier_dir }}/{{ item.name }}-linux-x64"
    state: absent
  loop: "{{ nativefier_apps }}"

  # I don't love this but copy was too slow
- name: Move Builds to Nativefier Location
  become: True
  shell: "mv {{ nativefier_build_dir }}/{{ item.name }}-linux-x64 {{ nativefier_dir }}/{{ item.name }}-linux-x64"
  loop: "{{ nativefier_apps }}"
```

This will pull down the latest nativefier image, and then use our variables
to build each application to the build directory. The tasks will also move the
built app to the final location.

#### Manaing Application Files

Lastly, with icons in place and the application builds complete, we can create the application
entry files to point to them by adding this final task:

```yaml
- name: Generate Application Desktop Files
  template:
    src: templates/nativefier.desktop.j2
    dest: "{{ applications_dir }}/{{ item.name }}.desktop"
  loop: "{{ nativefier_apps }}"
```

And there we go, that's it! Well... sort of.

## Selinux woes

While this initially *worked on my computer*, when I tested it on my laptop and
in some VMs... it failed.

### Issues

Every time I ran the playbook, I hit this error:

```bash
Error during build. Run with --verbose for details. [Error: EACCES: permission denied, mkdir '/target/linux-x64-template'] {
  errno: -13,
  code: 'EACCES',
  syscall: 'mkdir',
  path: '/target/linux-x64-template'
}
```

I was able to tell it was happening while running the podman container. I
assumed it might be `selinux` related but was unable to sort out a solution
right away.

### The Fix

Eventually after browsing the internet, I learned that my easiest solution was
to add the option `--security-opt label=disable` to my `podman run` command to
turn off label separation for the container. I'm sure there is a better, more
secure soltion I could do, but I figured this one was a good compromise of
being easy to implement, but more secure than the common (and wrong) suggestion
to "*just disable selinux*".

### One last fix...

```bash
drwxr-xr-x. 1 100999 100999  560 Oct 25 20:40 jellyfin-linux-x64
```

Lastly, I wanted to add one more cleanup task. My builds usually had the ugly uid/gid
pair of `100999 100999`, so I added one more task to change ownership to the
`user`:

```yaml
- name: Change Permissons of Nativefier Dirs
  become: True
  file:
    path: "{{ nativefier_dir }}/{{ item.name }}-linux-x64"
    owner: "{{ user }}"
    group: "{{ user }}"
  loop: "{{ nativefier_apps }}"
```

After that change:

```bash
drwxr-xr-x. 1 ryan ryan  560 Oct 25 20:40 jellyfin-linux-x64
```

Much better!

## Example adding it to my playbooks

With the role complete, it is *finally* time to add it to a playbook. I define
playbooks to provision all of my machines, so I will just at it those. To do
so, first make sure the role is added to the list of roles used by the plabook.
For example:

```
  roles:
    - apps/nativefier
```

Next, define a new var named `nativefier_apps`. This variable is a list of
dictionaries, with each dictionary providing the variavles for a different
nativefier application. Each nativefier build requires three values:

- `name`: The name of the application
- `icon`: The filename (including ext) of the icon file to for the application
- `url`: The address for the webpage to build as a nativefier app

So, to build my `pocket`, `fastmail`, and `homeassistant`  I added the
following var to my playbook:

```yaml
nativefier_apps:
  - name: pocket
    icon: pocket.png
    url: "https://app.getpocket.com"
  - name: fastmail
    icon: fastmail.png
    url: "https://www.fastmail.com"
  - name: homeassistant
    icon: homeassistant.png
    url: "http://homeassistant.local:8123"
```

That should be it. Run the playbook and enjoy!

## Conclusion

*Last screenshot of some apps?*

I have wanted to create this role for a very long time and I am glad I finally
did. Nativefier is such an amazing tool that I love using. Paring it with
podman and ansible has somehow managed to make it magnitudes better. Enjoy!
