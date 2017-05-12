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
Ansible is an open source configuration management and automation system, written in Python, and backed by [Red Hat](http://www.redhat.com). It allows management of groups of computers through the use of modules, standalone units of work (ex: apt, ping, rpm, etc). Ansible is scriptable, via playbooks, a YAML file that can define a set of tasks to orchestrate on a single or group of computers. 



## Notes for post:
-- added `ryan` user on rpis, gave sudo permissions     
	- Made ryan able to use sudo without password by adding `ryan ALL=(ALL) NOPASSWD: ALL` to the bottom of my `visudo` file.

-- setup ssh keys

-- install python on rpis (bpi was okay)

-- install on host (was already on solus)
