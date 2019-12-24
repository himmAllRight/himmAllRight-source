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
- The elephant… it's very proprietary. The ecosystem is great but REALLY locks out anyone not in the high-end market, or willing to buy used, or change their computing paradigm (switching to a more affordable iPad in place of a macbook).
- At first I had issues getting some applications like Joplin to work. I later learned that it's due issues with signing the applications for Catalina (I think). There apparently is a work-around for this, but I didn't investigate it..
- There surprisingly isn’t a good replacement for Virt-viewer. I got it installed with home-brew, but have to launch it from the terminal, unless I setup an application I guess (which I haven't figured out how to do yet).
- It’s *great* that brew exists, but it confuses the hell out of me and is nowhere as nice as the Linux package managers (IMO).
- Filesystem access is a pain, especially when trying to connect to network devices. I had to install `sshfs` with brew, and  I couldn’t do a normal network connection without first setting up samba or nfs on my Linux computers. While I want to setup a proper samba/nfs server on my desktop/server in the long run, it’s annoying that it couldn’t just mount the system in Finder, using something like `sftp` under the hood like Linux does..
- Window management isn’t great out of the box. I had to by magnet to snap my windows which is better. Also, I can’t seem to hold a key and click a window anywhere to resize/move like I can in most linux DEs.
- The Dongle is annoying. Ports and connections worked fine on the air, but now that I’m on the pro and have to use a usb-c for anything, the “cheap” $20 hub I got is very flakey. I wonder if I got an actual thunderbolt one it’d be better…Or even one of the simple HDMI+USB ones but made by apple (that’s all I really need with my usb3 hub). Still. I’ll have to do something better I think. This thing heats up right away and won’t be a great solution long-term if I want to use the MacBook as my interfacing computer at the desk too…


#### Stuff I liked
- I actually am starting the like the CMD-centric shortcuts. They work everywhere and are nice when working with a terminal (which I do all the time).
- Default keybindings, while different from what I’m used to are actually intuative, and prevalent across the system. Not to many that are crazy/don’t make sense. For example, on Windows/Linux systems, the keybinding to close a window usually defaults to `Alt+F4` so I normally change it to `Super+Shift+Q`. While not the exact same as what I do, the macOS default of `CMD+Q` is close enough that I've been able to easily adapt to it, without feeling the need to figure out how to change it. It's a similar story across most of the default keybindings. They aren't exactly how I've been setting mine up, but close enough I'm fine with accepting them as it.
- iCloud syncing is nice - photos and messages.
- I think it’s neat that I can take calls from my iPhone with my computer…
- - Profiles. Specifically, setting up something like Fastmail in the mail app
    was SUPER easy because of this. I basically just downloaded the profile
    from fastmail and loaded into mail and everytihng was setup. That's it.
- The UI really is space respecting. In addition to global menu, title bars are thin and minimal, and I think fonts and everything is just called down which makes me feel at least like I have more working space… especially compared to Gnome.
- Font and Video stuff just work without configuring anything/switching back and forth between Wayland and X sessions
- Gestures are actually great and intuitive. Even on this old MacBook, that trackpad works amazingly with them
- Things like screen time settings work across all my “front-end devices”. If I set a downtime for 8:30pm… it basically happens on all my computers and I basically get off. (The TV however … lol)
- Well made core apps (calendar, mail, notes)
- Photos is easy to do the obnoxious contrast photo editing I like doing
- Iterm2 is great. Also, mosh works well
- Privacy does actually seem to be a focus on the system.

#### Reservations/Fears


### Conclusion/Plans
