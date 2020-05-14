+++
title  = "Rx-580 Upgrade"
date   = "2020-05-14"
author = "Ryan Himmelwright"
image  = "img/posts/rx580-upgrade/holding-rx580.jpeg"
tags   = ["linux","hardware", "homelab"]
draft  = "False"
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

## Old Card - RX560
### Why I got it
#### I wanted an AMD GPU
When I [designed and built my desktop](/post/charmeleon-desktop-design/), I
knew I wanted to get and AMD GPU because I had heard the state of their open
source drivers was good, and would allow me to skip all the headaches I've had
over the years messing around with the proprietary Nvidia drivers.

I remain very pleased with this decision. With the AMD GPU, I simply install my
linux distro of choice, install steam, and I'm playing games. No hassle. :w

### Why the 560?
#### Needed a card to handle modest gaming
stated that while I wasn't a big pc gamer, I did enjoy the *occasional* game.


	- Open source drivers much better
	- Had issues with Nvidia on my Bonobo and work laptop with nvidia GPUs
	- I dont the the absolute best GPU performance

#### Plans to eventually upgrade
- AMD cards were still just starting to come down in price from crypto miners
-
	- Possibly to the rx580

### Issues with RX560
- no displays when attached
- Computer worked fine to ssh in and my VMs always started up fine
- I wan't really able to re-install a distro if I had to (or most distros at least) without a display, and was worried something might break and I'd be stuck without my main VM host...

## The RX-580
- Capable of what I need it for
	- The 560 worked fine for me, but might of heated up a bit because it was startign to be pushed
	- The 580 should be able to handle all the games I play perfectly
    - Wasn't too different that the 570 in price, so worth the bump up
- Prices have gone down a bit on it since I built Charmeleon
	- When I build it prices had just started to come down from the bitcoin mining
	- Plust it's an older card now


## Conclusion

I'm loving it so far. It's handling all the games I play just fine and seems to even doing it cooler for most of them.


