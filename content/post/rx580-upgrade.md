+++
title  = "Rx-580 Upgrade"
date   = "2020-05-27"
author = "Ryan Himmelwright"
image  = "img/posts/rx580-upgrade/holding-rx580.jpeg"
caption = "My new rx580"
tags   = ["linux","hardware", "homelab", "gpu",]
draft  = "True"
Comments = "True"
+++

At the start of the year, I noticed that my desktop wouldn't connect to my
display. Using it mostly as a server, and thus through `ssh`, I didn't really
notice and assumed it was a mis-plugged cable or a config issue. A few months
later when I started to game a bit more (and wanted to use my desktop as a
gaming machine in addition to my main computer server), I realized it was an
*actual* issue. Long story short, my desktop now has an rx580 instead of it's
old rx560.

<!--more-->

## My Old Card - RX560 Recap

So why did I select the rx560 in the first place? What did I like about it?

#### I wanted an AMD GPU
<center>
<a href="/img/posts/rx580-upgrade/amd_radeon_logo.png">
<img alt="rx580 price history" src="/img/posts/rx580-upgrade/amd_radeon_logo.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
</center>

When I [designed and built my desktop](/post/charmeleon-desktop-design/), I
knew I wanted to get and AMD GPU because I had heard the state of their open
source drivers was good, and would allow me to skip all the headaches I've had
over the years messing around with the proprietary Nvidia drivers.

I remain very pleased with this decision. With the AMD GPU, I simply install my
linux distro of choice, install steam, and I'm playing games. No hassle. :w

#### I needed a card to handle *modest* gaming
In the post about my desktop, I stated that while I wasn't a big pc gamer, but
did enjoy the *occasional* game. I play some games on consoles (especially ones
I play with my wife), but PC gaming is still my favorite. However, I don't need
all the graphics on ultra, and I tend to not play the newest games.

The rx560 was a perfect little card that give me *enough* performance to play
some games, without costing too much. GPUs were still coming down from steep
prices due to crypto mining at the time, and saving some money on the GPU
allowed me to buy more RAM, while remaining under budget (which was needed more
for my use case).


#### I planned to eventually upgrade

One of the reasons I wanted to build a desktop computer again was for
the ability to easily upgrade it over time. I build I designed seemed like it
had enough power to fit all of my needs, but I set it up so that if part of it
lacked enough performance over time, I could upgrade it.

<center>
<a href="/img/posts/rx580-upgrade/side-by-side-photo.jpeg">
<img alt="The rx560 and 580 side-by-side" src="/img/posts/rx580-upgrade/side-by-side-photo.jpeg" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">The rx560 (bottom) next to my new rx580 (top)</div>
</center>

I knew one of the components I might *eventually* want to upgrade would be the
GPU. I knew that the rx560 should last me for awhile, but if I started playing
more games, I could easily get a better one, and hopefully prices would be
lower. I figured I could always upgrade to an rx580, or an even newer card if
needed.

### Issues
#### Debugging
At the beggining of the year, I noticed that my desktop wouldn't connect to my
monitor. However, when I `ssh`ed into it, everything worked as normal, and all
of my VMs and containers spun up like there was nothing wrong. I did some more
testing and confirmed I couldn't get a signal on *any* monitor in the house,
using a large assortment of cables.

Investigating further, I noticed in the logs during boot-up the `$DISPLAY`
trying to connect via all the various inputs (DVI, HDMI, etc), but eventually
failing stating that there was `No Display Attached`, even when it was plugged
in. I opened up the case, ensured everything was connected properly, tried
different cables, and even attempted to boot into live cds and os installs.
However, the system wouldn't even display the BIOS when it started.

#### The Possible 'Solution'
I eventually narrowed the problem being caused by issues with the GPU, despite
it showing up fine in my pci devices. If it wasn't the GPU, it was likely the
motherboard.... So I figured the next best (and easier) step was to swap in
another card and see if it worked. Not having a spare graphics card on hand,
and not being able to borrow one easily due to COVID lockdown, my option was to
order one.

Fixing the display issues on my workstation was an *urgent* issue. In fact,
because I wasn't playing any PC games and I already exclusively worked on the
desktop via `ssh` from laptops, I likely didn't notice the issue for weeks.
However, without the ability to connect to a display I couldn't easily
re-install or debug my system if something went wrong. This was compounded by
the fact that I was running [Fedora
Silverblue](https://silverblue.fedoraproject.org), and I needed to hold my
breath and reboot every time I wanted to update my packages. Lastly, I didn't
know what availability or shipping times would be given the pandemic. So, I
decided it was best to just order a new card right away, rather than wait until
the problem *did become* urgent.

## My New Card: The RX-580

After some brief researching, I decided on the rx580. I also considered the 570
and 590, as well as glanced at some of the newer AMD cards. The truth is, my
rx560 honestly worked fine for what I needed, but if I was getting a new card,
a slight spec bump would be nice. The 580 seemed to provide great performance
for a very reasonable price.

So far, my experience seems to confirm that. I am able to play all of my games
(mostly Divinity Original Sin II, Minecraft, City Skylines, right now)
generally above 60 fps at mostly high settings. Additionally, because the card
isn't being *too* taxed during gameplay, it doesn't seem to be heating up too
badly... which I also appreciate.

<center>
<a href="/img/posts/rx580-upgrade/rx580-price-history.png">
<img alt="rx580 price history" src="/img/posts/rx580-upgrade/rx580-price-history.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">rx580 price history</div>
</center>

Lastly, the card has come down in price since I built my desktop. I purchased
the rx580 for only slightly more than I originally paid for the rx560, and over
$100 cheaper than what it cost when I built the desktop. For what I need, the
price and performance are perfect.

## Conclusion

I'm loving it so far. It's handling all the games I play just fine and seems to
even doing it cooler for most of them.


