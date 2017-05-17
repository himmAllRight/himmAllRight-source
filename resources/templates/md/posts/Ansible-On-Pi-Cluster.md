{:layout :post
:title  "Configuring Ansible on the Pi Cluster"
:date "2017-05-17"
:author "Ryan Himmelwright"
:tags ["Homelab" "Cluster" "Pi" "DevOps" "Ansible"]
:draft? false
}

In my [previous post](http://ryan.himmelwright.net/posts/Setting-up-the-pi-cluster/), I setup my [pi cluster](http://ryan.himmelwright.net/pages/homelab/#cluster) and installed the variations of Ubuntu 16.04 Server on each of them. With the cluster setup, I needed an easy way to interact and maintain the systems. This is where [Ansible](https://www.ansible.com/) comes in.

<!-- more -->

## Ansible
Ansible is an open source configuration management and automation system, written in Python, and backed by [Red Hat](http://www.redhat.com). It allows management of groups of computers through the use of modules, standalone units of work (ex: apt, ping, rpm, etc). Ansible is scriptable using playbooks, YAML files that define a set of tasks to orchestrate on a single or group of computers. These scripts can be edited and version controlled, creating a simple [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_Code) setup.

## Setting up the User Account
Ansible exectute commands on the PIs, from user-accounts (ryan) that I setup in the last post. Many of these commands will require Root privledges. While I setup sudo and added the accounts to the `sudo` group in the last post.... it requires a password. Ansible doesn't like this, so I had to edit the sudo configuration so that users in the `sudo` could run `sudo` commands with out a password. To do this, I opened the `sudoers` file:


```
sudo visudo
```

and added the following line to the end of the file:

```
ryan  ALL=(ALL:ALL) NOPASSWD: ALL
```

I repeated this on each of the nodes. I was now longer promted for a password when running `sudo` commands, and Ansible was happy.



## Setup SSH Keys
Well... Ansible was *almost* happy. 

Ansible's default communication method is ssh, and by default, `ssh` prompts me for passwords to loging, which Ansible did not like. Ansible *really* hates passwords. So, I had to configure ssh to use keys. Honestly, this is proabaly a good step to do regardless, now that the ryan account no longer needs a password when running `sudo`. To do this, I sent the already generated public key on my [main computer](../../pages/homelab/#alakazam), to the pis:

```
scp ~/.ssh/id_rsa.pub pi0:~/.ssh/alakazam_id.pub
scp ~/.ssh/id_rsa.pub pi1:~/.ssh/alakazam_id.pub
scp ~/.ssh/id_rsa.pub bpi:~/.ssh/alakazam_id.pub
```

*Note: If keys are not already generated, they can be created using the command:*

```
ssh-keygen
```

With Alakazam's public key on each node, I appended it to each of the pi's `authorized_keys` file by sshing into the pi and running the command:

```
cat ~/.ssh/alakazam_id.pub >> ~/.ssh/authorized_keys
```

Afterwards, if done correctly, a password should no longer be required when sshing to the pis.

**GIF ANIMATION OF SSHING INTO NODE**


### Optional SSH Stuff...

#### Key Only Login
To help secure access to the PIs, I configured sshd to disable password logins, and only allow connections from approved keys, now that those are setup. To disable password authentication, I opened the `/etc/ssh/sshd_config` file, found the `PasswordAuthentication yes` line, uncommented it, and changed the `yes`, to a `no`.

While I was in the `sshd_config` files, I also set `PermitRootLogin` to `no`, for good measure.

I then reset the `sshd` service:

```
sudo systemctl restart sshd
```

Afterwards, I was unable to login to the PIs from a computer with unauthorized ssh keys.

**GIF OF FAILED LOGIN**

But, I was still able to loging from the authorized computer.

**GIF OF SUCCESSFULL LOGIN**


#### Other Methods for Key Setup
Just as a note, there are other real nice ways to transfer ssh keys between servers. I know on some distributions, such as CentOS, there is a script called NAME that can be installed, and it can setup keys with the single command:

```
ssh-copy
```

This scrip is considered old by some, which is why it is not included in the distribution I use (Solus), so be aware of that. If it's available to you though, you might as well use it.


## Install Python


## Install Ansible

I have a confession. You know how I was being fun and cheery by anthropomorphisizing ansible, saying that it was *"happy"* or *"frusterated"* during the previous steps? That wasn't true. Ansible wasn't installed yet. *So... to install Ansible...*

```
sudo eopkg it ansible
```
Again, this might be `sudo apt-get install ansible`, `sudo dnf install ansible`, or `pacaur -S ansible` depending on whatever distrobution you are using.


## Notes for post:
-- added `ryan` user on rpis, gave sudo permissions     
	- Made ryan able to use sudo without password by adding `ryan ALL=(ALL) NOPASSWD: ALL` to the bottom of my `visudo` file.

-- setup ssh keys

-- install python on rpis (bpi was okay)

-- install on host (was already on solus)
