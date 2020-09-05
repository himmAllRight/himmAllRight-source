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

### Motivaton

When I was on vacation the other week, I only brought my [macbook
pro](http://ryan.himmelwright.net/post/new-2019-16inch-mbp/), but I
wanted to still be able to jump into Linux while I was away. I've tried
VirtualBox in the past, kand while it's *fine* for running headless installs, I
find that it's really not a great experience on macOS when running full desktop
environments. So, I downloaded the free trial of [parallels desktopi
15](https://www.parallels.com/blogs/just-released-parallels-desktop-for-mac/)
for the mac, and honestly... it was great.

*Screenshot of Parallels/Product logo?*

It handled graphics on both my Windows and Linux guests wonderfully. I could
full screen, and felt like I was running that OS on my macbook. I was sad when
the trial was over, and decided not to buy the subscription. My main reason
being... I am a Linux user and my VM computer is *not* my macbook, it's my
Linux desktop.

I love libvirt and virt-manager, but using parallels showed me that I really
needed to figure out who to improve the graphics situation of my VMs to catch
up. I wanted to be able to work in guest VMs full screen, without lagging
UI or feeling like I was *in* a VM.

### VFIO - GPU Passthrough

Prior to my trip, I had been experimenting *once again* with VFIO... and
actually got it working* for the first time. If you don't know what this means,
basically in Linux it is possible to pass a full device, like a GPU, through to
a VM to be used directly. The technology was made more widely known a few years
ago from the "X Gamers, 1 CPU" serries of videos Linux Tech Tips made.

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/LuJYMCbIbPk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<div class="caption">The first video of the serries, 2 Gaming PCS 1 Tower</div>
</center>


I was able to temporarily run
Proxmox and Unraid on my desktop, and pass my gpu directly to Fedora VMs.
While it was a neat experiment, I realized the setup it can be a bit of a pain.

I currently only have one GPU in my desktop, so to pass it to the VM I had to
disable it from the host, and pass it along. This meant that I had to start the
VMs from another device (which isn't *that* bad), but worse, the gpu would
often get stuck while being passed around so I always had to reboot my hoest
whenever the VM restarted... which defeated the point.

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/6T_-HMkgxt0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>


So to *really* utilize VFIO and have a more stable setup, I would want a second
GPU. Honestly though, I realized this setup wasn't what I was looking for. KVM
gpu passthrough is a great option if you run Linux as your main computer, but
want to be able to boot into a Windows VM to play games, but VFIO is slowly
becoming overkill even for *that*, as gaming support on Linux just keeps
getting better.

Aside from having an occasional Windows VM to play around with, I mostly wanted
to just run Linux VMs on a Linux host. I needed to figure out how to let my VMs
utilize the power of my GPU, without the complications of GPU passthrough...

### Virgil

Let me introduce, [virgil](https://virgil3d.github.io). According to the
projects website:

>Virgil is a research project to investigate the possibility of creating a virtual 3D GPU for use inside qemu virtual machines, that allows the guest operating system to use the capabilities of the host GPU to accelerate 3D rendering. The plan is to have a guest GPU that is fully independent of the host GPU.

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
