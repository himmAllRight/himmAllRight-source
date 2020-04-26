+++
title  = "Ansible Quickstart"
date   = "2020-04-28"
author = "Ryan Himmelwright"
image  = "img/posts/ansible-quickstart/park-sky.jpeg"
caption = "Duke Park, Durham NC"
tags   = ["dev", "linux","devops", "ansible",]
draft  = "False"
Comments = "True"
+++

A couple weeks ago I was going to give a co-worker of mine a brief run down of
the very basics of ansible. I want to quickly share enough information, so that
someone could easily get up and going writing some basic playbooks that have
tasks organized with under ansible [roles](). While I briefly talked about
setting up ansible [a long time ago](/post/ansible-on-pi-cluster), it part of
another post and not a great full introduction to the basics of ansible. After
hashing out some examples into my notes, I realized this would actually make a
great post, and could be shared with anyone who would benefit from it.

<!--more-->


## Installing

First lets install ansible. It should be in most distro's main repos these
days:

*Fedota Linux*: `sudo dnf install ansible`

*MacOS*: No idea. I `ssh` to Linux boxes on my macbook XD. It can be installed
with `pip` though, so possibly:

`pip install ansible`

### Remote Node Requirements

In order for ansible to connect to a node, that node usually needs 3 things:

 - 1) Python installed
 - 2) Often, it needs passwordless sudo abilities... This can be done using:
 - 3) `ssh` keys configured (if running against remote hosts. Not needed if
     just running playbooks against `localhost`)

#### python

Python should already be installed on most systems. If not, I'm probably not
the best source of how to do it, so I'll leave this step up to you. Don't
worry, you got this!

#### Passwordless `sudo`

Now lets setup passwordless sudo. This will allow your user to run `sudo`
commands, without having to type in a password each time. Now, I shouldn't have
to say this, but... use with care.

This is most easily accomplished with `visudo`:

```shell
sudo visudo
```

This command will open up the `sudo` settings in your `$EDITOR`. Once opened,
find the following line and uncomment it (it's usually near the bottom of the
file).

```shell
## Same thing without a password
# %wheel        ALL=(ALL)       NOPASSWD: ALL
%ryan   ALL=(ALL)       NOPASSWD: ALL
```

You can also optionally copy the uncommented line and apply it with a more
limited group than `wheel`. This is my preferred method (And what I have done
in the example).


#### ssh

Lastly, copy ssh-keys. The easiest way is to use the `ssh-copy-id` command as
such:

```shell
ssh-copy-id username@hostname
```

## Basics

Now lets quickly get into the basics of ansible.

#### Hosts Inventory

A host inventory file is a yaml file that defines hosts to connect to in
ansible. The default is located at `/etc/ansible/hosts`. Another inventory file can
be provided with the `-i` flag.


Example:

```yaml
[VMs]
## Server VMs
192.168.10.50
192.168.10.71
192.168.10.118

[Hosts]
## Hosts
192.168.10.12

[cluster]
192.168.112.205
192.168.112.206
192.168.112.207
```

#### Modules/Roles

Premade functionality used in ansible. In playbooks, these are sort of like functions called for task blocks. They do something you want done. Some examples are `ping`, `dnf`, `apt`, `redhat_subscription`.

