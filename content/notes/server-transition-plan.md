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

## Pre Planning

### Host

The host system needs a few things it needs to support. Most are
broken down into the other categories below, but some are specific to
the Host, which will be here.

**Checklist**:

- [X] Determine OS/Distro to use (Ubuntu 18.04, 16.04 fallback)
- [ ] Monitoring System
- [ ] Easy Management System for Containers/VMs (ex: Ansible/Chef)

### Data

Need to continue to use ZFS, and be able to import my current ZFS pools. It also
needs to support LUKS, since I use it for my backups. Lastly, it would be nice
if it was easy enough to setup samba shares.

**Checklist**:

- [X] Test OS ZFS install/Setup
- [X] Import ZFS Pools
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

- [X] Replace Meowth with new VM
- [X] Export desired VMs
- [X] Learn how to create VMs
- [X] Network so VMs on main network
- [X] Remotely View GUI VMs
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
- [ ] Easily Create New (with options Proxmox provides)
- [ ] Network so Containers on main network
- [ ] Remotely Edit Containers (Easily)
- [ ] Auto Backups 


#### Docker
**Checklist**:

- [X] Docker Setup
- [ ] Network so Containers on main network
- [ ] Auto Backups

## Transition Steps

- [X] Export All Proxmox VMs 
- [X] Export All Proxmox Containers 
- [X] Run Test install (attached drive) 
- [X] Install OS 
- [X] Setup ZFS 
- [X] Import Pools 
- [X] Setup KVM/QEMU 
- [ ] Setup LXC/LCD 
- [X] Configure Bridged Network
- [ ] Import VMs/Contaienrs

## Notes

- So, I just installed [cockpit](http://cockpit-project.org/) on the
  test server. It's been a long time since I have used it, and it has
  really improved. It has interfaces to my VMs and docker
  containers. It's not as extensive as Proxmox, but honestly, goes
  enough of the way there for me.

- Now that I am using Ubuntu/Fedora systems as my main OS, I should be
  able to easily remote manage using virt-manager as well. Works so
  far on my test server.
  
- I have setup ZFS stuff on the test server. However, I won't really
  be able to test the pool import until I test it on the actual
  server. 
  
- I am thinking that I will setup a vpn VM that I can use for remote
  access to the network. This might be the most secure way to do
  remote management anyway.
    
-- Doing it

- Okay, I exported most of the VMs this morning and imaged my
Ubuntu 18.04 Server USB drive. Tonight, I've swapped the SSDs, which
are luckily the same one :).

- I installed Ubuntu Server on the new SSD.

- I first ran updated and setup ssh. No issue. Then I decided to try
  the part that is more difficult... at least for me right
  now. Setting up the VM bridge. It actually wasn't that bad and seems
  to be working :). I owe all thanks to [this
  post](https://www.linuxtechi.com/install-configure-kvm-ubuntu-18-04-server/)
  though... it was *very* helpful.
  
- I just installed `zfsutils-linux` and `zfs-initramfs`. I think I am
  going to try a reboot and insert my drives (took them out for
  safety). Will I be able to detect and then just import the pools? I
  guess I'll find out in a few minutes... 
  
  Fingers crossed...  
  
- It worked, although I didn't actually install the packages before
  the upgrade. Opps.
	
- I imported the pools and everything. This morning, I've upgraded the
  pools and am now in the process of scrubbing them.

- I also setup ansible and ran my ubuntu server playbooks :)

-- 

- So it's been a few days, and everything still seems to be up and
  working. I've easily setup and configured a few dev VMs through
  virt-manger on kadabra, and it works great. I would still like a
  better way to do it remotely, but I think setting up my VPN like
  I've planned will be the best way to do that, and cockpit will be
  enough for when I am truely remote.
  
- I still need to set up the container stuff, and put in place some
  automation system, but the basics are all up and running.
