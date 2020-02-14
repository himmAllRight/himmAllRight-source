+++
title  = "Authorizing Thunderbolt 3 on Fedora Plasma"
date   = "2020-01-25"
author = "Ryan Himmelwright"
image  = "img/posts/fedora-kde-tb3/leaves.jpeg"
caption = "Durham, NC"
tags   = ["Hardware", "Linux", "Laptop", "Thinkpad", "fedora", "tb3", "kde"]
draft  = "False"
Comments = "True"
+++

After buying a [16" MacBook Pro](/post/new-2019-16inch-mbp/) the other month,
I've been using a Thunderbolt 3 hub to connect it to my periphery devices.
Luckily, in addition to the macbook, I am able to use the hub with my my work
laptop when working from home. Normally, it works fine. However, last week I
reformatted the work laptop with the [*KDE Plasma* spin](https://spins.fedoraproject.org/kde/) of
Fedora Workstation 31... and my TB3 hub stopped playing nicely with it.
Here's why.

<!--more-->

## The Issue

Due to a NVIDIA Quadro M1000M in my lenovo P50 work laptop, I've been using
Gnome with Wayland, because that combination seems to have the least amount of
annoying trade-offs. While doing a system refresh, I figured I would see if
things are any different with a clean Fedora 31 Plasma install (they weren't,
but that's beyond this post).

<center>
<a href="/img/posts/fedora-kde-tb3/gnome-tb3-settings.png">
<img alt="Gnome Thunderbolt Settings" src="/img/posts/fedora-kde-tb3/gnome-tb3-settings.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">The Gnome desktop environment now has a thunderbolt pane
in the settings GUI</div>
</center>

Booting into the live cd, and later the installed system, I noticed that my
Thunderbolt 3 hub did *not* work while I was in Plasma. That was fine. I
expected it really, because for security reasons Linux distros tend to disable
thunderbolt ports by default.  In gnome, there are now settings to authorize
it (which I guess I had done on my previous install, and forgot about).  In
Plasma however, I needed to install and configure `bolt`.

## Bolt
<center>
<a href="/img/posts/fedora-kde-tb3/bolt-install.png">
<img alt="Installing bolt with dnf" src="/img/posts/fedora-kde-tb3/bolt-install.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">`bolt` is in the Fedora repos and is easily installed with
`dnf`</div>
</center>

In Fedora, `bolt` is in the repos (at least in Fedora 31+), so installing it is
easy:

```
sudo dnf install bolt
```

Once `bolt` is installed, it isn't a bad idea to check to make sure it is
running: `sudo systemctl bolt`.

<center>
<a href="/img/posts/fedora-kde-tb3/bolt-systemctl-status.png">
<img alt="bolt systemctl status" src="/img/posts/fedora-kde-tb3/bolt-systemctl-status.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Checking `bolt` is running using `systemctl status`</div>
</center>

If the status shows that it isn't running for some reason, it can be started
using `systemctl start bolt`. Check the status again, and if it it *still* is not
running... sorry?

<center>
<a href="/img/posts/fedora-kde-tb3/boltctl.png">
<img alt="boltctl" src="/img/posts/fedora-kde-tb3/boltctl.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption"></div>
</center>

With bolt installed, the command `boltctl` is available to use. The base command will
show information about attached thunderbolt devices. To see more `boltctl`
commands, run `boltctl --help`.

## Authorizing

<center>
<a href="/img/posts/fedora-kde-tb3/boltctl-authorize.png">
<img alt="boltctl authorize" src="/img/posts/fedora-kde-tb3/boltctl-authorize.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Authorizing the device</div>
</center>

In order to *use* the thunderbolt 3 device, it needs to be authorized. To
authorize a device, first use a plain `boltctl` command to get the `uuid` of
the device. Next, call `boltctl authorize` using the `uuid` to authorize it:

```
boltctl authorize <UUID HERE>
```

The device should now be authorized. When I authorized mine, some of my devices
started showing up automatically, while others needed to be disconnected and
replugged.

## Enrolling

<center>
<a href="/img/posts/fedora-kde-tb3/bresetoltctl-enroll.png">
<img alt="boltctl enroll" src="/img/posts/fedora-kde-tb3/boltctl-enroll.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Enrolling the device for permanent use</div>
</center>

Authorizing a device enables it to be used, but doesn't guarantee persistence.
While this may be desired to grant *temporary* authorization to a device, many
users tend want their device to *always* work, without having to manually
authorize it. In this case, the device should be *enrolled* (like `systemctl enable`).
Simply call `boltctl enroll`, with the device UUID:

```
boltctl enroll <UUID HERE>
```

Once enrolled, the device's UUID will be recorded and added to a database. By
default, the device will now automatically be authorized whenever it is
connected.

## Conclusion

That's it. While the solution isn't very difficult, it can be frustrating to
figure out when it appears that the thunderbolt device simply is not working.
Regardless, I'm glad that I now know about `bolt` and how to use it!
