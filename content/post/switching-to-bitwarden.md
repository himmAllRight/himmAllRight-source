+++
title  = "Switching to Bitwarden"
date   = "2019-09-13"
author = "Ryan Himmelwright"
image  = "img/posts/switching-to-bitwarden/trosa-college-dressers.jpg"
caption= "TROSA Thrift Store and Donation Center, Durham NC"
tags   = ["linux", "homelab", "dotfiles", "security"]
draft  = "False"
Comments = "True"
+++

After years of using [pass](https://www.passwordstore.org/) as my password
manager, I am mixing things up. Over vacation, I started importing all of my
passwords into [Bitwarden](https://bitwarden.com/). With all my passwords
finally transferred, I have now switched to using Bitwarden full-time. Here
are my thoughts so far.

<!--more-->

### Why Switch?
Before I start, I want to point out that I had already started my switch *before*
the large Bitwarden segment on the [recent episode of Linux
Unplugged](https://linuxunplugged.com/316). That was just a re-assuring
coincidence `:)` .

So, why did I decide to switch?

#### Easier Setup

<a href="/img/posts/switching-to-bitwarden/bigtwarden-flathub.png">
<img alt="Bitwarden on Flathub Page" src="/img/posts/switching-to-bitwarden/bitwarden-flathub.png" style="max-width: 100%;"/></a>
<div class="caption">Bitwarden on Flathub</div>

The main reason is that when configuring a new system, Bitwarden is simply
easier to setup. All I need to do is install a Bitwarden client and login. In
fact, using the hosted service I don't even need to do that. I can just login
using the [web vault](https://vault.bitwarden.com/). Installing is made even
easier by the fact that Bitwarden is packaged as a [Flatpak on
flathub](https://flathub.org/apps/details/com.bitwarden.desktop). So on my
[Fedora Silverblue](https://silverblue.fedoraproject.org/) computers, it works
out of the box and already fits in with the design philosophy behind Silverblue
(running all user apps in containers). Perfect.

#### Mobile Support

<a href="/img/posts/switching-to-bitwarden/bitwarden-ipad.jpg">
<img alt="Bitwarden on Flathub Page" src="/img/posts/switching-to-bitwarden/bitwarden-ipad.jpg" style="float: right;width: 250px; max-width: 100%; padding: 5px 5px 10px 10px"/></a>

Over the past few months I have been [switching up the tools I
use](/post/switched-to-joplin-notes/), at least the ones I use [outside of
work](/post/back-on-org-mode-for-work/). The big driving force behind many of
these switches is better mobile support. While I still prefer to keep as much
data off of my phone as possible, there are some things I need to have on the
go. My password manager is unfortunately one of them.

Additionally, as I start to test out different workloads on alternative devices
like my ipad, having a mobil-friendly work flow is a godsend. In fact, trying to
[setup pass](/post/setting-up-pass/) on my iPad is what eventually frustrated
me enough to give Bitwarden a chance.

Setup on both my phone and ipad was dead-simple. Install the app, and login.
Done.

#### Wayland Friendly

<a href="/img/posts/switching-to-bitwarden/wayland-logo.png">
<img alt="Wayland logo" src="/img/posts/switching-to-bitwarden/wayland-logo.png" style="float: left; width: 250px; max-width: 100%; padding: 5px 15px 10px 10px"/></a>

One of the best features of my pass system was how well it was integrated with
my desktop environment. *However*, I want to switch to wayland now more than
ever, but my pass desktop integration is the biggest blocker preventing me from
using it on my machines. I access pass using launcher applications like `dmenu`
and `rofi`... but they do not function correctly in wayland. This forced me to
use `pass` from a terminal window while in a wayland session. Bitwarden, at
least the limited GUI interactions I've used thus far, appears to work just
fine in wayland.

#### Easier to share/expand

Lastly, if my wife eventually wants to switch to Bitwarden, I *think* we can
share our joint passwords with each other, even being on just the free personal
plan. If not, we can upgrade to the "family plan" which is currently $1/mo and
allows unlimited collections across 5 accounts *and* optional self hosting. For
shared family password management... that's a great deal.

### What I am still learning
Normally, this is where I list the few things that I "don't like". However,
this still is all new and I *think* the majority of my current issues are
solvable, but I just haven't figured it out yet. So it's a "What I'm still
learning" section this time (•‿•) .

#### Better keyboard/DE integration

The *main feature* I still seem to be missing is better keyboard
support/integration with the desktop environment. The GUI app is nice, and
Bitwarden has *much* better support for browser extensions and tools. Yet, I
haven't found a good way to open up Bitwarden (give my master password),
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
to efficiently grab my passwords which was *awesome*. As mentioned a few
sections above, `passmenu` unfortunately falls apart for me these days now that I am
mostly on wayland... but I don't need a full launcher. Honestly, all I
*need* is the ability to copy a password (and maybe other fields) using my
keyboard once I have selected an item. I can already search using `ctrl-f` +
`tab`, and then `arrow` my way down the list, but once there I cannot copy
unless I continue to tab through all the options. This is not efficient and
defeats the purpose of remaining on the keyboard in the first place.

This is a highly requested feature, and I'm sure someone has hacked *some
solution* together... I just have yet to find it... or implement it myself.

### Conclusion

That is it. **TLDR;** I've switched to Bitwarden and have been using it as my
main password manager for almost a month and I love it. It works on *all*
my devices and doesn't give me too many headaches. My only real complaint is
that I wish it had better keyboard support, but I'm sure I'll be able to figure
out a work-around eventually.
