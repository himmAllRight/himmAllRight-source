+++
title   = '2020 M1 Macbook Air Initial Thoughts'
date    = "2021-03-01"
author  = "Ryan Himmelwright"
image   = "img/posts/m1-air-initial-thoughts/m1_air_header.jpeg"
caption = "Durham, NC"
tags    = ["hardware", "apple", "laptop", "macbook", "macos"]
draft   = "False"
Comments = "True"
+++

As discussed in my [previous post](/post/trading-mbp16-for-m1air/), I decided
to trade-in my 2019 16" MacBook Pro and replace it with a new 2020 M1 MacBook
Air. So far, I think making the swap was a great idea. Here are
my initial thoughts...

<!--more-->

## Background (what I ordered)

<a href="../../img/posts/m1-air-initial-thoughts/m1_air_box.jpeg"><img alt="The M1 Air Box" src="../../img/posts/m1-air-initial-thoughts/m1_air_box.jpeg" style="max-width: 100%;"/></a>
<div class="caption">The MacBook Air Box</div>

To recap, I got the 'second tier' model 2020 M1 MacBook Air (Silver, 8 gpu
cores, 512GB ssd) and upgraded the RAM to 16Gb. I wanted to maintain the same
RAM and storage that my MBP had. After way too many weeks (3+), the air
showed up at my door.


## What I Like


<a href="../../img/posts/m1-air-initial-thoughts/side.jpeg"><img alt="The M1 Air Side" src="../../img/posts/m1-air-initial-thoughts/side.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Side of the MacBook Air</div>


First, lets start with the good. There is a lot to say here, but these are my
main thoughts:

- It's cool and ~~quiet~~ *silent*. It hardly heat up, and when
it does, it is *barely* noticeable.

- It very portable. I can easily pick it up with one had and open it up on my
lap nearly anywhere.

- I like having physical function keys again, especially now that I learned
how to utilize [BetterTouchTool](https://folivora.ai) for window management
using keyboard shortcuts, instead of the touch bar.

<center>
<video style="max-width:100%;" controls>
  <source src="../../img/posts/m1-air-initial-thoughts/wake_compare.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
<div id="caption">The instant wake is nicer than I thought it would be</id>
</center>

- Instant wake is actually delightful. I honestly thought my sleep settings were
misconfigured, and the laptop simply wasn't turning off when I shut the lid. It's a
feature that I thought "who cares" when it was announced, but after I tried
it, my 16" suddenly felt unbearably slow for the few days I had both.

- Rosetta II is amazing at what it does. Most apps just work because of it,
even if they haven't been ported to Apple Silicon yet. This has made the transition
rather seamless.

- It works surprisingly well at my desk on the stand. Possibly even better
than the 16". The laptop is about the same size of by stand, so I'm able to
push it further back, out of the way, and it is much sturdier. The smaller
screen hasn't been an issue with the content I usually on it at my desk
(background videos or nothing usually). With how cool it runs, I also feel
safer closing it to focus solely on my external monitor, almost as if I was
using a mac mini.

<center>
<video style="max-width:100%;" controls>
  <source src="../../img/posts/m1-air-initial-thoughts/terminal_compare.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
<div id="caption">New tabs in my terminal lagged for some reason on the MBP. Not on the Air though!</id>
</center>


- My terminal instantly opens! For some reason on my mac, it always took
a second to load the shell prompt in iterm with my config. On the air,
it is instant.

- Garage band works much better. It opens immediately and is ready. My 16"
would take forever to load, and then often beach-ball and crash.

- The battery life is great. I don't really think about it.

## What Could be Better

<a href="../../img/posts/m1-air-initial-thoughts/macbooks_compare.jpeg"><img alt="My old MacBook Pro and the new M1 Air" src="../../img/posts/m1-air-initial-thoughts/macbooks_compare.jpeg" style="max-width: 100%;"/></a>
<div class="caption">The Air has thicker bezels compared to my old 16" MacBook Pro.</div>

- The screen bezels are rather thick, even compared to the 16" and could use
some slimming.

- More TB ports. The air has two Thunderbolt ports, on only *one* side of the
laptop. I use hubs, so I don't usually require more than the two ports, but
it can be an issue to only have them on one side depending on where I want to
place my laptop. Having one port on either side wouldn't solve the issue
either, because I wouldn't like wrapping the power cord all the way around to
the other port when my hub is plugged in. The only *true* solution is to have
more than 2 TB ports, split across both sides of the laptop, *even if* you
don't need them all at the same time.

- Some applications are still tricky to install. For example, I had to
compile `neofetch` in `homebrew` (which was simple enough to do). I imagine
this issue should resolve with time. Overall though, I haven't really had any
major installation issues.

## What's... Different?

<a href="../../img/posts/m1-air-initial-thoughts/keyboard.jpeg"><img alt="The M1 Air Keyboard" src="../../img/posts/m1-air-initial-thoughts/keyboard.jpeg" style="max-width: 100%;"/></a>
<div class="caption">The MacBook Air does not have a touchbar</div>

There were a few things that we neither good nor bad, just *different* coming
from an Intel 16" MBP:

- The Efficiency cores are weird at first. I would look at my CPU usage when
only running background tasks and wonder why the first four cores had such
high usage, especially when compared to the other four. Eventually I
realized, it was because the tasks were running mostly using the efficiency
cores. So while it *looked* like there was a heavy load that it wasn't being
properly balanced across the cores... the work was actually shifted to be
more efficient. This is the desired functionality, but weird to get used to
at first if you're someone that is constantly watching CPU usage like I to.

- Surprisingly, not having the touch bar. Not that I *miss* it, but I
apparently got used to checking the time there and had to slowly break that
habit.

- The smaller screen space. I got used to the smaller screen quicker than I
anticipated, and I think the trade-off is worth it for the portability of
this laptop. But it is different.

- I miss the speakers on the 16". The air has *great* speakers... but the 16"
had *amazing* speakers. Like the screen resolution, this is mostly a physical
size limitation, and I think the trade-off is well worth it here as well.


## Conclusions

<a href="../../img/posts/m1-air-initial-thoughts/laptop_coffee.jpeg"><img alt="The M1 Air with Coffee" src="../../img/posts/m1-air-initial-thoughts/laptop_coffee.jpeg" style="max-width: 100%;"/></a>
<div class="caption">The MacBook Air with my coffee</div>

This laptop has been remarkable. It reminds me of some of my previous
*portable* laptops, like the x230 thinkpad and my x201e. That is a good thing.
*I
loved both of those computers and their ability to be thrown in a bag on the
go. It is a setup that pairs nicely with a powerful workstation, which [I
currently have](/post/selecting-charmeleons-upgrades/). While the air has
about the same footprint as both of those previous laptops, it is thinner,
has more screen space, and is
*magnitudes* more powerful. I can't complain with that.
