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

My laptops have served the majority of my needs well the last few years, I have
been feeling a bit restricted when trying to do more complicated and demanding
tasks. While I still agree with a "*interface with a low-powered, portable
computer, and remote into more powerful ones when needed*" mentality, I enjoy
having *one* of those power computers being my physical, main workstation
desktop.

## Workstation Goals

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
#### *Some* Gaming Ability
#### Good Budget "Base", Ability to Upgrade

## Other Considerations

#### CPUs
- Ryzen 7 1700
- Ryzen 7 2700
- Ryzen 5 2400g

#### GPUs
- RX 580
- RX 570
- Vega 11 (in the 2400g)

#### MBs
- MSI B450 Pro Gaming AC Carbon

## Final Build Selections

**- CPU: Ryzen 5 2600 -**

**- Motherboard: MSI B450 Tomahawk -**

**- RAM: G.Skill - Trident Z 32GB (2 x 16GB) DDR4-3200Mhz RAM -**

**- GPU: Sapphire 1024 4GB PULSE Radeon RX 560 -**

**- Case: Fractal Design - Meshify C Dark TG ATX Mid Tower -**

**- PSU: EVGA - SuperNOVA G4 650W 80+ Gold, fully modular ATX PSU -**

**- Storage: One of my Samsung 850 Evo SSDs (temp) -**

[pc part picker
list](https://pcpartpicker.com/user/himmelwr/saved/#view=MhbcYJ)
