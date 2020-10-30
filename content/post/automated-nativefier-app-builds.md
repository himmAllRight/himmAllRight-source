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

Intro talking about how I love and use nativefier... but it's a pain to setup.

<!--more-->

## How I use nativefier

Many applications we use today are really just fancy web pages wrapped up in a
desktop shell. Some even forego the deskop wrapper and are straigt webapps used
in the web browser. Personally, I prefer to have dedicated apps windows opened
for my essential computing tools, rather than browsing through a bunch of tabs
in the browser.

So, I use nativefier. This is particularly being a linux user. While MacOS has
some applications in the AppStore that I don't have an equivelant for, they are
usually just a wrapper around the same functionality that the webpage has, that
I can save in the dock. Using nativefier, I am able to have "desktop" versions
of these apps on other platforms that don't have a Linux desktop version, *or*
even create desktop versions for web applications that do not have a desktop
version on *any* platform. I have even used nativefier on my Mac to create
desktop apps I got used to using on Linux.

### What Apps I use it for

**Screenshot of one of my nativefier app?**

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

#### Desktop Files

**Screenshot of apps being listed in search?**

#### Icons


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


## It's a pain to setup

... so automate.

## Using a podman container instead

```
code
```

## Automating the process

```
code
```

### Automating the podman builds

```
code
```

### Managing Icon Files

```
code
```

### Manaing Application Files

```
code
```

## Selinux woes

### Issues

### The Fix

```
code
```

## Example adding it to my playbooks

```
code
```

## Conclusion
