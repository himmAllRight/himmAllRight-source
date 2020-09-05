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
**Image of Fedora VM Created?**

- Create a VM in `virt-manager`
- Finish the full install process like normal, login, and shutdown


### Enable VirtIO and 3D Acceleration
- Switch the Video settings

**Image of Video Settings**
<center>
<a href="img/posts/virtio-3d-vms/video_config_post.png">
<img alt="Virt-manager's Video settings for a VM" src="/img/posts/virtio-3d-vms/video_config_post.png" style="max-width: 100%;"/></a>
<div class="caption">In the VM's video settings, switch to Virtio and select 3D
acceleration</div>
</center>

**Image of Spice Settings**
<center>
<a href="img/posts/virtio-3d-vms/display_spice_config_post.png">
<img alt="Virt-manager's Spice settings for a VM" src="/img/posts/virtio-3d-vms/display_spice_config_post.png" style="max-width: 100%;"/></a>
<div class="caption">In the VM's 'Display Spice' config, select 'None' for
Listen type, and check the box for OpenGL</div>
</center>


## Testing and Comparisons

### Youtube Video Playback


### Unigine Heaven Benchmark
**Image of Host Benchmark**
<center>
<a href="img/posts/virtio-3d-vms/unigine_heaven_score_host_export.png">
<img alt="Unigine Heaven Benchmark - Host" src="/img/posts/virtio-3d-vms/unigine_heaven_score_host_export.png" style="max-width: 100%;"/></a>
<div class="caption">Unigine Heaven Benchmark running directly on the host (my
desktop)</div>
</center>

**Image of VM Benchmark**
<center>
<a href="img/posts/virtio-3d-vms/unigine_heaven_score_vm_export.png">
<img alt="Unigine Heaven Benchmark - VM" src="/img/posts/virtio-3d-vms/unigine_heaven_score_vm.png" style="max-width: 100%;"/></a>
<div class="caption">Unigine Heaven Benchmark running inside the VM with
*shared* graphics</div>
</center>


### Portal 2

**Image of Game Looking at ground?**

- I first tried and was immediately that I was in a VM... that my mouse wasn't
    passed through to.


**Image of VM Game**

<center>
<a href="img/posts/virtio-3d-vms/portal2_window.png">
<img alt="Playing Portal 2 in a Fedora VM" src="/img/posts/virtio-3d-vms/portal2_window.png" style="max-width: 100%;"/></a>
<div class="caption">Playing Portal2 at 2560x1440 resolution, inside my Fedora
VM.(I had it full screen but windowed it to show it was indeed in the VM)</div>
</center>

- After passing in the mouse, it worked well enough


## Drawbacks/Limitations

### Need to pass through devices for some things
... like a mouse when gaming XD

### Linux Guests Only?
- I've seen conference talks about getting it working on Windows, but I don't *think* that is default or fully working yet? Again... I'm new to this...

### Even on Linux some Distros might freak out a bit

**Side-by-side Image of Manjaro and Pop working?**

- I've had weird issues switching it on while on some of my work RHEL 8 VMs. Not sure why
- I have tried it with Pop_OS! and Manjaro VMs and they seem to work.
- Fedora, my main use case works great.Creating a VM

### Not entirely sure about hardware support
- So far mostly used on my desktop, which has a AMD RX580 GPU it uses for this
- Tried it on my T470 Thinkpad with integrated intel graphics, and a normal Fedora guest worked (I think?)
    - By Silverblue didn't seem to like it at all. Not sure if that was a Silverblue issue or being on the intel gpu issue... (verify on desktop)

## Conclusion
