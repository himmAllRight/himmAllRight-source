+++
title   = "Running VMs with VirtIO 3D Acceleration"
date    = "2020-09-07"
author  = "Ryan Himmelwright"
image   = "img/posts/virtio-3d-vms/obx-sunrise.jpeg"
caption = "Kitty Hawk, NC"
tags    = ["linux", "Homelab", "KVM", "fedora",]
draft   = "True"
Comments = "True"
+++


<!--more-->


## Background
* Tested out Parallels Desktop on MacOS. It worked great, graphics included.

* I wanted to figure out a way to work *comfortably* in Linux VMs, on Linux hosts.

* I have recently been experimenting with VFIO, and while it is really cool and works well, it can be a bit of a pain. Also, to *really* benefit and have a more stable setup, I would want a second GPU.

## Setup

### Create a VM
- Create a VM in `virt-manager`
- Finish the full install process like normal, login, and shutdown


### Enable VirtIO and 3D Acceleration
- Switch the Video settings


### Increase Video Memory?
- Edit the VM with `virsh`
- Increase the video memory


## Testing and Comparisons

### Youtube Video Playback


### Unigine Heaven Benchmark


### Portal 2


## Drawbacks/Limitations

### Need to pass through devices for some things
... like a mouse when gaming XD

### Linux Guests Only?
- I've seen conference talks about getting it working on Windows, but I don't *think* that is default or fully working yet? Again... I'm new to this...

### Even on Linux some Distros might freak out a bit
- I've had weird issues switching it on while on some of my work RHEL 8 VMs. Not sure why
- I have tried it with Pop_OS! and Manjaro VMs and they seem to work.
- Fedora, my main use case works great.Creating a VM

### Not entirely sure about hardware support
- So far mostly used on my desktop, which has a AMD RX580 GPU it uses for this
- Tried it on my T470 Thinkpad with integrated intel graphics, and a normal Fedora guest worked (I think?)
    - By Silverblue didn't seem to like it at all. Not sure if that was a Silverblue issue or being on the intel gpu issue... (verify on desktop)

## Conclusion