Feel free to search the [ansible documentation](https://docs.ansible.com) to learn more.

#### Ad-hoc Ansible Commands

Simple and straight ansible commands can be called with the `ansible` command,
and usually with a module, called using the `-m` flag. For example, ping:

```shell
ansible -m ping localhost
```

For a more complicated example, lets use the `dnf` module to install `htop`:

```bash
ansible -m dnf -a "name=htop state=latest" localhost --become
```

This module requires some parameters to know what to do. We are able to supply them using the `-a` flag, followed by a string of the key/values.

Also, since the `dnf` module requires root permissions to function, we supply the `--become` flag, to become root.

Note, if I want to run this against another machine (beyond `localhost`), it has to be defined in whatever inventory file we are using.

So, if I define an inventory (`./hosts.yaml`) like this:

```yaml
[charmelon]
192.168.1.5
```

I can install `htop` on *it*, using:

```bash
ansible -i hosts.yaml -m dnf -a "name=htop state=latest" charmeleon --become
```

... and it works!

```
192.168.1.5 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "msg": "Nothing to do",
    "rc": 0,
    "results": []
}
```

#### Playbooks

As you can imagine, doing everything from the command line isn't always helpful or easily reproducable. That's where playbooks come in. Playbooks are basically ansible scripts. They are a yaml file that ansible is able to run, instead of running the straight ansible commands we showed above.

As an examble, lets convert the `dnf` command from above to a simple playbook (named `install-htop.yaml`).

```yaml
---
- hosts: all
  become: true

  tasks:
    - name: Install Htop
      dnf:
        name: htop
        state: latest
```

Being a `yaml` file, the first line starts with `---`. Next, we define some meta information for the entire playbook. For example, this is were we state our `--become` flag, by turning it into a `become: true`. This is also where we state that hosts the playbook will run against. If I'm providing a hosts file, I can use `hosts: all` to run against all hosts in the inventory file.



If the playbook is to run only locally, the connection type can be set to `local` (by default, it is set to `ssh`.)
```
  hosts: 127.0.0.1
  connection: local
```

After the header information, we can define a set of `tasks:` to run. In the `tasks` section, define a block for each task, usually by calling a module with parameters. It is best practice to name each tag using `name:`.

For example, if I also wanted to add our `ping` module so we had more than one task....

```yaml
---
- hosts: 127.0.0.1
  connection: local
  become: true

  tasks:
	- name: Ping host first...
	  ping:

    - name: Install Htop
      dnf:
        name: htop
        state: latest
```

and it will run both tasks, using the "name" as the header for the output of each one:

```bash
➜  /tmp ansible-playbook install-htop.yaml

PLAY [all] *****************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************
ok: [192.168.1.5]

TASK [Ping host first...] **************************************************************************************
ok: [192.168.1.5]

TASK [Install Htop] ********************************************************************************************
ok: [192.168.1.5]

PLAY RECAP *****************************************************************************************************
192.168.1.5                : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```


##### Variables

We can define other sections beyond `tasks` in a playbook. Another section we can define is variables, with `vars:`. To illistrate, lets replace the hard-coded `htop` in our playbook to a variable named `package`. We can even swap it out in our `name`, and the output will dynamically change.


```yaml
---
- hosts: 127.0.0.1
  connection: local
  become: true

  vars:
    package: htop

  tasks:
    - name: Ping host first...
      ping:

    - name: Install {{ package }}
      dnf:
        name: "{{ package }}"
        state: latest
```

And the output:

```bash
➜  ansible-playbook install-htop.yaml

PLAY [127.0.0.1] ***********************************************************************************************

TASK [Gathering Facts] *****************************************************************************************
ok: [127.0.0.1]

TASK [Ping host first...] **************************************************************************************
ok: [127.0.0.1]

TASK [Install htop] ********************************************************************************************
changed: [127.0.0.1]

PLAY RECAP *****************************************************************************************************
127.0.0.1                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

The best thing about variables... is they can be swapped out when calling the playbook. The `-e` flag allows you to provide your own value for a variable. For example, lets say we want to install `nano` instead of `htop`:

```bash
➜  ansible-playbook install-htop.yaml -e package=nano

PLAY [127.0.0.1] ***********************************************************************************************

TASK [Gathering Facts] *****************************************************************************************
ok: [127.0.0.1]

TASK [Ping host first...] **************************************************************************************
ok: [127.0.0.1]

TASK [Install nano] ********************************************************************************************
changed: [127.0.0.1]

PLAY RECAP *****************************************************************************************************
127.0.0.1                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Fun right?


## Creating some structure

### roles

As nice as scripts are, they don't scale well. So, we break things down into things called `roles`. Roles are collections o tasks, varilables, and other resources that can be mixed and matched in playbooks. A role is defined by a directory of it's name, and usually contains a `tasks` sub-directory, were all of it's tasks are defined. At the vary least, there is a task file named `tasks/main.yml` that contains tasks.

If there are a BUNCH of tasks defined, they can be broken out into seperate files, and included in the `main.yml` taks file.

In addition to `tasks`, a role might include a `defaults` or `vars` sub directory. These are again structured with a `main.yml` file that may or may not import other files, depending on the size and organization.

```bash
## Example structure of a 'subscriptions' role
roles
└── subscriptions
    ├── defaults
    │   └── main.yml
    ├── README.md
    └── tasks
        └── main.yml
```

It is important to note that these yaml files contain *just* their item. For example, the tasks files, contain just tasks, like *tasks* section of a playbook. This is because when a role is imported in a playbook, the tasks are basically inserted into the tasks section of it.

#### Our role

So... I guess we can convert the tasks and variables in our playbook to a role?

First, lets make the dirs:

```bash
mkdir -p roles/install-htop/{tasks,defaults}
```

Next, lets add our variables to a defaults file, `roles/install-htop/defaults/main.yml`:

```yaml
---
package: htop
```

Next, lets create the tasks. To demonstrate including other files in the `main.yml`, I'm going to be overly-complicated and extract our `ping` task to it's own file, and include it in the main.

So first, `roles/install-htop/tasks/ping.yaml`

```yaml
---
- name: Ping host first...
  ping:
```

And now, `roles/install-htop/tasks/main.yaml`, which will also include our `dnf` install task...

```yaml
---
- include_tasks: ping.yaml

- name: Install {{ package }}
  dnf:
    name: "{{ package }}"
    state: latest
```

Now, we should have an `install-htop` role defined!


### Including roles in playbooks

Just as we included `vars` and `tasks` in a playbook, if we already have a bunch of tasks and vars defined in a *role*, instead we can just include that *role*:


```yaml
---
- hosts: 127.0.0.1
  connection: local
  become: true

  roles:
    - install-htop
```

Easy. Let's run it:

```bash
➜  ansible-playbook install-htop.yaml
[WARNING]: Ansible is being run in a world writable directory (/tmp), ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir

PLAY [127.0.0.1] *****************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************
ok: [127.0.0.1]

TASK [install-htop : include_tasks] **********************************************************************************************************
included: /tmp/roles/install-htop/tasks/ping.yaml for 127.0.0.1

TASK [install-htop : Ping host first...] *****************************************************************************************************
ok: [127.0.0.1]

TASK [install-htop : Install htop] ***********************************************************************************************************
ok: [127.0.0.1]

PLAY RECAP ***********************************************************************************************************************************
127.0.0.1                  : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```


Still works :)

### ansible.cfg

One last thing to note, if you are using roles, you do need to tell `ansible` where to find them. The easiest way to do this is to define an `ansible.cfg` file. For example:

```
[defaults]
roles_path = roles/
```

# Conclusion

So while only this tip of the ice-burg, I think I have covered the majority of
things you need to know to get *something* useful. I have been able to create
several useful roles and playbooks using this limited knowledge of Ansible in
both my personal and work life. But don't let that stop you from learning even
more! Good luck!
