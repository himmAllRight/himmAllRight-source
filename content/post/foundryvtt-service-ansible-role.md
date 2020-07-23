+++
title   = "Creating Systemd Unit Files using Ansible"
date    = "2020-07-30"
author  = "Ryan Himmelwright"
image   = "img/posts/foundryvtt-service-ansible-role/unc-campus.jpeg"
caption = "UNC-Chapel Hill Campus, Chapel Hill, NC"
tags    = ["Linux", "systemd", "Customization", "ansible"]
draft   = "True"
Comments = "True"
+++

In my [previous post](/post/autostarting-application-systemd-service/), I
created a systemd unit file to define an application as a service, and
auto-start on my server. Recently, I've made a big push to define the provision
and setup of all my homelab machines/VMs in automation. Fortunately, it turns
out that creating a systemd unit file is quite easy to do with
[ansible](https://www.ansible.com).

<!--more-->

## Creating the Ansible Role
Let's first start by creating a role (if you don't know what an ansible role
is, checkout [this guide](/post/ansible-quickstart/) I wrote not too long ago).
Lets start by creating the directories:

```
cd roles
mkdir -p foundryvtt/{defaults,tasks,templates}
```

One difference from some of the roles I've created previously, is that this one
contains a `tempaltes` directory. This is because it will use a `j2` tempalate
to define the systemd unit file, but more on that later.

## Defining Variables

With the directories, lets create the files, starting with the default
variables. So, open `roles/defaults/main.yaml` and add the following:

```
---
user: "{{ ansible_user_id }}"
service_description: "A service to run the Foundry VTT node app"
foundryvtt_dir: "/home/{{ user }}/foundryvtt/"
foundrydata_dir: "/home/{{ user }}/foundrydata"
```
This defines a few default veriables that will be used in the service file
template, as well as in the tasks file. These variables can optionally be
over-ridden when running a playbook, but they will default to these values if
not specified.

## Making a Template

Now that the varibles are defined, we can create the unit file template. So,
open a new files (`roles/templates/foundryvtt.service.j2` in my case), and
insert the unit file from the previous post.

Next, walk through the file and substitute any values for the variables defined
in the previous section:

```
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
- Create tasks file
- Define the tasks to:
    - Setup for service (create dirs, etc)
    - create/move the file to the location
    - Start the service, open ports, and other post start tasks


## Conclusion

Wrap up, that's it.
