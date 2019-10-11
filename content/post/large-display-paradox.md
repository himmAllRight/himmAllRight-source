+++
title  = "My Experience with the Large Display Paradox"
date   = "2019-10-13"
author = "Ryan Himmelwright"
image  = "img/posts/large-display-paradox/dc-rooftop.jpg"
caption= "Crimson View Rooftop Bar, Washington DC"
tags   = ["linux", "homelab", "dotfiles", "security"]
draft  = "True"
Comments = "True"
+++

About a year ago, I [switched to using LG's ud4379b, a single 42.5" 4k IPS
monitor](/post/new-lgud4379b/). My motivation to *switch* monitors was mostly
to convert to an IPS panel. My *selection of monitor* on the other hand, was an
attempt to simplify my hardware by only having a single monitor. I wanted a
single monitor, but not at the cost of loosing the 2x(1920x1080) resolution my
dual 1080p setup had, because [everyone knows]() [that multiple monitors]()
[are required]() [to get any real work]() [done,]() [especially programming]().
After a year of using my massive display, I started to feel the large display
paradox.

<!--more-->

### Background

Before I dive into what exactly the *large display paradox* is and how I
experienced it, lets refresh on the past. In the [post about choosing my 43"
monitor](/post/new-lgud4379b/), I went in depth about my history of using dual
monitors, and *why* I wanted to switch to a single monitor:

>While I like having the screen real estate of two monitors, I was never able to optimally use them because of the bezels between the monitors. While working, I would naturally shift over and use one monitor as a primary display, and the other as a secondary display.

Basically, I wanted to be able to stare at my monitor straight on, without any
bezels getting in the way. I also knew that a single 1080p monitor was just a
bit too cramped though.

In that same paragraph, I provided an additional reason for the switch. If I
had been paying closer attention, I might have noticed it
foreshadowed the large display paradox:

>This was okay for some tasks, but it usually just meant that I just used the primary monitor, and half of the secondary one, because it was too hard to see the far end of the screen.

While I was aware that large screen may not be optimal, the lure of having 4
monitors in one was just too strong to let go of. This is apparent in the section where I compare the LG 43" with the Dell ultrawide:

>Being so large, I could still have auxiliary windows opened on either side. One advantage the ud4379 had over the ultra-wide however, was that being a massive 16:9 screen, it could easily be divided into 4 1080p screens.

Despite a nagging voice in the back of my head reminding me that a *single* 27"
1440p monitor was an option... I ignored it and picked up the 43" LG monitor. (Don't get me wrong, It's a *Great* monitor!)

### The Large Display Paradox

#####  Background information on what the "Large Display Paradox" is

So. What *is* the *"Large Display Paradox"*? As far as I can find, the term was
coined by Jeff Atwood in a [blog post titled with the same
name](https://blog.codinghorror.com/the-large-display-paradox/). In the post,
Atwood refers to [another post](http://www.dansdata.com/3007wfp-hc.htm) in
which Dan Rutter states while reviewing his new Dell UltraSharp 3007WFP-HC monitor (remember... each of these posts are from over 10 years ago!)

>Users of 30-inch monitors face the terrible, terrible problem of how to
effectively use all of that space. You don't often want to maximise a folder or
document window on a screen this big; either you'll end up with a lot of white
space and important program buttons separated by a vast expanse of nothing, or
you'll get lines of text 300 or more characters long, which are difficult to
read.


Atwood claims this is a perfect example of what he deems the *Large Display Paradox*:

>That's the large display paradox. Having all that space can make you less
productive due to all the window manipulation excise you have to deal with to
make effective use of it.

explains how once a display grows beyond the point of being able to
efficiently maximize windows without too much whitespace (above 1600x1200 by
his estimates), it becomes *less productive* due to the user having to
continuously manage the windows.

### My Experience

<a href="/img/posts/large-display-paradox/work-widescreen.jpg">
<img alt="Wayland logo" src="/img/posts/large-display-paradox/work-widescreen.jpg" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">I enjoyed remoting to my Windows work computer using an ultrawide
resolution, and still having space for my notes and chat applications below.</div>

With the *Large Display Paradox* finally defined... did I expereince it with my
very large 43" monitor? In sort, yes. At first, it was great. I loved throwing
everything I needed up on a single screen. In particular during the first few
months, I still worked remotely for my previous job and required to work on a
Windows machine. I loved that I could RDP to my work computer with an ultrawide
resolution from my linux laptop, and *still* have space to keep my notes and
chat windows below it.

Switch to Linux


- However, when I tried to *focus* on a task, the usefulness really started to
    fall apart.

### Issues
- I didn't use the entire space, just focused on what was in my field of view in front of me.
- I couldn't fullscreen my windows, or even split screen them really (too big)
	- Without being able to split nicely, I couldn't use quick keyboard shortcuts to setup windows
	- This meant I was manually moving my windows around
	- It also meant using tiling window managers like i3 (or sway), was out of the question.


