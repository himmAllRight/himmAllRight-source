---
title: "Transitioning Server from Proxmox"
date: 2018-03-05
type: homelab
layout: homelab-page
image: img/header-images/drives1.png
---

I've been planning to move my server from Proxmox to just a normal server
install, to give me more control over everything. However, I don't want this to
be like the wild west of servers, where it is basically just a desktop with a
bunch of crap on it. I like how easy it is to spin up both containers and VMs,
and then continue to monitor/manage everything. 

So, I am creating a list of things I want to have at least *somewhat* figured
out before officially making the switch. Some things might be un-check even
though I have an idea about what to do. I will check things off as I go through
and fully ensure I know what to do for that task, and optionally write something
down about it.

### Host

The host system needs a few things it needs to support. Most are broken down
into the other categories below, but some are specific to the Host, which will
be here.

**Checklist**:

- [ ] Determine OS/Distro to use
- [ ] Monitoring System
- [ ] Easy Management System for Containers/VMs (ex: Ansible/Chef)

### Data

Need to continue to use ZFS, and be able to import my current ZFS pools. It also
needs to support LUKS, since I use it for my backups. Lastly, it would be nice
if it was easy enough to setup samba shares.

**Checklist**:

- [ ] Test OS ZFS install/Setup
- [ ] Import ZFS Pools
- [ ] LUKs setup and working
- [ ] Ensure Backup Process Works

### VMs

Want to continue to use KVM. Needs to allow me to use ~virsh~ and other tools.
Ideally, I'd like to be able to connect using ~virt-manager~ and similar GUI
tools, even from Distros without ~ssh-askpass~, like Solus. I need to figure out
and export just a couple of VMs, but I think that just requires me to export
them to qcow2 images, and use the "disk" into a new VM. Additionally, I think I
[already figured that
out](http://ryan.himmelwright.net/post/exporting-proxmox-vms/). The main things
I need to learn/do for the VM stuff is to figure out the tool set I want to use
for management, especially remotely.

**Checklist**:

- [X] Export desired VMs
- [ ] Run VMs on ZFS or LVM pools
- [ ] Learn how to create VMs
- [ ] Network so VMs on main network
- [ ] Remotely View GUI VMs
- [ ] Remotely Edit VMs (Easily)
- [ ] Auto Backups for VMs

### Containers

I want to continue to use LXC containers for a large majority of the server's
tasks. So, I plan to use LXD, and many of these tasks will be about configuring
it so that I have all the ease of managing containers as I did in Proxmox. Also,
unlike Proxmox, I want to have the server run and support Docker cotnainers.

#### LXC/LXD
**Checklist**:

- [X] Install Setup LXC
- [ ] Run Containers on ZFS or LVM pools?
- [ ] Easily Create New (with options Proxmox provides)
- [ ] Network so Containers on main network
- [ ] Remotely Edit Containers (Easily)
- [ ] Auto Backups 


#### Docker
**Checklist**:

- [X] Docker Setup
- [ ] Containers on ZFS or LVM pools?
- [ ] Network so Containers on main network
- [ ] Auto Backups


## Notes

- So, I just installed [cockpit](http://cockpit-project.org/) on the test
  server. It's been a long time since I have used it, and it has really
  improved. It has interfaces to my VMs and docker containers. It's not as
  extensive as Proxmox, but honestly, goes enough of the way there for me.
