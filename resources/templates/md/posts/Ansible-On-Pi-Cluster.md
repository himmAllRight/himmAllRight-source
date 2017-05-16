{:layout :post
:title  "Configuring Ansible on the Pi Cluster"
:date "2017-05-10"
:author "Ryan Himmelwright"
:tags ["Homelab" "Cluster" "Pi" "DevOps" "Ansible"]
:draft? false
}

In my [previous post](http://ryan.himmelwright.net/posts/Setting-up-the-pi-cluster/), I setup my [pi cluster](http://ryan.himmelwright.net/pages/homelab/#cluster) and installed the variations of Ubuntu 16.04 Server on each of them. With the cluster setup, I needed an easy way to interact and maintain the systems. This is where [Ansible](https://www.ansible.com/) comes in.

<!-- more -->

## Ansible
Ansible is an open source configuration management and automation system, written in Python, and backed by [Red Hat](http://www.redhat.com). It allows management of groups of computers through the use of modules, standalone units of work (ex: apt, ping, rpm, etc). Ansible is scriptable using playbooks, YAML files that define a set of tasks to orchestrate on a single or group of computers. These scripts can be edited and version controlled, creating a simple [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_Code) setup.

## Adding an User Accounts



## Setup SSH Keys
Ansible's default communication method is ssh, so the first thing I did was to configure ssh keys between the systems. To do this, I sent my already generated keys to the pis:

```
scp ~/.ssh/id_rsa.pub pi0:~/.ssh/alakazam_id.pub
scp ~/.ssh/id_rsa.pub pi1:~/.ssh/alakazam_id.pub
scp ~/.ssh/id_rsa.pub bpi:~/.ssh/alakazam_id.pub
```

*Note: If keys are not already generated, they can be created using the command:*

```
ssh-keygen
```

With my [main computer](../../pages/homelab/#alakazam)'s keys on each node, I added the key to each of the pi's `authorized_keys` file by sshing into the pi and running the command:

```
cat ~/.ssh/alakazam_id.pub >> ~/.ssh/authorized_keys
```

Afterwards, if done correctly, a password should no longer be required when sshing to the pis.

**GIF ANIMATION OF SSHING INTO NODE**


### Other Methods for Key Setup
Just as a note, there are other real nice ways to transfer ssh keys between servers. I know on some distributions, such as CentOS, there is a script called NAME that can be installed, and it can setup keys with the single command:

```
ssh-copy
```

This scrip is considered old by some, which is why it is not included in the distribution I use (Solus), so be aware of that. If it's available to you though, you might as well use it.


## Install packages


## Notes for post:
-- added `ryan` user on rpis, gave sudo permissions     
	- Made ryan able to use sudo without password by adding `ryan ALL=(ALL) NOPASSWD: ALL` to the bottom of my `visudo` file.

-- setup ssh keys

-- install python on rpis (bpi was okay)

-- install on host (was already on solus)
