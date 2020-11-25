+++
title   = "My new Ergox-EZ Keyboard -- Initial Thoughts"
date    = "2020-11-25"
author  = "Ryan Himmelwright"
image   = "img/posts/ergodox-ez-initial-review/ergodox_header.jpeg"
caption = "Durham, NC"
tags    = ["hardware", "keyboards", "hhkb", "ergodox",]
draft   = "True"
Comments = "True"
+++

Several weeks ago, I wrote about how I [decided to purchase an
ergodox-ez](/post/decided-to-get-an-ergodox/) split keyboard. However, in that
post I omitted any details about what configuration I ordered,
as well my impressions about the board. Now that I have been an
ergodox owner for... wow, almost two months now... I guess this post is
due. Here are my '*initial*' thoughts of the ergodox-ez...

<!--more-->


## Ordering and shipping

<a href="../../img/posts/ergodox-ez-initial-review/both_boxes.jpeg"><img alt="The Boxes my ergdox came in" src="../../img/posts/ergodox-ez-initial-review/both_boxes.jpeg" style="max-width:
100%;"/></a>
<div class="caption">The boxes my ergodox-ez shipped in</div>

First, what ergodox specifically did I order? After a few hours toggling the
configuration tool and tons of internal debating, I eventually settled on an
ergodox-ez *glow* (backlit keys), with a black body, and black printed (LED
Compatible) key caps.  With a narrowed selection of switch options (to maintain
backlit key compatibility), I landed on Cherry MX Browns as my best option. I
wanted a noticeable tactile bump, but didn't want "click-y" keys. I prefer a
lower "*Clack*", while typing and find the higher pitch of MX Blues annoying.
I decided that I might as well go all in with this keyboard, and ordered the
tenting poles and black wrist rests as well.

With all of my options decided, I placed my order and prepared myself to wait
in anticipated glee for... an average of 3 weeks shipping time ಠ_ಠ. *Luckily*,
I was fortunate and about a week later, I had a large, flat box show up at my
door!

<a href="../../img/posts/ergodox-ez-initial-review/ergodox_box_plastic.jpeg"><img alt="Opened the ergodox box" src="../../img/posts/ergodox-ez-initial-review/ergodox_box_plastic.jpeg" style="max-width: 100%;"/></a>
<div class="caption">Opening the main box</div>

Everything was very well packaged. The keyboard came in one box, and the wrist
rests had their own. The two boxes matched in width, so they could be shipped
as one. Lifting the lid on the larger box, I was greeted by the keyboard
looking back at me through a plastic panel, with it's accessories (cables, key
switch pulled, screws) neatly pinned around it.

## Setup

The initial *physical* setup was quite simple. I took everything out of the
box, connected the two haves of the board together with the included TRRS
cable, and then used the mini usb cable (also included) to connect right half
of the board to my laptop's usb port. I positoned the wrist-rests and tweaked
the tenting poles to some arbitrary position, acting as if I knew what I was
doing.  That was it. After that point, I was able to type... *stuff*... into my
computer.

### Initial Layout Changes

<a href="../../img/posts/ergodox-ez-initial-review/ergodox_defalut_layout.png"><img alt="The ergodox default layout" src="../../img/posts/ergodox-ez-initial-review/ergodox_default_layout.png" style="max-width: 100%;"/></a>
<div class="caption">The default ergodox layout</div>

