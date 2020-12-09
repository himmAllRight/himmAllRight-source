+++
title   = "Selecting Charmeleon's Upgrades"
date    = "2020-12-14"
author  = "Ryan Himmelwright"
image   = "img/posts/selecting-charmeleon-upgrades/cpu_pins_header.jpeg"
caption = "Durham, NC"
tags    = ["hardware", "linux", "ryzen", "homelab", "vfio"]
draft   = "True"
Comments = "True"
+++

After years of planning and months of keeping my eye on prices while
conducting deep research... I have upgrade a bunch of components in
Charmeleon, my Linux workstation. What started as a cpu + ram upgrade
eventually also included a new motherboard and secondary gpu. Here is what I
selected and why.

<!--more-->

## Background

<a href="../../img/posts/selecting-charmeleon-upgrades/pre_upgrades.jpeg"><img alt="Inside charmeleon before upgrades" src="../../img/posts/selecting-charmeleon-upgrades/pre_upgrades.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Charmeleon Internals before upgrades</div>

Over two years ago, I [build and designed
charmeleon](post/charmeleon-desktop-design/), my linux desktop computer. In
that post, I explain how I did eventually want to upgrade charmeleon over
time. Since the initial build, I have only upgraded a few single items: a new
m.2 ssd and a [gpu upgrade](/post/rx580-upgrade/) when my origonal one
Stopped working several months ago. The next 'single part' I wanted to upgrade was some more RAM... but, as I started down that path, things became a bit more... complicated...

## Part Selection

### RAM

<a href="../../img/posts/selecting-charmeleon-upgrades/ripjaws_ram.jpeg"><img alt="Two 32GB sticks of DDR4 3200 ram in" src="../../img/posts/selecting-charmeleon-upgrades/ripjaws_ram.jpeg" style="max-width:
100%;"/></a>
<div class="caption">RAM upgrade: 2x32 GB of 3200Mhz DDR4, CL 16</div>

* One of the easy upgrades I prepped for was RAM. My motherboard had 4 slots, with a max capacity of 64GB, and I populated it with 2x16gb sticks so I could easily double it down the road when RAM was cheaper.
* But... Ryzen 3000 made it a bit complicated. All of a sudden, those cpus could support 128gb, even in my MB...
* So I wondered if I should fill those blank spaces with the new max size
* The problem was, RAM suddenly stopped being a 'simple' whenever upgrade. Not only because the price double, but if I did want to get new max dimm sizes, I couldn't use it until I had a 3000+ series cpu

### CPU

<a href="../../img/posts/selecting-charmeleon-upgrades/ryzen9_box.jpeg"><img alt="Ryzen 9 3900x Box" src="../../img/posts/selecting-charmeleon-upgrades/ryzen9_box.jpeg" style="max-width:
100%;"/></a>
<div class="caption">CPU upgrade: Ryen 9 3900x, 12 core/24 thread cpu</div>

* the *origonal* plan when I built charmeleon was to get the 2600 for a but until I could upgrade to an 8 core from the same 2000 series or even a rumored cpu with even more cores
* I made sure my motherboard had good VRMs for it's cost to support a future higher core upgrade.
* Months later, after all the 3000 cpus launched, I was rather set on getting a 3900x.
* However I knew AMD was going to be releasing the '4000' (lol) cpus in the Fall, so I figured I'd wait until they were released and either get a new one or discount old one.
* 5000 was released, and I thought the 5900x would be perfect.
* But then it was impossible to buy them, and I didn't feel like waiting even longer, and I don't actually *need* the increased performance. Particularly the gaming performance increases... I'm rocking an rx580 and am clearly gpu bottlenecked 😆
* So I started looking at older crazier options, like the 3950x
    * It was awesome, and honestly I'd still love to have one.
    * However, even if I *could* get it on sale... it would still cost a ton and I couldn't justify the price difference. 16 cores is amazing, but 12 should easily still fit my needs
    * The money *saved* on the price difference could then be used to get my ram upgrade (the thing that started everything) so I wouldn't have to wait a few months to save for it.
    * So, I looked at the 3900x and wondered if it would go on sale.
    * It did intermittently, but it seemed like it might actually start to have shortage issues with people jumping to it after not being able to get a 5900x. The next time I saw it go on sale I grabbed it right before they sold out again. It's not the *cheapest* it's ever been, but it's not far off either. And it was *much* cheaper than it remained for the remainder of the holiday shopping week

