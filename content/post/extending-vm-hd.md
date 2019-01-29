+++
title  = "Extending VM Hard Drive"
date   = "2019-02-01"
author = "Ryan Himmelwright"
image  = "img/header-images/hdd-replace.jpg"
caption= "My Desk, Durham, NC"
tags   = ["Linux", "Homelab", "filesystems", "KVM", "LVM",]
draft  = "False"
Comments = "True"
+++

Last week I extended my Jenkin's VM server's HD. Then I extended the
max size of one of the job's docker containers... which also runs on
that HD, so I need to extend it again. If you ever have to do
something twice... it *better* be documented for the third time. So
here we are.

<!--more-->

## Clone VM
You don't have to, but it's not a *bad* idea.

## Extend qcow2 file

Expand the `qcow2` image using the `qemu-img resize` command. You give
it the image name and then the size to expand. For example, I used
`+40G` in my command (`qemu-img resize Jenkins.qcow2 +40G`) to extend
my image 40GB.

```bash
root@ninetales:/var/lib/libvirt/images# qemu-img info Jenkins.qcow2 
image: Jenkins.qcow2
file format: qcow2
virtual size: 20G (21474836480 bytes)
disk size: 20G
cluster_size: 65536
Format specific information:
    compat: 1.1
    lazy refcounts: true
    refcount bits: 16
    corrupt: false

root@ninetales:/var/lib/libvirt/images# qemu-img resize Jenkins.qcow2 +40G
Image resized.

root@ninetales:/var/lib/libvirt/images# qemu-img info Jenkins.qcow2 
image: Jenkins.qcow2
file format: qcow2
virtual size: 60G (64424509440 bytes)
disk size: 20G
cluster_size: 65536
Format specific information:
    compat: 1.1
    lazy refcounts: true
    refcount bits: 16
    corrupt: false
    
root@ninetales:/var/lib/libvirt/images# 
```

## Gparted Live ISO
For the next few steps, it is a good idea to boot the system from a
live CD. That way, the disk isn't being used, and if you use a live
ISO like `gparted`, it has nice graphical tools to use to resize
everything.

(When you boot up and don't see the new space available to to
volume... make sure you didn't boot up the backup VM XD. Opps)

#### LVM Resize

My VM is installed using LVM volumes, so I have to resize them in
order to resize the filesystem partition.


<center>
<a href="../../img/posts/extending-vm-hd/gparted-live-iso.png"><img alt="Booting into the Gparted live ISO" src= "../../img/posts/extending-vm-hd/gparted-live-iso.png" style="max-width: 100%;"/></a>
<div class="caption">Booting into the Gparted live ISO</div>
</center>

<center>
<a href="../../img/posts/extending-vm-hd/gparted-resize.png"><img alt="Resizing the partition in Gparted" src= "../../img/posts/extending-vm-hd/gparted-resize.png" style="max-width: 100%;"/></a>
<div class="caption">Resizing the partition in Gparted</div>
</center>

#### Grow XFS

It wasn't a mounted volume from the live disk, so I booted into the
VM. However, this meant I couldn't auto complete tab in my shell
because it spit out there's no disk space. Looks like the `xfs_growfs`
worked though.

```bash
[ryan@mr-mime ~]$ sudo xfs_growfs /dev/centos/root
(... Ryan removed output for the post...)
data blocks changed from 4851712 to 15322112

[ryan@mr-mime ~]$ df -h
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/centos-root   59G   19G   40G  32% /
devtmpfs                 1.9G     0  1.9G   0% /dev
tmpfs                    1.9G  8.0K  1.9G   1% /dev/shm
tmpfs                    1.9G  8.7M  1.9G   1% /run
tmpfs                    1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/vda1                497M  231M  267M  47% /boot
tmpfs                    379M     0  379M   0% /run/user/1000
```
That's about it. :)
