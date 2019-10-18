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

About a year ago, I [switched to using the LG ud4379b, a 42.5" 4k IPS
monitor](/post/new-lgud4379b/). My motivation to *switch* monitors was mostly
to convert to an IPS panel. My *selection of monitor* on the other hand, was an
attempt to simplify my hardware by only having one monitor. I wanted a
single monitor, but not at the cost of loosing the 2x(1920x1080) resolution my
dual 1080p setup had, because [everyone knows]() [that multiple monitors]()
[are required]() [to get any real work]() [done,]() [especially programming]().
After a year of using my massive display, I started to notice the *large display
paradox*.

<!--more-->

### Background

Before I dive into what exactly the *large display paradox* is and my
experience with it, lets quickly refresh on the past. In my [post about
choosing the 43" monitor](/post/new-lgud4379b/), I went in depth about my
history of using dual monitors, and *why* I wanted to switch to a single
monitor:

>While I like having the screen real estate of two monitors, I was never able to optimally use them because of the bezels between the monitors. While working, I would naturally shift over and use one monitor as a primary display, and the other as a secondary display.

I wanted to be able to stare at my monitor straight on, without any
bezels getting in the way. I also knew that a single 1080p monitor was just a
bit too cramped.

In that same paragraph, I provided an additional reason for the switch. If I
had been paying closer attention, I might have noticed it
foreshadowing the large display paradox:

>This was okay for some tasks, but it usually meant that I just used the primary monitor, and half of the secondary one, because it was too hard to see the far end of the screen.


<a href="/img/posts/large-display-paradox/4-monitors.jpg">
<img alt="Wayland logo" src="/img/posts/large-display-paradox/4-monitors.jpg" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">I was excited to use a single monitor as a 4x1080p bezel-less
grid... even though I already had trouble seeing the edges of my 2x1080
monitor setup...</div>

While I was aware that large screen may not be optimal, the lure of having 4
monitors in one was just too strong to let go of. This is apparent in the section where I compare the LG 43" with the Dell ultrawide:

>Being so large, I could still have auxiliary windows opened on either side. One advantage the ud4379 had over the ultra-wide however, was that being a massive 16:9 screen, it could easily be divided into 4 1080p screens.

Despite a nagging voice in the back of my head reminding me that a *single* 27"
1440p monitor was an option... I ignored it and picked up the 43" LG monitor.

(I just want to be clear... the LG is a *Great* monitor!)

### The Large Display Paradox

#####  Background information on what the "Large Display Paradox" is

So. What *is* the *"Large Display Paradox"*? As far as I can find, the term was
coined by Jeff Atwood in a [blog post titled with the same
name](https://blog.codinghorror.com/the-large-display-paradox/). In the post,
Atwood refers to [another post](http://www.dansdata.com/3007wfp-hc.htm) in
which Dan Rutter states the following while reviewing his new Dell UltraSharp
3007WFP-HC monitor:

>Users of 30-inch monitors face the terrible, terrible problem of how to
effectively use all of that space. You don't often want to maximise a folder or
document window on a screen this big; either you'll end up with a lot of white
space and important program buttons separated by a vast expanse of nothing, or
you'll get lines of text 300 or more characters long, which are difficult to
read.


Atwood summarizes that this is a perfect example of what he deems to be the
*Large Display Paradox*:

>That's the large display paradox. Having all that space can make you less
productive due to all the window manipulation excise you have to deal with to
make effective use of it.

He further explains how once a display grows beyond the point of being able to
efficiently maximize windows without too much whitespace (above 1600x1200, by
his estimates), it becomes *less productive* due to the user having to
continuously manage the windows.

While these posts are on the older side (2007!), I think the issue is even more
possible today.

### My Experience

With the *Large Display Paradox* finally defined... did I experience it with my
very large 43" monitor? Yes. At first, it was great. I loved throwing
everything I wanted up on a single screen.

<a href="/img/posts/large-display-paradox/work-widescreen.jpg">
<img alt="Widescreen work RDP session" src="/img/posts/large-display-paradox/work-widescreen.jpg" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">I enjoyed remoting to my Windows work computer using an ultrawide
resolution, and still having space for my notes and chat applications below.</div>

In particular, during the first few months using the monitor, I still worked
remotely for my previous job and needed to use a Windows machine. I appreciated
that I could RDP to my work computer using an ultrawide resolution, but *still*
have space to keep my notes and chat windows below it.

Then, I switched jobs and used Linux 100% for home *and* work. Instead of
having to RDP into a second machine... I could just `ssh` using a small
terminal window. I no longer had to view multiple machine desktops to get work
done.

### Issues

At first, I still didn't see an issue, especially when using it on my personal
computer. I was mostly on my computer for leisure anyway, so it didn't matter
as much if I also had a video and chat window next to met personal project.
However, when I tried to *focus* on a task, the "usefulness" of the large
screen really started to fall apart. Here are a few issues I started to run up
against when trying to be productive with what was seemingly one of "the best
productivity monitors on the market".

#### Always wanting to fill the space.

The tricky thing about having all that space... is you want to fill it, even if
you don't *need* to for the task at hand. So for example, if I wanted to work
on writing a blog post, all I *need* is my text editor. In addition, I like to
have a preview of the post open in a browser so I can see how the post renders.
While I sometimes like to also have a photo editor and picture folders also
open, it is best if I can have them in a separate [virtual
workspace](https://en.wikipedia.org/wiki/Virtual_workplace). In reality,
everything beyond my text editor, really starts to detract from my ability to
focus on *writing* the post.

<a href="/img/posts/large-display-paradox/filling-space.jpg">
<img alt="Filling up the monitor's space" src="/img/posts/large-display-paradox/filling-space.jpg" style="max-width: 100%; padding: 5px 15px 10px 10px"/></a>
<div class="caption">With so much space, I felt obligated to fill it with
windows unrelated to the task at hand...</div>

It turns out people really like filling space. How often do you find that a
particular surface in the house seems to *always* collect random crap? Large
monitors are the same. Even when I *knew* I only needed a single small terminal
in from of me... the vast space surrounding it always made me feel uneasy. So I
would fill the space by either extending the editor window to a comical size,
or litter the surround space with random applications, unrelated to the work I
was trying to focus on.

#### I didn't use the entire space, just focused on what was in my field of view in front of me.

#### I couldn't fullscreen my windows, or even split screen them really (too big)

#### Without being able to split nicely, I couldn't use quick keyboard shortcuts to setup windows
	- This meant I was manually moving my windows around
	- It also meant using tiling window managers like i3 (or sway), was out of the question.



### Conclusion
I think the large display paradox could be a real modern tech issue. More
accurately, a [first world
problem](https://en.wikipedia.org/wiki/First_World_problem). Given the
increased affordability of large displays, what might seem like an great setup,
might not actually be optimal, given one's workload. At it's core, technology
is a tool, and it should be configured to best aid us in the tasks we use it
for. (bleh. Terrible sentence)