I say *stuff*, because I wasn't able to just pick up the board, adjust to the
layout in 20 seconds, and feel 100% comfortable like one might with a "normal"
keyboard. There was definitely a learning curve (more on that later).  However,
the pressing barrier was that I didn't even know the default layout. The
back-lit QWERTY keys were labeled, but all of the modifier keys on the sides
and in the thumb clusters were not. So, I navigated online to the [oryx
configurator](https://ergodox-ez.com/pages/oryx) with two goals in mind:

* To learn the standard layout that the board shipped with was, and
* To make any initial changes to the layout I *knew* I would want (ctrl in the caps
    lock location, for example)

After a few minutes of scanning and tweaking, I had my first layout to flash.
So I downloaded the file... and hit the only true issue I've experienced with the
ergodox...

### Issues with Wally

<a href="../../img/posts/ergodox-ez-initial-review/ergodox_macbook.jpeg"><img alt="Using the ergodox with my Macbook Pro" src="../../img/posts/ergodox-ez-initial-review/ergodox_macbook.jpeg" style="max-width:
100%;"/></a>
<div class="caption">Using the ergodox-ez with my MacBook Pro</div>

While I was able to flash the firmware using my macbook, for some reason my
Fedora laptops and desktop had issues at first. I would open up
[wally](https://ergodox-ez.com/pages/wally) (ZSA's firmware flashing tool), load the
firmware file, and press the tiny 'reset' button on my keyboard with a
paperclip... and it would freeze. The backlights stopped their magical
dancing and key presses rendered no response. The only way
to get the board to respond again was to unplug and replug it back in.

I had heard that ZSA had good support, so I emailed them about my issue.
They responded right away and helped to debug what might be happening.
It appeared to be some sort of permissions issues, although to this day I'm not
100% sure what it actually was. Eventually, it started working. Since then I
have updated most of my computers to Fedora 33, and I use a newer version of
Wally. I haven't had the issue pop up again, even on fresh OS installs. It just
works.

Oh well, problem resolved I guess? My main takeaways from the experience were
that 1) wally definitely requires `sudo` permissions, and 2) the ZSA's customer
support is wonderful.  Oh, and [open source
firmware](https://github.com/zsa/wally)* is the best, but I already knew that.

(*ZSA has since updated the Linux README instructions to contain the udev
instructions they gave me)


## Getting used to and learning the board

As previously stated, I knew I would have to put some effort into learning how
to type on the ergodox. When I got it, I did a fair bit of
[typing](https://www.keybr.com) [practice](https://play.typeracer.com/) and
used it for work everyday. Within a few days, I was at a passable typing speed,
and after a few more and I was at a *decent* speed. I am not sure if I am any
*faster* than on my old keyboard, but I can type faster for much longer (I
could only burst speed type on the HHKB and start to cramp up, mostly due to
poor form).

<a href="../../img/posts/ergodox-ez-initial-review/oryx_trainer.png"><img alt="Oryx Training Tool" src="../../img/posts/ergodox-ez-initial-review/oryx_trainer.png" style="max-width: 100%;"/></a>
<div class="caption">Oryx Training Tool</div>

I haven't done any typing practice the last few weeks and I've started to
notice *some* of my bad habits have creeping back. I want to start practicing
again and might try to use the trainer that is included in the Oryx tool. It is
able to connect to the keyboard to show your layout, and provides several types
of content to type through (code, books, symbols). I might try to use to to
create an optimized coding layer where that has my most used symbols in easy to
reach places.

## What I like

### Customizability

This board is fully customizable on both the hardware *and* software side.

#### Firmware

<a href="../../img/posts/ergodox-ez-initial-review/ergodox_layout.png"><img alt="Ergodox layout" src="../../img/posts/ergodox-ez-initial-review/ergodox_layout.png" style="max-width: 100%;"/></a>
<div class="caption">One of my custom layer layouts</div>

Being able to tweak the layout of multiple layers means there are an endless
amount of ways I can tailor my keyboard to fit my needs. My tweaking it has
slowed down a bit, but I love that I can make quick changes to my layout if I
decide there is a better way to do something. For example, today I realized I wanted to add
a key on one of my alternate layers, so I popped open oryx and wally, and had
the change finished in about a minute.

Using open firmware reminds me of when I used vanilla arch linux. I would go
weeks assuming I had everything required for a typical desktop environment when
all of sudden, I would try to open a pdf and realize I never installed a pdf
reader... or a file browser. Last week while clipping a video, I noticed that
my ergodox layout didn't have a 'delete' key. So I quickly added one. Done.

#### Hardware

<a href="../../img/posts/ergodox-ez-initial-review/key_switches.jpeg"><img alt="Key switches" src="../../img/posts/ergodox-ez-initial-review/key_switches.jpeg" style="max-width:
100%;"/></a>
<div class="caption">Testing swapping out a switch with one from my switch
tester</div>

In addition to the firmware, It's nice to know that there is quite a bit I can
    *physically* change about my keyboard. Specifically, the key caps can be
    changed and the switches themselves are hot-swappable.


I've already looked around for some of the parts I could swap out on my board
in a few years I want to mix things up. I wouldn't be against swapping to mx
clear switches for example. The main issue is the back glow lights would not
shine through anymore. I guess that wouldn't be too big of an issue though,
because many of the alternative keycaps I like are solid.

*Anyway*... Despite talking about all the hardware upgrades I can make, I
actually do enjoy it's current configuration. But I do love that I change it
over time.


### Ortholinear

While it was more difficult to get used to than I expected, I have found using
an orthlinear layout to be considerably easier to type on. My fingers no longer
fight and trip over each other like Black-Friday shoppers trying to grab the
last hot-ticket item. The worst thing about using an ortholinear layout, is
that I want it to become a *standard* option when buying laptops: ISO or ANSI,
Ortho or Staggard? Unfortunately I don't see that happening anytime soon...

### Split Design

<a href="../../img/posts/ergodox-ez-initial-review/laptop_stand.jpeg"><img alt="Ergodox around a laptop stand" src="../../img/posts/ergodox-ez-initial-review/laptop_stand.jpeg" style="max-width:
100%;"/></a>
<div class="caption">A split design keyboard pairs nicely with a laptop stand.</div>

Like the ortholinear layout, having a split keyboard, particularly one that is
completely split in two, is a considerable ergonomic boost. I can lay my arms
on the desk in whichever way is most comfortable... and then position the keyboard
to match *them*.

As a bonus, the split design allows it to pair nicely with laptop stands,
allowing me to slide the stand closer, which helps with viewing the smaller
screen.

### Thumb cluster keys
<a href="../../img/posts/ergodox-ez-initial-review/ergodox_wood.jpeg"><img alt="ergodox on wood desk" src="../../img/posts/ergodox-ez-initial-review/ergodox_wood.jpeg" style="max-width:
100%;"/></a>
<div class="caption">The thumb cluster of keys has allowed me to better utilize my thumbs, which has been a nice change</div>

Another feature I immediately miss on other keyboards, is thumb keys. It is a
relief to allow my thumbs control more keys than just the spacebar. The thumb
clusters allow me to offload responsibility for backspace, tab, enter, delete,
and a few other keys from my weakest fingers (pinkies), to my strongest
(thumbs). While also tricky to get used to at first, this makes a huge
difference while typing, and is probably the biggest issue I have when
switching to a laptop keyboard from my ergodox (I find my self smashing the
spacebar when trying to backsapce or enter).


## What I don't love
There's honestly not I don't *like*, but here is a thing or two that I maybe
don't *love*..



### Learning curve

<center>
<a href="../../img/posts/ergodox-ez-initial-review/typing_test.png"><img alt="typing test results" src="../../img/posts/ergodox-ez-initial-review/typing_test.png" style="max-width: 100%;"/></a>
<div class="caption">One of my custom layer layouts</div>
</center>

The biggest con to getting a keyboard like the ergodox is the learning curve.
It isn't something you will be able to pick up and immediately start using. You
will have to sit down and play typing games daily to really start to feel
comfortable.


### Cost

It is expensive, especially for a unique board you might hate. That being said,
if the ergodox works for you, it actually isn't that bad of a deal. While
expensive, the ergodox-ez is a solid board, with the ability to customize both
it's hardware and firmware to fit your needs over a span of many years. When
compared to other 'ergonomic' keyboards, it isn't really even priced that bad.


### It's difficult to switch back to my HHKB...

Switching to my Laptop keyboards is mostly fine, but for whatever reason
however... my HHKB feels so squished. I'm sure if I dedicated a few hours to
using the HHKB this would go away, but I haven't done that yet.

## Conclusion

<a href="../../img/posts/ergodox-ez-initial-review/ergodox_office.jpeg"><img alt="The ergodox in my home office" src="../../img/posts/ergodox-ez-initial-review/ergodox_office.jpeg" style="max-width:
100%;"/></a>
<div class="caption">The ergodox-ez in my home office</div>

Overall, I love this keyboard and am very happy with my choice. Now that I am
used to it, I feels great to type on and I really don't have to think too much
about it. The Split design and ortholinear layout truly make it the most
natural feeling and comfortable board I have typed on, and my body thanks it.
Additionally, any little niggles I have with where a key is can be stomped out
with a 2 minute config change and flash, ensuring that I should *continue* to
love this board for years to come, even as my preferences and uses continue to
change.