### CPU Cooler

<a href="../../img/posts/selecting-charmeleon-upgrades/noctua_box.jpeg"><img alt="Noctua nh-u14s box" src="../../img/posts/selecting-charmeleon-upgrades/noctua_box.jpeg" style="max-width: 100%;"/></a>
<div class="caption">CPU Cooler upgrade: Noctua NH-U14s</div>

* I always knew I'd get a noctua cooler, although I did second guess if I wanted an AIO for like an hour one day.
* I actually wanted to get one when I got my noctual fans over the summer, but figured if I was going to swap the cpu *eventually,* I might as well wait till then to prevent the hassel of repasting and everything.
* I switched the model once or twice being confused about compatibility, I didn't want the massive one and found it wouldn't actually cool much more than the single heat sink ones. I wanted the 140mm fan one because I much prefer their lower sounding woosh. After I confirmed it should fit in the Meshify C and with my ram (and anticipated ram) knew what I'd get.

### Motherboard

<a href="../../img/posts/selecting-charmeleon-upgrades/mb_box.jpeg"><img alt="x570 Aorus Elite Wifi Box" src="../../img/posts/selecting-charmeleon-upgrades/mb_box.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Motherboard upgrade: x570 Aorus Elite Wifi</div>

* I never intended to get a new motherboard. In fact, I stated previously that one of the reasons I got the b450 tomahawk was that it's VRMs suposidly should be able to support a higher core ryzen upgrade.
* However, when I was looking at getting a 5000s cpu, I knew my MB wouldn't get the bios upgrade it needed until January maybe... and it might not be reversable which I didn't like
* So I started looking into x570 boards.
    * I liked their gen4 support
    * I really liked their iommu groupings and wanted to dabble with vfio some more
    * There were some other features I realized I would like to have on my MB, like a second m.2 (So I could get a larger one but not loose the old one), more sata ports (2 of mine were disabled because I used the m.2), wifi (mostly for bluetooth), and just more pcie lanes
    * I realized x570 fit my need a bit better, even when compared to b550 (which I think most people should probably get). Esp if I was doing a big upgrade with more powerful components
* Looked at mother boards for months. Eventually settled on one of the Aorus ones
    * The Master was rated REALLY well, but was very expensive
    * I went back and forth between the elite wifi, pro, ultra... and sometimes still master for weeks
    * Eventually when I started making purchases and the elite wifi went on sale though, I decided to grab it. It had everything I needed, and most of the upgraded features on the other boards I either wouldn't use or were just small nice to haves

### GPU

<a href="../../img/posts/selecting-charmeleon-upgrades/gpu_box.jpeg"><img alt="rx550 box" src="../../img/posts/selecting-charmeleon-upgrades/gpu_box.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Second GPU: RX 550 4GB</div>

* With a MB that supported iommu I wanted to get a smaller gpu that I could use for host graphics if I got VFIO working.
* I heard that both the rx550 and 1030gt were good, and were sub $100
    * I wasn't thrilled about using a nvida cpu, particularly the one that would be the linux host, but I loved how small it was
    * However the 550 seemed to have slightly more power, was amd, and well rated.
    * I had actually considered the 550 when I first built charmeleon, but ended up picking the rx550.
    * This time, I picked the rx550 to pair with my rx580.
        * I had actually read several gpu passthrough guides using this exact pairing so I guessed it was a safe bet.

## Conclusion

<a href="../../img/posts/selecting-charmeleon-upgrades/post_upgrades.jpeg"><img alt="Inside charmeleon after upgrades" src="../../img/posts/selecting-charmeleon-upgrades/post_upgrades.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Charmeleon Internals after upgrades</div>
