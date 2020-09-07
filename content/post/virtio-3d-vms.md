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

So, Virgil basically allows libvirt to create *virtual 3D GPUs* to use in VMs.
This means, that I *should* be able to get high performing VMs, including the
graphics, on my Linux desktop.

## Setup

Enabling virgil for a VM using virt-manager actually ended up be much easier
that I expected it to be.

### Create a VM

<center>
<a href="img/posts/virtio-3d-vms/new_fedora_vm.png">
<img alt="Newly Created Fedora VM" src="/img/posts/virtio-3d-vms/new_fedora_vm.png" style="max-width: 100%;"/></a>
<div class="caption">Newly created Fedora VM</div>
</center>

First, create and install a new virtual machine using `virt-manager`. I
recommend going through your normal install process and then boot into the
installed system once, just to ensure that everything works as expected. If
things look good, shutdown the VM and open up the settings window.

### Enable VirtIO and 3D Acceleration

#### Spice Settings

In the settings menu, open up the *Display Spice* section.

<center> <a href="img/posts/virtio-3d-vms/display_spice_config_post.png">
<img alt="Virt-manager's Spice settings for a VM" src="/img/posts/virtio-3d-vms/display_spice_config_post.png" style="max-width: 100%;"/></a>
<div class="caption">In the VM's 'Display Spice' config, select 'None' for
Listen type, and check the box for OpenGL</div>
</center>

Select `Spice server` for `Type:`, and `None` for `Listen type:` (virgil only
works on local VMs right now). Lastly, make sure that the `OpenGL` checkbox
*is* checked. Hit `Apply`.

#### Virtio Settings

Next, select the *Video Virtio* section.

<a href="img/posts/virtio-3d-vms/video_config_post.png">
<img alt="Virt-manager's Video settings for a VM" src="/img/posts/virtio-3d-vms/video_config_post.png" style="max-width: 100%;"/></a>
<div class="caption">In the VM's video settings, switch to Virtio and select 3D
acceleration</div>
</center>

Switch to `Virtio` for `Model:`, and make sure to check the `3D acceleration`
checkbox. That's it! Start up the VM and check that it is working okay.

## Testing and Comparisons

### Youtube Video Playback

While configuring this for the first time, there were a few benchmarks I used
to tell if and how well it was working. The first one, was simply opening up
Firefox and trying to play a fullscreen Youtube Video (at 1440p).

Now to be fair, the video playback was still *okay* before I made this change.
However, the playback was *great* after it. Still, this wasn't a good measure,
but rather an initial test.


### Unigine Heaven Benchmark

My next step was to give the VM a *real* GPU test, so I downloaded the [Unigine
Heaven Benchmark](https://benchmark.unigine.com/heaven). First I got my
baseline by running the benchmark directly on my host system. *It should be
noted, I did have other applications running during these bench marks*.

<center>
<a href="img/posts/virtio-3d-vms/unigine_heaven_score_host_export.png">
<img alt="Unigine Heaven Benchmark - Host" src="/img/posts/virtio-3d-vms/unigine_heaven_score_host_export.png" style="max-width: 100%;"/></a>
<div class="caption">Unigine Heaven Benchmark running directly on the host (my
desktop)</div>
</center>

So not bad, and roughly what I expected. Next, I tried running it in the VM...

<center>
<a href="img/posts/virtio-3d-vms/unigine_heaven_score_vm_export.png">
<img alt="Unigine Heaven Benchmark - VM" src="/img/posts/virtio-3d-vms/unigine_heaven_score_vm.png" style="max-width: 100%;"/></a>
<div class="caption">Unigine Heaven Benchmark running inside the VM with
*shared* graphics</div>
</center>

While not as good of a result as on the host, it is a *very* respectable
result. One thing to note, is that the VM did have less cores and RAM assigned
to it compared to the host.

Additionally, my default VM basically *wouldn't even run* the benchmark. I was
able to open it, but the load screen ran frame-by-frame.


### Portal 2

With the Unigine Heaven bench mark running in my test VM, I decided to try the
next step... running a game. Now, I have *zero* intentions of running games in
my VMs, but this is the most common use case for having a GPU-passthrough
setup.

I thought a would try running a classic game: Portal 2. It's not a very heavy
resource game, but one that most certainly does *not* normally run in my VMs.
So, I installed the game, opened it, and started a level... and immediately was
looking at the ground.

That was when I indeed knew I was in a VM, because it  didn't actually have my
mouse capture. It just used my window input clicks from my host, which wasn't
enough to actually play the game.

<center>
<a href="img/posts/virtio-3d-vms/portal2_window.png">
<img alt="Playing Portal 2 in a Fedora VM" src="/img/posts/virtio-3d-vms/portal2_window.png" style="max-width: 100%;"/></a>
<div class="caption">Playing Portal2 at 2560x1440 resolution, inside my Fedora
VM.(I had it full screen but windowed it to show it was indeed in the VM)</div>
</center>

However, one shutdown and usb mouse pasthrough later... and I was playing
Portal 2! It was a little glitchy the first few seconds, but after that ran
fine enough. I think this is likely due to hitting the *virtualized* disk
during the initial load. Again, this is better performance than what I *need*,
so I am more than happy with it.



## Drawbacks/Limitations

While I'm very happy with the performance of my virtio VM, there are a few
drawbacks and limitations to keep in mind:

**Need to pass through devices for some things**: ... like a mouse when gaming
XD, or maybe a full HD if you need high IO.

**Linux Guests Only:** While researching, I saw [conference talks about getting
birgil working on Windows](https://www.youtube.com/watch?v=aBgYNDLXuyg) , but I
*think* currently this really only works with Linux guests.

<center>
<a href="img/posts/virtio-3d-vms/other_working_distros.png">
<img alt="Both Manjaro and Pop_OS! worked fine" src="/img/posts/virtio-3d-vms/other_working_distros.png" style="max-width: 100%;"/></a>
<div class="caption">Both my Manjaro and Pop_OS! VMs worked just fine with
virgl</div>
</center>

**Even on Linux some Distros might freak out a bit**:

- I've had weird issues switching it on while on some of my work RHEL 8 VMs. Not sure why
- I have tried it with Pop_OS! and Manjaro VMs and they seem to work.
- Fedora, my main use case works great.Creating a VM

<center>
<a href="img/posts/virtio-3d-vms/glitch_t470_fedora.png">
<img alt="My Fedora VMs didn't work on my T470 Thinkpad" src="/img/posts/virtio-3d-vms/glitchy_t470_fedora.png" style="max-width: 100%;"/></a>
<div class="caption">My Fedora VMs on my T470 Thinkpad (intel graphics only)
didn't seem to like virgl</div>
</center>

**Not entirely sure about hardware support**:
- So far mostly used on my desktop, which has a AMD RX580 GPU it uses for this
- Tried it on my T470 Thinkpad with integrated intel graphics, and a normal Fedora guest worked (I think?)
    - By Silverblue didn't seem to like it at all. Not sure if that was a Silverblue issue or being on the intel gpu issue... (verify on desktop)

## Conclusion
