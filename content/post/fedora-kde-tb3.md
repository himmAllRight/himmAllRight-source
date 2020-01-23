+++
title  = "Authorizing Thunderbolt 3 on non-Gnome Fedora"
date   = "2020-01-26"
author = "Ryan Himmelwright"
image  = "img/posts/new-2019-16inch-mbp/mbp-box-header.jpeg"
tags   = ["Hardware", "Linux", "Laptop", "Thinkpad", "fedora", "tb3"]
draft  = "False"
Comments = "True"
+++

Since getting my [16" MacBook Pro](/post/new-2019-16inch-mbp/) the other month,
I've been using a Thunderbolt 3 hub to connect not only the Macbook to my
periphery devices, but also my work laptop when working from home. Normally, it
works fine. However, last week I installed Fedora Workstation Plasma... and the
TB3 hub didn't work. Here's why.

<!--more-->

## The Issue

Due to a NVIDIA Quadro M1000M in my [lenovo
P50](https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-p/ThinkPad-P50/p/22TP2WPWP50)
work laptop, I've been using Gnome and Wayland because I tend to have
trade-offs running others. While doing a system refresh, I thought I'd see if
things are any different with a fresh Fedora 31 Plasma install (they weren't,
but that's beyond this post).

*< Image of Gnome TB3 Settings? >*

Booting into the live cd, and even the installed system, I noticed that my
Thunderbolt 3 did *not* work while I was in Plasma. This is because for
security reasons, Linux distros tend to disable thunderbolt ports by default.
In gnome, there are now settings to authorize it which I guess I had done on my
previous install (although I forgot about it). In Plasma however, I needed to
install and configure `bolt`.

## Bolt

In Fedora, `bolt` is in the base repos, so installing it is easy:

```
sudo dnf install bolt
```


## Authorizing

### Listing Devices

### Authorizing Device

## Conclusion
