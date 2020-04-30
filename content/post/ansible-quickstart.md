+++
title  = "Ansible Quickstart"
date   = "2020-04-30"
author = "Ryan Himmelwright"
image  = "img/posts/ansible-quickstart/ansible-balcony.jpeg"
caption = "Ansible Office Balcony, Durham NC"
tags   = ["dev", "linux","devops", "ansible",]
draft  = "False"
Comments = "True"
+++

A *long* time ago, I briefly explained how to configure
[Ansible](https://www.ansible.com), in [a post about building a raspberry pi
cluster](/post/ansible-on-pi-cluster/). All in all... it was by no means a
great introduction to the basics of ansible.


A month ago, I drafted a progression of examples with notes, to teach a
co-worker the *basics* of writing and using ansible roles and playbooks. After
reading through them, I realized it wouldn't take much to turn
them into an *actual* Ansible quickstart post. So here we are.

<!--more-->

I am not an Ansible genius, and reading this will not make you one either. However,
the goal of this post is to provide enough understating to get started with writing
some ansible playbooks.


## Installing

Lets start by installing ansible. It should be in most distro's main repos these
days:

Fedora Linux:
```
sudo dnf install ansible
```

MacOS:

... I have no idea. I usually always `ssh` to Linux boxes from my macbook.

I think it can be installed with `pip` though, so possibly:

```
pip3 install ansible
```

### Remote Node Requirements

In order for ansible to connect to a remote node, that node usually needs 3
things:

 - 1) Python installed
 - 2) password-less sudo permissions
 - 3) `ssh` keys configured (if running against remote hosts. Not needed if
     just running playbooks against `localhost`)

#### python

