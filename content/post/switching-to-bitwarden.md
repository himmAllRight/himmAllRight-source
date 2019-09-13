+++
title  = "Switching to Bitwarden"
date   = "2019-09-12"
author = "Ryan Himmelwright"
image  = "img/posts/switching-to-bitwarden/trosa-college-dressers.jpg"
caption= "TROSA Thrift Store and Donation Center, Durham NC"
tags   = ["Linux", "Homelab", "dotfiles"]
draft  = "True"
Comments = "True"
+++

After years of using the [password store](https://www.passwordstore.org/) as my
password manager, I am switching things up. Over vacation, I started
transferring my password to [Bitwarden](https://bitwarden.com/). I have finally
finished transferring all of my passwords and will be switching over to use it
as my main password manager. Here are my thoughts so far.

<!--more-->

### Why Switch?
First of all, I want to point out that I had already started my switch *before*
the large bitwarden segment on the [recent episode of Linux
Unplugged](https://linuxunplugged.com/316). That was just a re-assuring
coincidence. So, why did I decide to switch?

*(By the way, it turns out this section doubles as my usual "What I like"
section)*

#### Easier Setup

<a href="/img/posts/switching-to-bitwarden/bigtwarden-flathub.png">
<img alt="Bitwarden on Flathub Page" src="/img/posts/switching-to-bitwarden/bitwarden-flathub.png" style="max-width: 100%;"/></a>
<div class="caption">Bitwarden on Flathub</div>

Probably the main reason is that when configuring a new system, it is simply
easier to setup. All I need to do is install bitwarden and login. This is made
even easier by the fact that Bitwarden is packaged as a [Flatpak on
flathub](https://flathub.org/apps/details/com.bitwarden.desktop). So on my
[Fedora Silverblue](https://silverblue.fedoraproject.org/) computers it just
works as expected out of the box without having to mess around at all.

#### Mobile Support

<a href="/img/posts/switching-to-bitwarden/bitwarden-ipad.jpg">
<img alt="Bitwarden on Flathub Page" src="/img/posts/switching-to-bitwarden/bitwarden-ipad.jpg" style="float: right;width: 250px; max-width: 100%; padding: 5px 5px 10px 10px"/></a>

Over the past few months, I have been [switching up some of the tools I
use](/post/switched-to-joplin-notes/), at least the ones I use for my [non-work
life](/post/back-on-org-mode-for-work/). A big diving force for some of many of
these switches is better mobile support. While I still prefer to keep as much
off of my phone as possible, there are some things I like/need to have on the
go. My password manager is unfortunately one of them.

Additionally, as I start to test out different workloads on alternative devices
like my ipad, having a mobil-friendly workflow is helpful. In fact, trying to
setup my password manager on my iPad is what caused me to try bitwarden. It was
just too much of a pain to get my [pass](/post/setting-up-pass/) configuration
up and working on the iPad.

By comparison, to setup Bitwarden I just had to install the app and login. The
experience was the exact same on my phone.

#### Wayland Friendly

<a href="/img/posts/switching-to-bitwarden/wayland-logo.png">
<img alt="Wayland logo" src="/img/posts/switching-to-bitwarden/wayland-logo.png" style="float: left; width: 250px; max-width: 100%; padding: 5px 15px 10px 10px"/></a>

One of my favorite parts of my pass system was how well it was integrated into
my desktop environment. *However*, I have been wanting to switch to wayland
more than ever now, but probably the biggest blocker keeping me from being able
to use wayland at least 90% of the time on all my machines... was my pass
setup. I mainly access pass using helper launcher applications like `dmenu` and
`rofi`. However, they do not play very nicely with wayland so I had to just use
`pass` from the terminal while in a wayland session. Bitwarden, (at least the
limtied GUI interactions I've used thus far), works just fine in wayland.

#### Easier to share/expand

Lastly, if my wife eventually wants to switch to bitwarden, I *think* we could
still share our joint passwords with each other using the free personal
service. If not, we can upgrade to the "family plan" which is currently $1/mo
and allows unlimited collections across 5 accounts *and* optional self hosting.

### What I am still learning
Normally, this is where I list the few things that I "don't like". However,
this is all new still and I *think* the majority of my current issues are
solvable, but I just haven't figured it out yet. So it's a "What I'm still
learning" section (•‿•) .

#### Better keyboard/DE integration

The *main feature* I still seem to be missing is better keyboard
support/integration with the desktop environment. The GUI app is nice, and
bitwarden has *much* better support for browser extensions and tools, but I
haven't found a good way yet to open up bitwarden (give my master password),
search for an item, and copy the password... all from the keyboard.

<center>
<video style="max-width:100%;" controls>
  <source src="../../img/posts/setting-up-pass/passmenu_demo.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
<div id="caption">`passmenu` lets you easily search and select a pass item.</div>
</center>

By comparison, `pass` let me integrate with launchers like `dmenu` and `rofi`
to efficiently grab my passwords which was *awesome*. As mentioned in the
section above, the `passmenu` also falls apart for me these days now that I am
mostly on wayland... but I don't need pass support. Honestly, all I *need* is
the ability to copy a password (and maybe other fields) using my keyboard once
I have selected an item. I can already search using `ctrl-f`, and `tab` then
`arrow` my way down the list, but once there I can copy unless I tab through
all the options.

This is a highly request feature, and I'm sure someone has hacked *some
solution* together... I just have yet to find it, or implement it myself.

### Conclusion

That is it. I've switched to bitwarden and have been using it as my main
password manager for almost a month now and I love it. It works on *all* my
devices and doesn't give me *too* many headaches. My only real complaint is I
wish it had better keyboard support, but I'm sure I'll be able to figure
out a work-around eventually.
