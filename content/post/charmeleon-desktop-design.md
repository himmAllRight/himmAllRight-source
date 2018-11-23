+++
title  = "Designing my new Ryzen Workstation"
date   = "2018-11-23"
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

After spending weeks researching all the parts on the market and building
probably 50 part builds, I eventually settled on [my final part list](https://pcpartpicker.com/user/himmelwr/saved/#view=MhbcYJ).

#### Name: Charmeleon

<a href="../../img/posts/chameleon-desktop-design/charmeleon.png"><img alt="The KDE Plasma 5 extend display GUI" src="../../img/posts/charmeleon-desktop-design/charmeleon.png" style="max-width: 50%; float: right;"/></a>

Since my last desktop build was named "Charmander", I figured "Charmeleon" was
fitting. Also, I', free to rename it to "Charzard" in the future if I *evolve*
the build to a future Ryzen 7...

#### CPU: [Ryzen 5 2600](https://www.amd.com/en/products/cpu/amd-ryzen-5-2600)

While I ideally wanted a Ryzen 2700, it made my build out of budget... and
coming from 4 core/4 thread systems... it's likely that I don't *need* 8
cores/16 threads yet. Honestly, 4 cores/8 threads would be a noticeable
improvement from what I've been using... which is why I originally
considered the Ryzen 5 2400g, which I planned to start with and upgrade to the
2700 + a GPU once I had the spare money. However, [someone on the level1tech
forums](https://forum.level1techs.com/t/finalizing-an-upgradable-ryzen-linux-build/134670/2)
reminded me that the 2600 was the same price as the 2400g, and I could get that
plus a GPU for not much more cost. After thinking it over, I realized that was
my best option, and would *actually* fit my needs for awhile.

#### Motherboard: [MSI B450 Tomahawk](https://www.msi.com/Motherboard/B450-TOMAHAWK)

I had selected the MSI B450 Tomahawk after watching a [review of it by
Wendell](https://www.youtube.com/watch?v=lxtrHDJUMt4). Several other reviews
stated that it was a solid board, especially for it's price. When I considered
the 2400g however, I had to switch to looking at the [MSI B450 Gaming Pro
Carbon AC](https://www.newegg.com/Product/Product.aspx?Item=N82E16813144188)
(what a terrible name), because the Tomahawk didn't have a display output
that the integrated graphics could properly use with [my UHD
monitor](../new-lgud4379b/)'s resolution (I basically need display port). When
I switched to the 2600, I was able to go back to the TOMAHAWK, and funnel the
cost savings towards getting my GPU.

#### GPU: [Sapphire 1024 4GB PULSE Radeon RX 560](http://www.sapphiretech.com/productdetial.asp?pid=3ECEAD87-2972-477A-A3BE-480194D9FD6E&lang=eng)

As discussed above, I don't really need a killer GPU as I don't play very
demanding games. However, I did want something that could perform at least a
*little bit*, which is [why I picked the rx560 over the
rx550](https://www.youtube.com/watch?v=237L9UGQtGk&t=422s). I originally
planend to upgrade to something like a rx580 which I still might eventually
do.. but I don't think I will *need* to for a long time.

#### RAM: G.Skill - Trident Z 32GB (2 x 16GB) DDR4-3200Mhz RAM

I wanted to start out with 32GB of RAM, with the ability to easily upgrade to
64GB down the road, which meant I needed to get a 2x16GB pack. Additionally, I
needed the RAM to be *fast*, but still not *overpriced*. Some research showed
that at least right now, [3200Mhz seems to be the sweet spot, especially for my
particular motherboard](https://youtu.be/lxtrHDJUMt4?t=752). I originally
picked another kit, but the reviews for it weren't great, so I switched to the
G.Skill one which was only a few dollars more with much better reviews. I also
searched for kits with tighter timings, but they were *way* more expensive, so
that search didn't last long.

#### Case: [Fractal Design - Meshify C Dark TG ATX Mid Tower](https://www.fractal-design.com/home/product/cases/meshify/meshify-c)

I wanted a case that was sturdy, sleek, but not too flashy or expensive. During my
search, the Fractal Design cases kept catching eye. Eventually, I found the
Meshify C TG, which seemed to be universally loved by reviewers. Additionally,
it appeared to have [good
thermals](https://www.fractal-design.com/home/product/cases/meshify/meshify-c),
which I like. This was my easiest part to pick.

#### PSU: EVGA - [SuperNOVA G4 650W 80+ Gold, fully modular ATX PSU](https://www.evga.com/products/product.aspx?pn=120-g1-0650-xr)

For the power supply, I wanted one that was at least gold rated, and fully
modular. So I searched for the highest rated PSUs fitting those requirements...
and SuperNova popped up all over the place. At first I picked a 550w model, but
upped to the 650w at the last minute because it was about the same price and
gives me a little more room as I upgrade.

#### Storage: One of my Samsung 850 Evo SSDs (temp)

Lastly, storage. For now I am just going to use my spare 250GB Samsung Evo SSD
I have for my test laptop. I plan to eventually upgrade to a [500GB Samsung Evo
m.2 NVMe
drive](https://www.samsung.com/semiconductor/minisite/ssd/product/consumer/970evo/),
but the 850 will work for now.

## Conclusion

So after months of planing and research, I have finally picked and ordered all
the parts for my desktop. Hopefully, it meets the goals I set out to solve, and
I will be able to upgrade it over the next few years.
