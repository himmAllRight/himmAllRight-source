{:layout :post
:title  "Updating the Pi Cluster with Ansible"
:date "2017-05-23"
:author "Ryan Himmelwright"
:tags ["Homelab" "Cluster" "Pi" "DevOps" "Ansible"]
:draft? false
}

With Ansible configured on the Pi cluster, it's time to get it to do something useful. When working with a clustered system, even simple tasks can become tedious and time consuming. Once such task is updating the system. While I could manually update each of the 3 pi nodes, it isn't really scalable with 10 or 30 nodes, let alone 100. Tools like Ansible, make doing tasks like updating clustered systems, trivial again. In this post, I will walk through setting up an Ansible playbook to update my Pi cluster.

<!-- more -->

### Hosts File
The first task when using Ansible is to setup the `hosts` file. No, not the normal `/etc/hosts` file, but the *other* one *just* for Ansible, which can be found at `/etc/ansible/hosts`. Configuring the Ansible hosts file is fairly straight forward. Computer groups are defined using `[brackets]`, and computer ip/hostnames of the group are listed below. For example:

One nice feature of group definitions, is that hierical structures can be constructed by using the `:child` suffix to create groups of groups.. For example, for my [homelab](../../pages/homelab), I like to make an ansible hosts file that splits out my servers based on their distrobution, and then group those by their packaging type. This makes it easier for me to do generic updates, which is what I mostly use ansible for (at this point). So, for example:

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

For use with the cluster, I like to keep it simple, although I have opted to create rpi/bpi subgroups:

```
[cluser:children]
rpis
bpis

[rpis]
pi0
pi1

[bpis]
bpi
```

### Ping Hosts
Once the hosts file is setup, we can test it with the `ping` module. I tested my `cluser` group, as well as the `rpis` and `bpis` subgroups.

**PING TEST ANIMATION**

```
ansible rpis -m ping
ansible bpis -m ping
ansible cluster -m ping
```

This should work, assuming the steps of [the last post](../Ansible-On-Pi-Cluster) were done correctly. If not, double check that post and make sure everything checks out.

### Playbooks

### Apt Module

#### ModuleS

### Update Cluster Playbook
