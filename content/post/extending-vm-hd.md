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

#### Assumptions

Before we get started, I just want to point out that this method is
specific to the setup I currently have for *my* VMs. Specifically, I
am running my VMs using kvm/qemu and virt-manager, with qcow2 images
for the virtual disks. Additionally, the VM I was extending was
installed with LVM and it's main partition was formatted with an xfs
filesystem. Just note that some steps may differ if a different environment
is being used.

## Clone VM

<center>
<a href="../../img/posts/extending-vm-hd/clone-vm.png"><img alt="Clone VM window in Virt Manager" src= "../../img/posts/extending-vm-hd/clone-vm.png" style="max-width: 100%;"/></a>
<div class="caption">Cloning the VM in Virt Manager</div>
</center>

While not required, it is not a *bad* idea to first clone the VM (just
in case anything gets messed up). If using *virt manager*, cloning a
VM is as simple as right clicking a *powered down* VM, and selecting
"*Clone...*". A window will pop up with options for cloning the
VM. Make and desired name changes amd hit *Clone*. Shortly after, the
clone should be ready.

**NOTE**: If making changing to the *VM's* settings, be careful to not accidently
fire up the *VM clone*, and get all mad thinking the changes haven't
been applied...

## Extend qcow2 file

The first step in resizing the the virtual drive is to first expand
the `qcow2` image. By default, the images tend to be stored at
`/var/lib/libvirt/images/` and will require `root` privledges to
access. Virt-Manager can be used to double check which image the VM is
using for its disk. To resize the qcow2 image, use the `qemu-img
resize` command, providing it image file path/name and then the size
to expand it. For example, I used `+40G` in my command (`qemu-img
resize Jenkins.qcow2 +40G`) to extend my image by 40GB.

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

The command `qemu-image info` is helpful to use to check the size of
the image, and to verify that the resize worked.

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
