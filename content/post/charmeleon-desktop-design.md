+++
title  = "Designing my new Ryzen Workstation"
date   = "2018-11-20"
author = "Ryan Himmelwright"
image  = "img/homelab/new_monitor4.jpg"
tags   = ["Hardware", "Linux", "Ryzen", "Homelab",]
draft  = true
Comments = "True"
+++

Over the past few years (particularly since moving to the [T470](../my-t470/)
as my main device, I have been anticipating what an eventual desktop
workstation build will look like. For awhile, I was convinced that I was going
to make a [muti-socket, used xeon
build](https://www.techspot.com/review/1155-affordable-dual-xeon-pc/). In 2017
however, AMD released their [Ryzen](https://en.wikipedia.org/wiki/Ryzen)
CPUs, which caught my attention.

<!--more-->

## Why a Desktop?

<a href="../../img/posts/chameleon-desktop-design/kadabra-cpu-usage.png"><img alt="The KDE Plasma 5 extend display GUI" src="../../img/posts/charmeleon-desktop-design/kadabra-cpu-usage.png" style="max-width: 100%;"/></a>
<div class="caption">My T470 has been a little tight on resources.</div>

My laptops have served the majority of my needs well the last few years, I have
been feeling a bit restricted when trying to do more complicated and demanding
tasks. While I still agree with a "*interface with a low-powered, portable
computer, and remote into more powerful ones when needed*" mentality, I enjoy
having *one* of those power computers being my physical, main workstation
desktop.

## Workstation Goals

<a href="../../img/posts/chameleon-desktop-design/ryzen-logo.png"><img alt="The KDE Plasma 5 extend display GUI" src="../../img/posts/charmeleon-desktop-design/ryzen-logo.png" style="max-width: 100%;"/></a>
<div class="caption">My T470 has been a little tight on resources.</div>

As much as people may think I want to build a computer for the fun of it, if
I'm designing a workstation, I have goals in mind for it. Additionally, 98% of
online build guides are for designing *gaming* desktops... which is not what I
was doing. So, what I wanted *my build* to have, likely deviates from the
much of the *suggested* guidance found online.

#### More Cores


I tend to have workloads that can really benefit from multiple cores (and
threads). For example, I run a bunch of virtual machines, often at the same
time. While my server's 4 core Xeon handles day to day VMs just fine, it is
nice to have a workstation with a bunch of cores to spread a virtualised
cluster across. Beyond VMs, I compile code, compress/decompress packages of
files, and occasionally encode audio/video files. All tasks that love more
cores.

#### Lots of (*fast*) Ram

When running VMs, lots of RAM is actually more desirable than more cores. For
example, when running my 6 24-7 VM's, my server's 4-core Xeon will typically be
15-35% utilized. It's 20GB or RAM however, is almost always fully used. If I
want more cores, I'll need lots of RAM. Also... I use electron apps (Slack
etc.)... so, yea....

Lastly, because I'm looking at Ryzen builds, the RAM has to be *fast*.
More than other CPU architectures, Ryzen actually runs *faster* with faster
RAM.

#### Fast Storage

This goal of this build is for it to be a multi-tasking beast. If I have a
several CPU threads, running several VMs and a bunch of applications, and a
pile of *fast* RAM moving data around... I need good *fast* storage that has
[MOAR IOPs](https://www.youtube.com/watch?v=Bh_f0uof7Jw&feature=youtu.be&t=359)
to support all of these tasks that will compete for disk access. While I
wouldn't mind having room to throw a pair 3.5" rust drive to configure as a ZFS
data pool down the road, the goal for the initial *primary* drive of this build
is the most IOPs I can *afford*. So, a 2.5" SATA SSD at the very *least*.

#### *Some* Gaming Ability

While it doesn't have to be a *gaming* machine... I would like to be able to
play the *occasional* game. While I don't mind playing games with lower graphic
settings, on my laptops even with the lower settings they spike up the
temperature and nearly max out the CPU... which I *do* mind. I don't
need to play the most demanding games at *Ulimate* graphics settings, I do
want to play basic games at medium settings. A discrete graphics card would be
nice, ideally an AMD one due to their recent commitment to pushing forward
their open source drivers.

#### Good Budget "Base", Ability to Upgrade

Most importantly, I want this build to be a solid *base* that I can upgrade
over the next several years. That is easily the *main* advantage of switching
to a desktop over a laptop for my main rig. I want this build designed so that
over the next few years I can easily max out the RAM (so 4 RAM slots and
preferably 16GB sticks), add storage, or upgrade the CPU and/or GPU, and my
needs grow. For this to work best, I want my more long-time parts (case, power
supply, motherboard), to be long-lived and support the easy upgrading of the
other components.

## Final Build Selections


#### Name: Charmeleon

<a href="../../img/posts/chameleon-desktop-design/charmeleon.png"><img alt="The KDE Plasma 5 extend display GUI" src="../../img/posts/charmeleon-desktop-design/charmeleon.png" style="max-width: 50%; float: right;"/></a>

Since my last desktop build was named "Charmander", I figured "Charmeleon" was
fitting. Also, I', free to rename it to "Charzard" in the future if I *evolve*
the build to a future Ryzen 7...

#### CPU: Ryzen 5 2600

While I ideally wanted a Ryzen 2700, it made my build out of budget... and
coming from 4 core/4 thread systems... it's likely that I don't *need* 8
cores/16 threads yet. Honestly, 4 cores/8 threads would be a noticeable
improvement from what I've been using... which is why I originally
considered the Ryzen 5 2400g, which I planned to start with and upgrade to the
2700 + a GPU once I had the spare money. However, [someone on the level1tech
forums](https://forum.level1techs.com/t/finalizing-an-upgradable-ryzen-linux-build/134670/2)
reminded me that the 2600 was the same price as the 2400g, and I could get that
plus a GPU for not much more cost. After thinking it over, I realized that was
my best option.

#### Motherboard: MSI B450 Tomahawk

#### RAM: G.Skill - Trident Z 32GB (2 x 16GB) DDR4-3200Mhz RAM

#### GPU: Sapphire 1024 4GB PULSE Radeon RX 560

#### Case: Fractal Design - Meshify C Dark TG ATX Mid Tower

#### PSU: EVGA - SuperNOVA G4 650W 80+ Gold, fully modular ATX PSU -**

#### Storage: One of my Samsung 850 Evo SSDs (temp) -**

[pc part picker
list](https://pcpartpicker.com/user/himmelwr/saved/#view=MhbcYJ)
