+++
title   = "Selecting Charmeleon's Upgrades"
date    = "2020-12-28"
author  = "Ryan Himmelwright"
image   = "img/posts/selecting-charmeleon-upgrades/mb_header.jpeg"
caption = "Durham, NC"
tags    = ["hardware", "linux", "ryzen", "homelab", "vfio"]
draft   = "False"
Comments = "True"
+++

After months of planning and price tracking, I have finished upgrading
several major components in my Linux workstation. What started
as a planned cpu and ram upgrade, eventually ballooned to also include a new
motherboard and a secondary gpu. Let me explain...
<!--more-->

## Background

<a href="../../img/posts/selecting-charmeleon-upgrades/pre_upgrades.jpeg"><img alt="Inside charmeleon before upgrades" src="../../img/posts/selecting-charmeleon-upgrades/pre_upgrades.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Charmeleon Internals before the upgrades</div>

Over two years ago, I [built and designed
charmeleon](post/charmeleon-desktop-design/), my Linux desktop computer. In
that post, I explained how I wanted to upgrade charmeleon over time, and
designed it with that in mind. Since the initial build, I have only made a
few minor upgrades: I added a m.2 nvme ssd and [upgraded the
gpu](/post/rx580-upgrade/) after the original one stopped working. The next
upgrade I wanted to make was adding more RAM. As I started down that path,
things became a bit more... complicated...

## Part Selection

### RAM

<a href="../../img/posts/selecting-charmeleon-upgrades/ripjaws_ram.jpeg"><img alt="Two 32GB sticks of DDR4 3200 ram in" src="../../img/posts/selecting-charmeleon-upgrades/ripjaws_ram.jpeg" style="max-width:
100%;"/></a>
<div class="caption">RAM upgrade: 2x32 GB of 3200Mhz DDR4, CL 16</div>

An easy upgrade I prepared for during the inital build was RAM. My
motherboard had 4 slots with a max capacity of 64GB. So, I made sure to
populate it with 2x16gb sticks instead of 4x8gb ones, so the capacity could
be effortlessly doubled when RAM became cheaper. But, the release of Ryzen
3000 cpus changed things. Overnight, a Ryzen 3000 serries processor paired
with my motherboard, could support up to 128gb of RAM.

This made me wonder if I should instead fill those blank spaces with the
*new* max dimm size sticks. The only problem was, if I wanted to upgrade RAM
to the new max size, I needed to also upgrade to a CPU to that supported it.
Oh, and also buy twice the capacity of RAM.

*Spoiler alert*: I did buy a new cpu so I could max the RAM. Eventually
I settled on a Ripjaws V 2x32GB 3200Mhz kit with 16-18-18-38 timings. There
wasn't a 2x32gb kit that matched the model of my original RAM, and but this
one had all the same timings, while still being cheaper than the other
alternatives. A total of 96GB of RAM overkill for most uses (arguably, even
my own). However, I tend to run large VM deployments and often use my `/tmp/`
dir as a large working folder, so the extra overhead is nice.

**TLDR:** I always planned to expand my RAM. Ryzen 3000 allowed an even higher
max RAM capacity with my MB, but I would have to also upgrade my CPU. I upgraded both, 
and now have 96GB of RAM.

### CPU

<a href="../../img/posts/selecting-charmeleon-upgrades/ryzen9_box.jpeg"><img alt="Ryzen 9 3900x Box" src="../../img/posts/selecting-charmeleon-upgrades/ryzen9_box.jpeg" style="max-width:
100%;"/></a>
<div class="caption">CPU upgrade: Ryen 9 3900x, 12 core/24 thread cpu</div>

My *origonal* plan when I built charmeleon was to get the 2600, and later
upgrade to a 8 core 2700x or even a rumored 3000 cpu
with potentially even more cores. I made sure my motherboard had good VRMs
for the cost so it could support a future upgrade with more cores.

Months later the 3000 cpus launched, I was set on getting a 3900x.
However, I didn't *need* a new cpu and I knew AMD was going to be releasing
the '4000' (lol) cpus in the Fall. I figured I would wait until they were
released and either get a new one, or a discountted 3000 one.

When the 5000 series cpus were released, and I thought the 5900x would be
perfect. But, like ever other tech release in 2020, it was impossible to buy
one. I didn't feel like waiting even longer, and I don't actually *need* the
increased performance. The new ryzen cpus performance increases are patically
seen in gamming... I'm rocking an rx580 and am clearly gpu bottlenecked
anyway 😆

With the 5900x not available anytime soon, I started being tempted at some
crazier options... like the 3950x. The 3950x is an amazing cpu, and honestly
I'd still love to have one. However, even if I *could* get it on sale... I
knew it would still cost a ton and I couldn't justify the price difference. A
16 core cpu is amazing, but 12 should still easily fit my needs. The money
*"saved"* on the price difference could then be used to get the bigger ram
upgrade so I wouldn't have to wait a few months to save for it.

So, I looked back at the 3900x and wondered if it would go on sale. It did
intermittently, but it seemed like it might actually start to have shortage
issues with people jumping to *it* after not being able to get a 5900x. The
next time I saw it go on sale I grabbed it right before they sold out again.
I didn't get it for the cheapest it's *ever* been, but the sale was quite
close to the all time low. And it was *much* cheaper than what it has
remained at ever since.

**TLDR:** I planned to eventually upgrade to a higher core count CPU. After
waiting, I wanted a 5900x, but you can't buy them. After being tempted by the
3950x, I purchased the more reasonably priced 3900x on sale.

### CPU Cooler