Python should already be installed on most systems. If not, check your package
manager, or try searching the documentation on [python.org](https://python.org)
to learn the best install method for your system.

#### Passwordless `sudo`

This will allow a user to run `sudo` commands, without having to type in a
password each time. I shouldn't have to say this, but... *please use with care!*

Granting password-less sudo permissions are most easily accomplished with
`visudo`:

```shell
sudo visudo
```

This will open up the `sudo` settings in your `$EDITOR`. Once opened, find the
following line and uncomment it (it's usually near the bottom of the file).

```shell
## Same thing without a password
%wheel        ALL=(ALL)       NOPASSWD: ALL
```

#### ssh

Lastly, exchange ssh-keys with the remote node. This will allow ansible to ssh
into the node without having to deal with those pesky passwords. The easiest way
to exchange keys is using the `ssh-copy-id` command, as such:

```shell
ssh-copy-id username@hostname
```

## Ansible Basics

#### Hosts File

A host inventory file is a yaml file that defines hosts ansible can connect to.
The default file is located at `/etc/ansible/hosts`. An alternative inventory
file may be provided using the `-i` flag.


Example file:

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

#### Modules

Modules are premade functionality used in ansible that can be imported into a
playbook. Simply, they *do* what you want *done*. Some examples are `ping`,
`dnf`, `apt`, `redhat_subscription`.

Feel free to search the [ansible documentation](https://docs.ansible.com) to
learn more.

#### Ad-hoc Ansible Commands

Simple and straight ansible executions can be called with the `ansible` command.
Ad-hoc commands are usually called with a module, using the `-m` flag. For
example, `ping`:

```shell
➜  ansible -m ping localhost

localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

For a more complicated example, lets use the `dnf` module to install `htop`:

```bash
ansible -m dnf -a "name=htop state=latest" localhost --become
```

This module requires some parameters to be defined. We are able to supply
them using the `-a` flag, followed by a string of the key/values pairs.

Also, because the `dnf` module requires root permissions to function, we supply
the `--become` flag, to become `root`.

Note, if I want to run this against another machine (beyond `localhost`), it
has to be defined in whatever inventory file we are using.

So, if I define an inventory file (`./hosts.yaml`) containing my desktop
computer:

```yaml
[charmelon]
192.168.1.5
```

I can install `htop` on *my desktop*, using:

```bash
ansible -i hosts.yaml -m dnf -a "name=htop state=latest" charmeleon --become
```

... and it works!

```
192.168.1.5 | CHANGED => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": true,
    "msg": "",
    "rc": 0,
    "results": [
        "Installed: htop-2.2.0-8.fc32.x86_64"
    ]
}
```

### Playbooks

As you can imagine, doing everything from the command line isn't always
helpful, or easily reproducible. That's what playbooks are for. In a nutshell,
playbooks are ansible scripts. They are a yaml file which ansible runs, instead
of running a serries of ad-hoc commands.

To demonstrate, lets convert the `dnf` command from above, into a simple
playbook named `install-htop.yaml`.

```yaml
---
- hosts: charmeleon
  become: true

  tasks:
    - name: Install Htop
      dnf:
        name: htop
        state: latest
```

Being a `yaml` file, the first line starts with `---`. Next, we define some
meta information for the entire playbook. For example, this is were we put the
`--become` flag, by turning it into `become: true`. This is also where we
define what hosts the playbook will run against. If I'm providing a hosts file,
I can alternatively use `hosts: all` to run against *all* hosts defined in the
inventory file.


#### local connections

If the playbook is to run only locally, the connection type can be set to
`local` (by default, it is set to `ssh`.)
```
  hosts: 127.0.0.1
  connection: local
```

#### tasks

Below the header information, we can define a set of tasks to run. In the
`tasks` section, a block is defined for each task, usually by calling a module
with parameters. It is best practice to describe each task using `name:`. This
will make it easier to trace the logs.

For example, lets add the`ping` module to the playbook so we have more than one
task....

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

Now the playbook will run both tasks, using `name` as the header for the output
of each one:

```bash
➜  /tmp ansible-playbook install-htop.yaml

PLAY [all] ****************************************

TASK [Gathering Facts] ****************************************
ok: [192.168.1.5]

TASK [Ping host first...] ****************************************
ok: [192.168.1.5]

TASK [Install Htop] ****************************************
ok: [192.168.1.5]

PLAY RECAP ****************************************
192.168.1.5                : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```


##### Variables

We can define sections other than `tasks`.  A useful section to add is `vars:`,
which defines variables for use in the playbook. To illustrate, lets replace
the hard-coded `htop` in the `dnf` task, to a variable named `package`. We can
even use the `package` variable in the `name` string, to dynamically change the
output in the log:


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

PLAY [127.0.0.1] ****************************************

TASK [Gathering Facts] ****************************************
ok: [127.0.0.1]

TASK [Ping host first...] ****************************************
ok: [127.0.0.1]

TASK [Install htop] ****************************************
changed: [127.0.0.1]

PLAY RECAP ****************************************
127.0.0.1                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

One great feature of variables is that they can be swapped out when calling the
playbook. The `-e` flag allows you to provide an alternative value for a
variable.  For example, lets say we want to install `nano` instead of `htop`:

```bash
➜  ansible-playbook install-htop.yaml -e package=nano

PLAY [127.0.0.1] ****************************************

TASK [Gathering Facts] ****************************************
ok: [127.0.0.1]

TASK [Ping host first...] ****************************************
ok: [127.0.0.1]

TASK [Install nano] ****************************************
changed: [127.0.0.1]

PLAY RECAP ****************************************
127.0.0.1                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Note how the task name has changed accordingly in the output. So Fancy!


## Creating some structure

### Roles

As nice as scripts are, they don't scale well. To combat impending chaos, we
break functionality down into `roles`. Roles are collections of tasks,
variables, and other resources that can be mixed and matched in playbooks.

A role is defined by a directory of it's name, and usually contains a `tasks`
sub-directory, where all of it's tasks are defined. Each sub-directory requires
a `main.yml` to be the root file for that directory. So, at the vary least, a
tasks directory will have a file named `tasks/main.yml` which contains the
role's tasks.

If there are a BUNCH of tasks defined, they can be broken out into seperate
files, and included in the `main.yml` task file.

In addition to `tasks`, a role might include a `defaults` or `vars` sub
directory. These are again structured with a `main.yml` file that may, or may
not, import other files, depending on the size and organization of the role.

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

It is important to note that these yaml files contain *just* their item. For
example, the task files contain just tasks. This is because when a role is
imported into a playbook, its items are simply inserted accordingly.

### ansible.cfg

Before we start writing some roles, it is important to know that if you are using
roles, you need to tell `ansible` where to find them. The easiest way to do
this is to define an `ansible.cfg` file in the directory you will run
`ansible-playbook` from. For example:

```
[defaults]
roles_path = roles/
```

#### Our role

As it stands, our example playbook is a *massive 13 lines long*! I can hardly
open the file without crashing my text editor. So, lets try to break up the
functionality into roles.

First, lets make the directories:

```bash
mkdir -p roles/install-htop/{tasks,defaults}
```

Next, we can add our variables to a default file,
`roles/install-htop/defaults/main.yml`:

```yaml
---
package: htop
```

With the `package` variable set, lets create the tasks. To demonstrate
including other files in the `main.yml`, I'm going to be overly-complicated and
extract our `ping` task into its own file, and then include it in the `main.yaml`.

So first, `roles/install-htop/tasks/ping.yaml`

```yaml
---
- name: Ping host first...
  ping:
```

And then, `roles/install-htop/tasks/main.yaml`, which will also include our
`dnf` install task...

```yaml
---
- include_tasks: ping.yaml

- name: Install {{ package }}
  dnf:
    name: "{{ package }}"
    state: latest
```

Congrats, we have an `install-htop` role defined!


### Including roles in playbooks

Just as we included `vars` and `tasks` in the playbook, if we already have
tasks and vars defined in a *role*, we can instead include that *role*:


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

PLAY [127.0.0.1] ****************************************

TASK [Gathering Facts] ****************************************
ok: [127.0.0.1]

TASK [install-htop : include_tasks] ****************************************
included: /tmp/roles/install-htop/tasks/ping.yaml for 127.0.0.1

TASK [install-htop : Ping host first...] ****************************************
ok: [127.0.0.1]

TASK [install-htop : Install htop] ****************************************
ok: [127.0.0.1]

PLAY RECAP ****************************************
127.0.0.1                  : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```


and it still works :)

# Conclusion

While only the tip of the iceburg, I think we have covered enough basics
to make *something* useful. Using this small amount of Ansible
knowledge, I have been able to create playbooks that configure applications,
update all my computers, and setup each of my machines when I reformat them.
However, don't let that stop you from learning even more! Ansible is a powerful
tool and worth any amount of time invested into it. Enjoy!
