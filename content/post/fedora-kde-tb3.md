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

<center>
<a href="/img/posts/fedora-kde-tb3/gnome-tb3-settings.png">
<img alt="Gnome Thunderbolt Settings" src="/img/posts/fedora-kde-tb3/gnome-tb3-settings.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">The Gnome desktop environment now has a thunderbolt pane
in the settings GUI</div>
</center>

Booting into the live cd, and even the installed system, I noticed that my
Thunderbolt 3 did *not* work while I was in Plasma. This is because for
security reasons, Linux distros tend to disable thunderbolt ports by default.
In gnome, there are now settings to authorize it which I guess I had done on my
previous install (although I forgot about it). In Plasma however, I needed to
install and configure `bolt`.

## Bolt
<center>
<a href="/img/posts/fedora-kde-tb3/bolt-install.png">
<img alt="Installing bolt with dnf" src="/img/posts/fedora-kde-tb3/bolt-install.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">`bolt` is in the Fedora repos and is easily installed with
`dnf`</div>
</center>

In Fedora, `bolt` is in the base repos (at least in Fedora 31+), so installing
it is easy:

```
sudo dnf install bolt
```

Once `bolt` is installed, it isn't a bad idea to check the status of it. This
is accomplished with `sudo systemctl bolt`.

<center>
<a href="/img/posts/fedora-kde-tb3/bolt-systemctl-status.png">
<img alt="bolt systemctl status" src="/img/posts/fedora-kde-tb3/bolt-systemctl-status.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Checking `bolt` is running using `systemctl status`</div>
</center>

If the status shows that it isn't running for some reason, it can be started
using `systemctl start bolt`. Run a status again if it it *still* is not
running... sorry? I would suggest researching the issue  using the logs in the
status output.

<center>
<a href="/img/posts/fedora-kde-tb3/boltctl.png">
<img alt="boltctl" src="/img/posts/fedora-kde-tb3/boltctl.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption"></div>
</center>

With bolt installed, the command `boltctl` can be used. The base command will
show the information of attached thunderbolt devices. To see more `boltctl`
commands, enter `boltctl --help`.

## Authorizing

<center>
<a href="/img/posts/fedora-kde-tb3/boltctl-authorize.png">
<img alt="boltctl authorize" src="/img/posts/fedora-kde-tb3/boltctl-authorize.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Authorizing the device</div>
</center>


<center>
<a href="/img/posts/fedora-kde-tb3/boltctl-enroll.png">
<img alt="boltctl enroll" src="/img/posts/fedora-kde-tb3/boltctl-enroll.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Enrolling the device for permanent use</div>
</center>

## Conclusion
