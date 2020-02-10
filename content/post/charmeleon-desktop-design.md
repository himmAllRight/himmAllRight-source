+++
title  = "Designing my new Ryzen Workstation"
date   = "2018-11-26"
author = "Ryan Himmelwright"
image  = "img/posts/charmeleon-desktop-design/rht-header.jpg"
caption= "Red Hat Tower, Raleigh NC"
tags   = ["Hardware", "Linux", "Ryzen", "Homelab",]
draft  = false
Comments = "True"
+++

Over the past few years (particularly after moving to the [T470](/post/my-t470/)
as my main device), I have been anticipating what my next desktop
workstation build will look like. For a period of time, I was convinced that
I would build a [muti-socket, used xeon
build](https://www.techspot.com/review/1155-affordable-dual-xeon-pc/). Then, in 2017
AMD released their [Ryzen](https://en.wikipedia.org/wiki/Ryzen)
series CPUs...

<!--more-->

## Why a Desktop?

<a href="../../img/posts/chameleon-desktop-design/kadabra-cpu-usage.png"><img alt="Full system monitor on Laptop" src="../../img/posts/charmeleon-desktop-design/kadabra-cpu-usage.png" style="max-width: 100%;"/></a>
<div class="caption">My T470 has been a little tight on resources.</div>

[My](/post/sold-my-bonobo/) [laptops](/post/my-t470/) [have](/post/my-new-used-x230)
served the majority of my needs these last few years, but I have been feeling
a bit restricted when trying to do more demanding workloads.
While I still side with a "*use low-powered, portable computers, and remote
into more powerful ones when needed*" mentality, I enjoy having *one* of those
power computers being my physical, main workstation desktop.

## Workstation Goals

<a href="../../img/posts/chameleon-desktop-design/ryzen-logo.png"><img alt="Ryzen Logo" src="../../img/posts/charmeleon-desktop-design/ryzen-logo.png" style="max-width: 100%;"/></a>
<div class="caption">My T470 has been a little tight on resources.</div>

While building a new workstation may be fun, I have particular goals I want it
to achieve. Additionally, it seems like 98% of online build guides are for
designing *gaming* desktops... which is not exactly what I want. So, the
features I wanted in *my build*, likely deviate from much of the
*suggested* guidance found online, which tends to focus entirely on gaming
performance (more FPS). Here is the breakdown of what I was looking for:

#### More Cores


I tend to have workloads that benefit from multiple cores (and threads). For
example, I run a bunch of virtual machines, often at the same time. While my
server's 4 core Xeon handles day to day VMs just fine, it is nice to have a
workstation with several cores to spin up a virtualized cluster across. Beyond
VMs, I compile code, compress/decompress file packages, and occasionally encode
audio/video files. These are all tasks that love having many threads at their
disposal.

#### Lots of (*fast*) Ram

When running VMs, the amount of available RAM is usually more limiting than the
number of cpu cores. For example, when running 6 VM's, my server's 4-core Xeon
will typically be 15-35% utilized, whereas it's 20GB of RAM is nearly full.  If
I want more cores, I should supplement it with lots of RAM. In addition... I
use electron apps (Slack, Spotify,  etc.) and modern web browsers... so yea.... more RAM.

Being a Ryzen build, the RAM also needs to be *fast*.  More than other CPU
architectures, Ryzen CPUs actually [*run better* with faster
RAM](https://www.youtube.com/watch?v=g0SDr3EHHmY).

#### Fast Storage

This main goal of this build is for it to be a multi-tasking beast. If I am
running several VMs and a bunch of applications, utilizing a stack of *fast* RAM
to move data around... I need good *fast* storage with [MOAR
IOPs](https://www.youtube.com/watch?v=Bh_f0uof7Jw&feature=youtu.be&t=359) to
support of these operations, which will all be competing for disk access. While I
wouldn't mind having space to eventually throw in a pair 3.5" rust drives to configure as a
ZFS data pool, the goal for the initial *primary* drive of this
machine is the most IOPs I can *afford*. So, I ideally *want* a m.2 NVMe SSD,
but *need* a normal 2.5" SATA SSD at the very least.

#### *Some* Gaming Ability

While it doesn't have to be a *gaming machine*... I would like to be able to
play the *occasional* game. I don't mind playing games with lower graphic
settings on my laptops, but I *do mind* that even with the lower settings, the
CPUs nearly max out, which spikes up the temperature.
Increased graphics performance would also better support [my large
monitor](/post/new-lgud4379b/).  A discrete graphics card would be nice, ideally
an AMD one due to their recent work on improving their open source drivers.

#### Ability to Upgrade

Most importantly, I want this computer to be a solid *base* that I can upgrade
over the next several years. Upgradability is hands-down *the main* advantage
of switching to a desktop over a laptop for my main rig. I want this build
designed so that as my needs grow, I can easily max out the RAM, add storage,
or upgrade the CPU and/or GPU.

## Final Build Selections

<a href="../../img/posts/chameleon-desktop-design/charmeleon.png"><img alt="Chameleon Picture" src="../../img/posts/charmeleon-desktop-design/charmeleon.png" style="max-width: 40%; float: right;"/></a>

After spending weeks researching all the parts on the market and building
probably 50 theoretical builds, I eventually settled on [my final part list](https://pcpartpicker.com/user/himmelwr/saved/#view=MhbcYJ).

#### Name: Charmeleon


Since my last desktop build was named "Charmander", I figured "Charmeleon" was
fitting. Also, I'm then free to rename it to "Charzard" in the future if I *evolve*
the build to a next-generation Ryzen 7...

#### CPU: [Ryzen 5 2600](https://en.wikichip.org/wiki/amd/ryzen_5/2600)

<a href="../../img/posts/chameleon-desktop-design/ryzen2600.jpg"><img alt="ryzen 2600" src="../../img/posts/charmeleon-desktop-design/ryzen2600.jpg" style="max-width: 40%; float: left;"/></a>

While I initially wanted a Ryzen 2700, it pushed the build out of budget.
Coming from a 4 core/4 thread system... it's likely that I don't *need* 8
cores/16 threads right off the bat. Honestly, 4 cores/8 threads would be a
noticeable improvement from what I've been using... which is why I first
considered the Ryzen 5 2400g. I planned to start with the 2400g and upgrade to
the 2700 and a GPU once I had more cash. However, [someone on the level1tech
forums](https://forum.level1techs.com/t/finalizing-an-upgradable-ryzen-linux-build/134670/2)
reminded me that the 2600 was the same price as the 2400g, and I could get that
plus a GPU for not much more cost (considering I don't need an expensive GPU).
After thinking it over, I realized that was my best option, and should
*actually* fit my needs for quite awhile.

#### Motherboard: [MSI B450 Tomahawk](https://www.msi.com/Motherboard/B450-TOMAHAWK)

<a href="../../img/posts/chameleon-desktop-design/tomahawk.jpg"><img alt="B450 Tomahawk motherboard" src="../../img/posts/charmeleon-desktop-design/tomahawk.jpg" style="max-width: 40%; float: right;"/></a>

I had selected the MSI B450 Tomahawk after [Wendell reviewed
it](https://www.youtube.com/watch?v=lxtrHDJUMt4). [Several
other](https://www.youtube.com/watch?v=MWGzmbbimPw&feature=youtu.be&t=145) [reviews
confirmed](https://www.youtube.com/watch?v=MMJoLyrWa7E&feature=youtu.be&t=1260) that it was a solid board, especially for the price. When I was
considering the 2400g, I had to switch to the [MSI B450 Gaming Pro Carbon
AC](https://www.newegg.com/Product/Product.aspx?Item=N82E16813144188), because
the Tomahawk didn't have a display output that the integrated graphics could
properly use with [my UHD monitor](/post/new-lgud4379b/)'s resolution (I need a
display port). When I switched to the 2600, I was able to go back to the
TOMAHAWK, and funnel the cost savings towards getting my GPU.

#### GPU: [Sapphire 1024 4GB PULSE Radeon RX 560](http://www.sapphiretech.com/productdetial.asp?pid=3ECEAD87-2972-477A-A3BE-480194D9FD6E&lang=eng)

<a href="../../img/posts/chameleon-desktop-design/rx560.png"><img alt="The KDE Plasma 5 extend display GUI" src="../../img/posts/charmeleon-desktop-design/rx560.png" style="max-width: 35%; float: left;"/></a>

As discussed above, I don't need a killer GPU as I don't play very demanding
games. However, I did want something that could perform at least a *little
bit*. So, [I picked the rx560 over the
rx550](https://www.youtube.com/watch?v=237L9UGQtGk&t=422s). At first I planned
to get something like a rx580, which I still might eventually do... but
I don't think I will *need* to for a long time.

#### RAM: G.Skill - Trident Z 32GB (2 x 16GB) DDR4-3200Mhz RAM

<a href="../../img/posts/chameleon-desktop-design/ram.png"><img alt="The KDE Plasma 5 extend display GUI" src="../../img/posts/charmeleon-desktop-design/ram.png" style="max-width: 40%; float: right;"/></a>

I wanted to start out with 32GB of RAM, with the ability to easily upgrade to
64GB down the road. This meant that I needed a 2x16GB pack. Additionally, I
needed the RAM to be *fast*, but still not *overpriced*. Some research showed
that at least right now, [3200Mhz seems to be the sweet spot, especially for my
particular motherboard](https://youtu.be/lxtrHDJUMt4?t=752). I originally
picked another kit, but the reviews for it weren't great, so I switched to the
G.Skill kit for only a few dollars more, but with much better reviews. I also
briefly searched for kits with tighter timings, but they were *way* more expensive and not worth it.

#### Case: [Fractal Design - Meshify C Dark TG ATX Mid Tower](https://www.fractal-design.com/home/product/cases/meshify/meshify-c)

<a href="../../img/posts/chameleon-desktop-design/meshifyc.png"><img alt="The KDE Plasma 5 extend display GUI" src="../../img/posts/charmeleon-desktop-design/meshifyc.png" style="max-width: 30%; float: left; margin-bottom: 10px;"/></a>

I wanted a case that was sturdy, sleek, but not too flashy or expensive. During my
search, the Fractal Design cases kept catching eye. Eventually, I found the
Meshify C TG Dark, which seemed to be universally loved by reviewers. Additionally,
it appeared to have [good
thermals](https://www.fractal-design.com/home/product/cases/meshify/meshify-c),
which I liked. This was my easiest part to pick.

#### PSU: EVGA - [SuperNOVA G4 650W 80+ Gold, fully modular ATX PSU](https://www.evga.com/products/product.aspx?pn=120-g1-0650-xr)

<a href="../../img/posts/chameleon-desktop-design/psu.png"><img alt="The KDE Plasma 5 extend display GUI" src="../../img/posts/charmeleon-desktop-design/psu.png" style="max-width: 35%; float: right; margin-bottom: 10px;"/></a>

For the power supply, I wanted one that was at least gold rated, and fully
modular. So I searched for the highest rated PSUs fitting those requirements...
and SuperNova popped up all over the place. At first I picked a 550w model, but
upped to the 650w at the last minute because it was about the same price and
gives me a little more room as I upgrade.

#### Storage: One of my Samsung 850 Evo SSDs (temp)


Lastly, storage. For now I am just going to use a spare 250GB Samsung 850 Evo SSD
I had in my test laptop. I plan to eventually upgrade to a [500GB Samsung 970 Evo
m.2 NVMe
drive](https://www.samsung.com/semiconductor/minisite/ssd/product/consumer/970evo/),
but the 850 will work for now.

## Conclusion

So after months of planing and research, my desktop parts have all been
ordered. Hopefully, it meets the goals I set out to solve, and I will be able
to upgrade it over the next few years
