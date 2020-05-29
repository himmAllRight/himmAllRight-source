+++
title  = "Rx-580 Upgrade"
date   = "2020-05-28"
author = "Ryan Himmelwright"
image  = "img/posts/rx580-upgrade/holding-rx580.jpeg"
tags   = ["linux","hardware", "homelab", "gpu",]
draft  = "False"
Comments = "True"
+++

Earlier this year, I noticed that my desktop seemingly did not connect to my
monitor. I used the computer mostly as a server, remoting in via `ssh`, and
didn't think much of it.  I assumed it was either a mis-plugged cable or a
configuration issue. A few months later, I started to game a bit more and
wanted to use my desktop as a gaming machine again. That is when I realized...
it was an *actual* issue. Long story short, my desktop now has an rx580 instead
of it's old rx560.

<!--more-->

## My Old Card - The rx560

Before diving into the issues, lets recap. Why did I select the rx560 in the
first place? What did I like about it?

#### I wanted an AMD GPU
<center>
<a href="/img/posts/rx580-upgrade/amd_radeon_logo.png">
<img alt="rx580 price history" src="/img/posts/rx580-upgrade/amd_radeon_logo.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
</center>

When I [designed and built my desktop](/post/charmeleon-desktop-design/), I
knew I wanted to get an AMD GPU because their open source drivers were great,
and would allow me to skip all the headaches I've had over the years messing
around with the proprietary Nvidia drivers. I remain *very* pleased with that
decision, and have had zero issues getting games up and running. No hassle,
period.

#### I needed a card to handle *modest* gaming
In the post about my desktop, I stated that while I wasn't a big pc gamer, I
did enjoy the *occasional* game. I play many games on consoles, especially the
ones I play with my wife, but desktop gaming is still my favorite. That said, I
don't need all my graphics settings tuned to ultra, and I tend to not play the
*newest* games.

The rx560 was a perfect little card that give me *enough* performance to play
most games, without costing too much. GPUs were still coming down from steep
prices due to crypto mining at the time, and saving some money on the GPU
allowed me to buy more RAM (which I needed more), while remaining under budget.


#### I planned to eventually upgrade

<center>
<a href="/img/posts/rx580-upgrade/side-by-side-photo.jpeg">
<img alt="The rx560 and 580 side-by-side" src="/img/posts/rx580-upgrade/side-by-side-photo.jpeg" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">The rx560 (bottom) next to my new rx580 (top)</div>
</center>

One of the reasons I wanted to build a desktop computer again was for the
ability to upgrade it down the road. The build I designed had enough power
to fit all of my needs, but I configured it so that if any part lacked enough
performance over time, I could easily upgrade it.

I knew one of the components I might eventually want to upgrade would be the
GPU. I figured that the rx560 should last me awhile, but if I started playing
more games, I could easily get a better one, and hopefully prices would be
lower. I could always upgrade to an rx580, or an even newer card if needed.

### Issues

#### Debugging

Okay, back to the problem. As I said before, my desktop wouldn't connect to my
monitor. When I `ssh`'ed into it, everything worked as normal, and all of my
VMs and containers spun up without issue, as if there was nothing wrong.  I ran
commands like `lspci | grep 'VGA'` and `neofetch`, and they still correctly
detected and listed the rx560, confirming the system *knew* the card was there.
I did some more testing and confirmed that I couldn't get a signal on *any*
monitor in the house, using a large assortment of cables.

<center>
<a href="/img/posts/rx580-upgrade/no_display.jpeg">
<img alt="Displays would not connect" src="/img/posts/rx580-upgrade/no_display.jpeg" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">No display would 'connect', even when plugged in</div>
</center>

I attempted to boot into live cds and other os installs, but the system
wouldn't even display the BIOS when starting.  Investigating further, I saw in
the logs that the `$DISPLAY` was trying to connect via all the various inputs
(DVI, HDMI, etc) during bootup, but would eventually fail stating that there
was `No Display Attached`, even when it was plugged in. I opened up the case,
ensured everything was connected properly, and even tried different cables.
Nothing.

#### The Possible 'Solution'
I eventually narrowed down that the problem was being caused by issues with the
GPU, despite it showing up fine in my pci devices. If it wasn't the GPU, it was
likely the motherboard.... So I figured the next best (and easier) step was to
swap in another card and see if it worked. Not having a spare graphics card on
hand, and not being able to borrow one due to COVID-19 lockdown, my only option
was to order one.

Fixing the display issues on my workstation was not an *urgent* issue.
However, without the ability to connect to a display I couldn't easily
re-install or debug my system if something went wrong. This was compounded by
the fact that I was running [Fedora
Silverblue](https://silverblue.fedoraproject.org), and needed to reboot every
time I wanted to update my packages, never quite sure if I would be able to
`ssh` back in when it was done. Lastly, I didn't know what availability or
shipping times would be, given the pandemic. So, I decided it was best to just
order a new card now, rather than wait until the problem *did* become urgent.

## My New Card: The RX-580

<center>
<a href="/img/posts/rx580-upgrade/rx580_box.jpeg">
<img alt="The rx560 box arrived a few days later" src="/img/posts/rx580-upgrade/rx580_box.jpeg" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">The rx580 box arrived a few days after ordering</div>
</center>

After some brief researching, I decided on the rx580. I also considered the 570
and 590, as well as glanced at some of the newer AMD cards. The truth is, my
rx560 worked fine for what I needed. *If* I was getting a new card
though, a small spec bump would be nice. The 580 seemed to provide more than
enough performance.

So far, my experience confirms this. I am able to play my games (mostly
Divinity Original Sin II, Minecraft, and City Skylines, right now) generally
above 60 fps, and at mostly high or better settings. Additionally, because the
card isn't being *too* taxed during gameplay, it doesn't seem to be heating up
too badly...  which I also appreciate.

<center>
<a href="/img/posts/rx580-upgrade/rx580-price-history.png">
<img alt="rx580 price history" src="/img/posts/rx580-upgrade/rx580-price-history.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">rx580 price history</div>
</center>

Lastly, the card dropped in price since I built my desktop. I purchased the
rx580 for only a little bit more than I originally paid for the rx560, and over
$100 cheaper than what it cost when I built the desktop. For what I need, the
price and performance are perfect.

## Conclusion

So far, I'm loving it. The rx580 does everything that I need it to and honestly
doesn't give me any problems. Once again, I was able to plug in the card, boot
up the computer, open Steam, and start playing my games. No additional drivers,
no weird configuration, no bloatware. All on Linux. I am *very* happy with the
purchase, and it has once again reminded me why I truly do love having a
desktop/workstation under my desk, even if it is used as a server *most* of the
time.
