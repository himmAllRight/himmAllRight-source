+++
title = "Updating the Pi Cluster with Ansible"
date = "2017-05-25"
author = "Ryan Himmelwright"
tags = ["Homelab", "Cluster", "Pi", "DevOps", "Ansible",]
+++

With Ansible configured on the Pi cluster, it is time to have it do something useful. When working with a clustered system, even the simplest tasks become tedious and time consuming. For example, updating the system. While I could manually update each of the 3 pi nodes, it is not scalable to 10 or 30 nodes, let alone hundreds or thousands. Tools like Ansible, make doing tasks such a supdating clustered systems, trivial again. In this post, I will walk through setting up an Ansible playbook to update my Pi cluster.

<!-- more -->

### Hosts File
The first task when using Ansible is to setup the `hosts` file. No, not the normal `/etc/hosts` file, but the *other* one *just* for Ansible, which can be found at `/etc/ansible/hosts`. Configuring the Ansible hosts file is fairly straightforward. Groups of computers are defined using `[brackets]`, with computer ip/hostnames of the group are listed below. For example:

A nice feature of group definitions is that hierical structures can be constructed using the `:child` suffix in order to create groups of groups. For example, for my [homelab](../../pages/homelab), I like to make an ansible hosts file that splits out my servers based on their distribution, and then group those by their packaging type. This makes it easier for me to do generic updates, which is what I mostly use ansible for (at this point). So, for example:

```
[ubuntu]
mrmime
geodude

[debian]
ninetales

[fedora]
fedora-test

[centos]
tangels

[arch]
meowth
staryu
diglet

[deb:children]
ubuntu
debian

[rpm:children]
fedora
centos

```

For use with the cluster, I kept it simple, although I did opt to create rpi/bpi subgroups:

```
[cluster:children]
rpis
bpis

[rpis]
pi0
pi1

[bpis]
bpi
```

### Ping Hosts
Once the hosts file is setup, it can be tested using the `ping` module. I tested my `cluser` group, as well as the `rpis` and `bpis` subgroups.


```
ansible rpis -m ping
ansible bpis -m ping
ansible cluster -m ping
```

Assuming the steps of [the last post](../Ansible-On-Pi-Cluster) were done correctly, this should work. If not, double check that post and make sure everything looks correct.

### Playbooks
After confirming that the hosts file is properly configured, I started to dig into playbooks. Playbooks are Ansible's scripting system used to configure, deploy, and orcistrate systems. They can describe ways in which systems should be configured (ex: enable ssh), or outline a set of steps for an IT task (ex: running updates, restarting a server). As stated in the [playbook documentation](https://docs.ansible.com/ansible/playbooks.html):

<div id="post-quote">
*"If Ansible modules are the tools in your workshop, playbooks are your instruction manuals, and your inventory of hosts are your raw material."*
</div>

Playbook files are expressed using [YAML syntax](https://docs.ansible.com/ansible/YAMLSyntax.html), which is easy to read, but still powerful. The first step when creating a new playbook, being a YAML file, is to set the header and footer. The header consists of three `-`'s at the top of the file, and the footer ends the file with three periods (`.`). This indicates the start and end of the document.

When writing a playbook to update the pi cluster, I first needed to declare what systems the playbook is used with. To do that, I used the `hosts` key, and provided it with the `cluster` group name, which is defined in my `/etc/ansible/hosts` file, as the value.

```
---
- hosts: cluster

...
```

After the hosts are defined, modules can be added to update the nodes. To list the tasks, I used the `taks:` key, with the same indentation as the `hosts:` keyword. Instead of using a single value, I provided the `tasks:` keyword with a list of things to do. The first task I want to do when updating the nodes is to check that they running and connected. This can be accomplised with the [ping module](https://docs.ansible.com/ansible/ping_module.html) that I used earlier in the post. The ping module will try to connect to each node, verify that a usable python is installed, and return `pong` upon success. To add the module, I added `- ping: ~`, indented, to the line below `tasks:`:

```
---
- hosts: cluster

  tasks:
    - ping: ~
```

### Apt Module
After defining the ping module, I started to get a bit fancier. Well... a little bit fancier. Each node in my pi cluster is running some verison of Ubuntu, which uses apt as it's package manager. If I wanted to ssh into each node and update them manually, the steps I would follow would be to 1) run the command `sudo apt-get update` to update the repository cache, and 2) run `sudo apt-get upgrade` to actually install the updates. To recreate these commands in the playbook, I used the [apt module](https://docs.ansible.com/ansible/apt_module.html). To start with updating the repository cache, I added the following lines to my playbook:

```
- name: Update APT package manager repositories cache
  become: true
  apt:
    update_cache: yes
```

The `name:` defines the name of the task, and is the text printed out to the console when executing this step of the playbook. Setting the [`become`](https://docs.ansible.com/ansible/become.html) key to `true` tells Ansible to run the command with privilege escalation (sudo). Lastly, the remaining two lines run the `update_cache:` functionality of the apt module. 

With the repositories updated on each node, I can have ansible run the updates by adding the following lines to the playbook (after the cache update ones):

```
- name: Upgrade installed packages
  become: true
  apt:
    upgrade: dist
```

This set of commands is very similar to the last group. The `name:` again provides a description of what the task is doing, and privilege escalation is used again via `become: true`. The only difference is that the apt module is using the `upgrade: dist` command instead. This will run the updates for any installed packages on the system.

### Update Cluster Playbook

I then had a completed playbook to update the pi cluster:

```
---
- hosts: cluster

  tasks:
    - ping: ~

    - name: Update APT package manager repositories cache
      become: true
      apt:
        update_cache: yes

    - name: Upgrade installed packages
      become: true
      apt:
        upgrade: dist
...

```

The last step is to test it out! Playbooks can be executed using the `ansible-playbook` command:

```
ansible-playbook update-cluster.yml
```

When running the playbook, ansible will first attempt to gather facts about each node, and then begin to run each of the tasks defined in the playbook. At each step, it will print out the `name` of each task, followed by the status/result for each node. When it completes, all the nodes in the cluster should be updated. Now you can update three+ computers with a single command! Enjoy!