<a href="../../img/posts/selecting-charmeleon-upgrades/noctua_box.jpeg"><img alt="Noctua nh-u14s box" src="../../img/posts/selecting-charmeleon-upgrades/noctua_box.jpeg" style="max-width: 100%;"/></a>
<div class="caption">CPU Cooler upgrade: Noctua NH-U14s</div>

Over the summer I upgraded all the fans in my case to Noctua ones and love
them. At the time, I wanted to also get a new cpu cooler to match, but with plans
to upgrade my cpu soon, I figured I would wait and order both at the same time, so
I wouldn't have to go through the hassel of repasting the CPU twice. 

I switched what specific model I wanted once or twice, after being confused about
compatibility. I didn't want the massive NH-D15, and learned that it wouldn't actually
cool much more than the single heat sink ones. I did want a cooler that used a 140mm fan instead of a 120mm one, because I much prefer their lower sounding woosh. After I confirmed it should
fit in the Meshify C and with my RAM, I selected the NH-U14s.

**TLDR:** I wanted a new CPU Cooler with a 140mm fan. I love Noctua.

### Motherboard

<a href="../../img/posts/selecting-charmeleon-upgrades/mb_box.jpeg"><img alt="x570 Aorus Elite Wifi Box" src="../../img/posts/selecting-charmeleon-upgrades/mb_box.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Motherboard upgrade: x570 Aorus Elite Wifi</div>

Unlike the CPU and RAM, I never intended to get a new motherboard when
building Charmeleon. However, when I was looking at getting a 5000s cpu, I
knew my B450 thomahawk wouldn't get the required bios upgrade until January... maybe.
I also knew the upgrade might not be reversable which I didn't like, so I started looking at B550 and x570 boards.

I realized x570 fit my need a bit better when compared to my b450, and even
the new b550 (which I think most people should probably get). The x570 was a
good match considering the other upgrades I was making. Particular features that made me want to upgrade my b450 to a x570 motherboard were:

* Gen4 PCIe support
* Better iommu groupings for VFIO passthrough
* Often had a second m.2 
* More *usable* sata ports (2 of mine were disabled because they shared lanes with my m.2), 
* wifi (mostly for bluetooth)
* In general, more pcie lanes

Looked at mother boards for months. Eventually decided I wanted one of the
Gigabyte Aorus ones. The Aorus Master seemed to be one of the defacto
reccomened board for VFIO builds, but was very expensive. Much of what made
it good however seemed to still be present in the cheaper models. In
particular, the Aorus motherboards had good iommu groupings and support,
*and* a bios feature that allows you to select which x16 slot to use for the
primary gpu. This makes it easier to boot into a secondary gpu, saving the
bigger one to pass through to VMs.

I went back and forth trying to decide between the elite wifi, pro, ultra...
and sometimes still master for weeks. Eventually when I started making
purchases, the elite wifi went on sale and I decided to grab it. It had
everything I needed, and most of the upgraded features on the other boards I
either wouldn't use or were just small nice to haves.

**TLDR:** Looking at Ryzen 5000 CPUs had me looking at newer motherboards.
Even after dropping back down to a 3000 CPU, I still wanted a motherboard
upgrade for better VFIO support and expandability.

### GPU

<a href="../../img/posts/selecting-charmeleon-upgrades/gpu_box.jpeg"><img alt="rx550 box" src="../../img/posts/selecting-charmeleon-upgrades/gpu_box.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Second GPU: RX 550 4GB</div>

With a MB that better supported iommu, I wanted to get a smaller gpu that I
could use for host machine graphics. I read that rx550 and 1030gt were both
good, sub $100 gpus often used for the host.
 
I wasn't thrilled about using a nvida gpu on a linux host, but I loved how
small it was (although that could translate more fan moise). In comparison,
the 550 seemed to be slightly more powerful, was amd, and well rated. In
fact, I had read several gpu passthrough guides using the rx550 and passing
through a rx580 (my current gpu). I purchased the 550.

**TLDR:** I wanted an easier time with VFIO GPU passthrough. Having a second
card for the host or a second VM makes this easier. The rx550 is a common card
for this use.

## Conclusion

<a href="../../img/posts/selecting-charmeleon-upgrades/post_upgrades.jpeg"><img alt="Inside charmeleon after upgrades" src="../../img/posts/selecting-charmeleon-upgrades/post_upgrades.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Charmeleon Internals after upgrades</div>

Overall, I am extremely happy with my selections. It's sureal how powrful a
machien can be built at a modest budget these days. With the upgrades,
Charmelon's specs stand at:

```
Ryzen 9 3900x [3.8 GHz (4.6GHz Boost), 12 Cores, 24 Threads)
Noctua NH-U14s CPU Cooler
Aorus Elite Wifi x570 Motherboard
96 GB (2x16GB, 2x32GB) DDR4-3200 Mhz, CL 16 RAM
Sapphire Radeon Pulse RX 580 8GB GPU
Sapphire Radeon Pulse RX 550 4GB GPU
500 GB Samsung 970 EVO NVME SSD
500 GB Samsung 850 EVO SATA SSD
120 GB Kingston SSD (Dedicated windows VM)
EVGA SuperNOVA G4 650w 80+ Gold, fully modular PSU
Fractal Design Meshify C Dark TG ATX Mid Tower Case
2 x Noctua NF-A14 PWM 140mm Fans
1 x Noctua NF-F12 PWM 120mm Fan
Fedora 33 (KDE Plasma)
```

Not only have these changes drastically improved the performance of my
workstation, but they have allowed me to run virtual machines at the next
level. When passing hardware directly to my VMs, I cannot tell that the
computer I'm sitting at is virtualized. I have been living inside Vms, and I
love it.
