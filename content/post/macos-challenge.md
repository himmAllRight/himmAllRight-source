+++
title  = "Challenge - 30 Days with macOS"
date   = "2019-12-22"
author = "Ryan Himmelwright"
image  = "img/posts/macos-challenge/atc.jpeg"
caption= "American Tobacco Campus, Durham, NC"
tags   = ["Hardware", "Apple", "Laptop", "Software"]
draft  = "True"
Comments = "True"
+++

Intro

<!--more-->

### The Challenge

>Using a mac as the interface device for my personal computing for 30 days.

Here, "interface computer" means the device that I sit at and interact with
it's GUI.
For example, I might be sitting at macOS and using it for my web browsing and
music, but working on a project on my linux workstation via a mosh/tmux session
in iTerm. I can use remote Linux computers as much as I please, but should
interact with them through macOS.

One thing to note is that I still used Desktop Linux as my "interfacing
computer" for work.

### Why

Currently, I am really only interesting in using macOS for
my personal computing. At home, I don't mind iOS and macOS teaming up to make
my "normal person" computing (web browsing, video chatting family, emails)
easier. Where I care about working on Linux is in the backend. So having the
front end get out of the way, and not tempt me with the ability to fine-tune
it, or even switch desktop environments completely, is a good thing for me
(currently).

At work on the other hand, I don't need my computer to by in step with my
personal phone and/or ipad. In fact, I like having that barrier there. Also,
Linux works REALLY well for the work I do, especially when it comes to running
VMs (I love `libvirt`). So, there currently isn't a reason (or even a desire)
to switch there.

***Side Note:*** I actually wouldn't even consider this challenge if I didn't get to use Linux
so much at work every day, or if I didn't have my Linux desktop/workstation. I
already ssh into my desktop to work from any other device. In fact, I technically
remote into my desktop even when I'm working AT it, since I do
nearly everything in a container.

### Observations


#### Stuff I didn't like
- The elephant in the room… it's very proprietary. Still love open source and
    using something that's as locked down and secretive as macOS and Apple
    products in general feels, well... *dirty*.
<center>
<a href="/img/posts/macos-challenge/joplin-error.png">
<img alt="joplin error" src="/img/posts/macos-challenge/joplin-error.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">Error while trying to run Joplin</div>
</center>

- I had trouble getting some applications like [Joplin](/post/switched-to-joplin-notes/) to work. I later learned that it was likely due to issues with signing the applications in Catalina (I think). Apparently, there is a work-around for this, but I haven't investigate it yet...
- There surprisingly isn’t a good solution for [virt-manager](https://virt-manager.org). I was able to install it using homebrew, but have to launch it from the terminal. I guess I might be able to setup an application launcher for it? Again, I haven't tried that yet. I'm just surprised there isn't a better solution on mac, or at least one that's easy to find...
- On that note, it is *great* that [brew](https://brew.sh) exists, but it confuses the hell out of me (What's a `cask`? Is it like a [`dnf` group](https://dnf.readthedocs.io/en/latest/command_ref.html#group-command-label) install?). This is most likely because I am new to it, in my (current) opinion, I still think it is nowhere near as nice as default Linux package managers. This is one area where using Linux for so long has spoiled me.

<center>
<video style="max-width:100%;" controls>
  <source src="../../img/posts/macos-challenge/network-connect.mp4" type="video/mp4">
</video>
<div id="caption">Connecting to a remote server's filesystem from the
file browser in Gnome (Linux)</div>
</center>

- Working with filesystems is a pain, especially when connecting to network devices. I couldn’t use Finder to do an easy network connection without first setting up samba or nfs on my Linux computers. I had to install `sshfs` using brew. While I ideally to setup a proper samba/nfs server on my desktop/server in the long run, it’s annoying that it couldn’t just mount the system in the file browser, using something like `sftp` under the hood like Linux does..
- Window management isn’t great out of the box. I had to buy [magnet](https://apps.apple.com/us/app/magnet/id441258766?mt=12) to snap/tile my windows. (Alternatively for touch-bar mac users, note that [better touch tool](https://folivora.ai) has window snapping and other features built in). Also, I can’t seem to hold a key and click a window anywhere to resize/move like I can in most linux DEs.
- My desktop workspaces keep changing their order on me XD.
- Deviating from the stock experience can become painful. For example, if you
    don't like using a global menubar, and a dock for applications... sorry?
    I'm sure there are third-party ways to get around it, but it will likely be
    hacky and not guaranteed to always work across new version of macOS.

#### Stuff I liked
- I actually am starting the like the CMD-centric shortcuts. They work everywhere and are nice when working with a terminal (which I do all the time).
- Default keybindings, while different from what I’m used to are actually intuative, and prevalent across the system. Not to many that are crazy/don’t make sense. For example, on Windows/Linux systems, the keybinding to close a window usually defaults to `Alt+F4` so I normally change it to `Super+Shift+Q`. While not the exact same as what I do, the macOS default of `CMD+Q` is close enough that I've been able to easily adapt to it, without feeling the need to figure out how to change it. It's a similar story across most of the default keybindings. They aren't exactly how I've been setting mine up, but close enough I'm fine with accepting them as it.
- iCloud syncing is nice - photos and messages.

<a href="/img/posts/macos-challenge/phonecall.png">
<img alt="Receiving and answering a phonecall in macOS" src="/img/posts/macos-challenge/phonecall.png" style="float: right; max-width: 100%; padding: 5px 15px 10px 10px"/></a>

- I like being able to answer *all* phone calls from my computer. This is
    because I hate talking on the phone, and am always on the computer. Oddly
    enough, I don't mind voice chat on the computer, so this works out really
    well for me. Synced iMessage and Facetime are also nice, but universal
    *normal* phone calls is what I particularly enjoy.


- Profiles. Specifically, setting up something like Fastmail in the mail app
    was SUPER easy because of this. I basically just downloaded the profile
    from fastmail and loaded into mail and everytihng was setup. That's it.


<a href="/img/posts/macos-challenge/header-bar-comparison-stacked.png">
<img alt="macOS header bars compared to Gnome" src="/img/posts/macos-challenge/header-bar-comparison-stacked.png" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">What the website homepage is *supposed* to look like</div>

- The UI really is space respecting. In addition to global menu, title bars are thin and minimal, and I think fonts and everything is just called down which makes me feel at least like I have more working space… especially compared to Gnome.
- Font and Video stuff just work without configuring anything/switching back and forth between Wayland and X sessions
- Gestures are actually great and intuitive. Even on this old MacBook, that trackpad works amazingly with them
- Things like screen time settings work across all my “front-end devices”. If I set a downtime for 8:30pm… it basically happens on all my computers and I basically get off. (The TV however … lol)

*--Screenshot of some of the default apps?--*

- Well made core apps (calendar, mail, notes)
- Photos is easy to do the obnoxious contrast photo editing I like doing
- Iterm2 is great. Also, mosh works well
- Privacy does actually seem to be a focus on the system.

#### Reservations/Fears


### Conclusion/Plans
