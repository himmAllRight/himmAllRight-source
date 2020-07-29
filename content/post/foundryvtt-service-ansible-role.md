+++
title   = "Creating Systemd Unit Files using Ansible"
date    = "2020-07-29"
author  = "Ryan Himmelwright"
image   = "img/posts/foundryvtt-service-ansible-role/unc-campus.jpeg"
caption = "UNC-Chapel Hill Campus, Chapel Hill, NC"
tags    = ["Linux", "systemd", "Customization", "ansible"]
draft   = "False"
Comments = "True"
+++

In my [previous post](/post/autostarting-application-systemd-service/), I
created a systemd unit file to define an application as a service, and
configured it to auto-start on my server. I've been making a big push to define
the provisioning of all my homelab machines/VMs using automation. So the last
step in setting up my FoundryVTT server, is to *automate* the process.
Fortunately, creating a systemd unit file is quite easy to do using
[ansible](https://www.ansible.com).

<!--more-->

## Creating the Ansible Role
Let's start by creating a role (if you don't know what an ansible role
is, checkout [this guide](/post/ansible-quickstart/) I wrote not too long ago).
First, create some directories:

```bash
cd roles
mkdir -p foundryvtt/{defaults,tasks,templates}
```

One difference from roles I've created previously, is that this one contains a
`templates` directory. That is because *this* role will use a `j2` template to
define the systemd unit file, but more on that later.

## Defining Variables

Lets create some files, starting with one to define the default variables.
Open `roles/foundryvtt/defaults/main.yaml` and add the following:

```yaml
---
user: "{{ ansible_user_id }}"
service_description: "A service to run the Foundry VTT node app"
foundryvtt_dir: "/home/{{ user }}/foundryvtt/"
foundrydata_dir: "/home/{{ user }}/foundrydata"
```
This defines a few default veriables that will be used in the service file
template, as well as in the tasks file. The variables can optionally be
over-ridden when running a playbook, but they will default to these values if
not specified.

## Making a Template

Now that the varibles are defined, we can create the unit file template. So,
open a new file (`roles/foundryvtt/templates/foundryvtt.service.j2` in my
case), and insert the unit file from the previous post.

Next, walk through the file and substitute any values for the variables defined
in the previous section:

```INI
[Unit]
Description={{ service_description }}
Documentation=https://foundryvtt.com
After=network.target

[Service]
Environment=NODE_PORT=30000
Type=simple
User={{ user }}
ExecStart=/usr/bin/node {{ foundry_dir }}/resources/app/main.js --dataPath={{ foundrydata_dir }}
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Great! This template is now ready to be used in our role.


## Ansible Tasks

Last but not least, time to write some Ansible tasks. Open a new file
(`roles/foundryvtt/tasks/main.yaml`), and lets start by adding any additional
tasks *this particular role* needs, outside of the service file. For my example,
this includes creating the defined data directories, unzipping the application source
package, and opening required ports in the firewall:

```yaml
## Note, you likely don't need these tasks. They are just for my particular
## example...
- name: Create foundryvtt dir at {{ foundryvtt_dir }}
  become_user: "{{ user }}"
  file:
    path: "{{ foundryvtt_dir }}"
    state: directory

- name: Create foundrydata dir at {{ foundrydata_dir }}
  become_user: "{{ user }}"
  file:
    path: "{{ foundrydata_dir }}"
    state: directory

- name: Send Foundry Package
  when: foundryvtt_send_src is defined and foundryvtt_send_src is not none
  copy:
    src: "{{ foundryvtt_send_src }}"
    dest: "{{ foundryvtt_package_src }}"

- name: Extract package
  unarchive:
    src: "{{ foundryvtt_package_src }}"
    dest: "{{ foundryvtt_dir }}"
    remote_src: yes

- name: Start firewalld
  systemd:
    name: firewalld
    state: started

- name: Open FoundryVTT Ports (firewalld)
  firewalld:
    port: 30000/tcp
    permanent: yes
    state: enabled

- name: reload service firewalld, in all cases
  systemd:
    name: firewalld
    state: reloaded
```

With all that defined, lets finally define a task to create our unit file using
the template:

```yaml
- name: Create foundryvtt systemd service file
  template:
    src: templates/foundryvtt.service.j2
    dest: /lib/systemd/system/foundryvtt.service
```

The `src` is set to the relative location (to the role) of the template we
defined earlier, and the `dest` is set to where we would like the generated
file to be copied to. This template is a unit file for a systemd service, so
I'm going to copy it to `/lib/systemd/system/foundryvtt.service`.

Last but not least, lets start the newly created service:

```yaml
- name: Start foundryvtt service
  systemd:
    name: foundryvtt
    state: started
```

... and... our role is finished!

## Playbook

To run the role, it is easiest to have it run in a playbook. I try to define
the provisioning of all my systems in their own playbooks, including my foundry
server, so I use this role there. Just remember to call it in a `roles:`
section of the playbook, like so:

```yaml
  roles:
    - foundryvtt
```

## Conclusion

That's it. We've easily automated setting up the systemd unit file from the
previous post using ansible. This makes defining and reproducing unit roles
very simple. In addition, knowing how to use templates in ansible is *very*
powerful, and I will definitely be utilizing them much more moving forward.
Enjoy!
