+++
title   = "My new Ergox-EZ Keyboard -- Initial Thoughts"
date    = "2020-11-23"
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
of the board, to my laptop's usb port. I set down the wrists, rests and acted
tweaked the tenting poles to some arbitrary position, as if I knew what I was
doing. That was it. At that point, I was able to type... *stuff*... into my
computer.

### Initial Layout Changes

<a href="../../img/posts/ergodox-ez-initial-review/ergodox_defalut_layout.png"><img alt="The ergodox default layout" src="../../img/posts/ergodox-ez-initial-review/ergodox_default_layout.png" style="max-width: 100%;"/></a>
<div class="caption">The default ergodox layout</div>

I say *stuff*, because I wasn't able to truely pick up the board, adjust to the
layout in 20 seconds, and feel 100% comfortable like one might with a "normal"
keyboard. There was definately a learning curve I knew I would have to face
(more on that later). However, the immediate impediment was that I didn't even
know what the default layout of the board was. The back-lit QWERTY keys were
labeled, but all of the modifier keys on the sides and in the thumb clusters
were not. So, I navigated to the [oryx
configurator](https://ergodox-ez.com/pages/oryx) on the erogox-ez website with
two goals in mind:

* To learn the standard layout that the board shipped with was, and
* To make any initial changes to the layout I *knew* I would want (ctrl in caps
    lock location, for example)

After a few minutes of scanning the layout, and adding a tweak here and there,
I had my first layout to flash to the board. So I downloaded the file... and
hit the one issue I've experienced with the ergodox...

### Some issues with Wally

<a href="../../img/posts/ergodox-ez-initial-review/ergodox_macbook.jpeg"><img alt="Using the ergodox with my Macbook Pro" src="../../img/posts/ergodox-ez-initial-review/ergodox_macbook.jpeg" style="max-width:
100%;"/></a>
<div class="caption">Using the ergodox-ez with my MacBook Pro</div>

While I was able to flash the firmware using my macbook, for some reason my
Fedora laptops and desktops had issues at first. I would open up
[wally](https://ergodox-ez.com/pages/wally) (ZSA's firmware flashing tool), load the
firmware file, and press the tiny 'reset' button on my keyboard with a
paperclip... and it would freeze. The backlights would stop their magical
dancing, key presses rendered no response, and I would just wait. The only way
to get the board to respond again was to unplug and replug it back in.

I had heard that ZSA had good support, so I shot them and email about my issue.
They responded right away and helped me try to debug what might be happening.
It appeared to be some sort of permissions issues, although to this day I'm not
100% sure what it actually was. Eventually, it started working. Since then I
have updated most of my computers to Fedora 33, and I use a newer version of
Wally and it seems to work out of the box.

Oh well, problem resolved I guess. My main takeaways from it were that wally
deffinately requires `sudo`, and the ZSA's customer support really is great.
Oh, and that [open source firmware](https://github.com/zsa/wally) is awesome,
but I already knew that.

(ZSA has since updated the Linux README instructions to contain the udev
instructions they gave me)


## Getting used to and learning the board

- When I got it I did a fair bit of typing practice
- Within a few days, I was at a passable typing speed, and a few more and I was
    at a decent speed.
- I haven't been doing any typing practice the last few weeks and some of my
    bad habits have crept in.
- I'm not sure if I'm *faster* than on my old keyboard, but it is much more
    pleasent to type on, even when going faster (I could really only *burst*
    speed type on the HHKB because of my poor form).
- I want to start practicing again (Doesn't zsh have a typing trainer? If so
    link here)

## What I like

### Customizeability
Going to break this into two paragraphs, or maybe two sub sections if each
item needs more than a single para

#### Firmware

<a href="../../img/posts/ergodox-ez-initial-review/ergodox_layout.png"><img alt="Ergodox layout" src="../../img/posts/ergodox-ez-initial-review/ergodox_layout.png" style="max-width: 100%;"/></a>
<div class="caption">One of my custom layer layouts</div>

- I've already hinted about the ability to customize the layouts and I have
    done so.
- Tweaking it has slowed down, but even today I realized I wanted a key on one
    of my layers so I popped open the tools, and had the fix in about a minute.
- It sort of reminds me of when I use to use vanilla arch linux. You can go
    weeks and think you have everything installed and then all of sudden, you
    realize your missing a key, or it could be better positioned in the layers.
    - For example, last week while clipping a video, I noticed that I didn't
        think I had a 'delete' key. So I added one. Done.

#### Hardware

<a href="../../img/posts/ergodox-ez-initial-review/key_switches.jpeg"><img alt="Key switches" src="../../img/posts/ergodox-ez-initial-review/key_switches.jpeg" style="max-width:
100%;"/></a>
<div class="caption">I like that I can customize the hardware, including
hot-swapping out the switches</div>

- In addition to the firmware, It's nice to know the extent to what I can
    *physically* change about my keyboard.
- I've looked around at some of the parts I could tweak on my board in a year
    or two if I want to mix things up (without actually getting a different
    board).
- I wouldn't be against possibly swapping to mx clears for example. The main
    issue is the backglow lights shouldn't shine through then...
    - Which isn't that big of an issue though, because many of the alternative
        keycaps I like are solid (link?)
- Despite talking about all the hardware upgrades I can make, I actually like
it's current configuration. I love the board as it is, and am in no rush to
swap everything out. I *love* that I can though.


### Ortholinear

While it was more difficult to get used to than I expected, I have found using
an orthlinear layout to be *so* much easier to type on. My fingers don't fight
and trip over each other like Black-Friday shoppers trying to grab the last
hot-ticket item in the store. It broke me, really. I
wish it would become a standard option when buying laptops: ISO or ANSI, Ortho
or Staggard? Unfortunately I don't see that happening anytime soon.

### Split Design

<a href="../../img/posts/ergodox-ez-initial-review/laptop_stand.jpeg"><img alt="Ergodox around a laptop stand" src="../../img/posts/ergodox-ez-initial-review/laptop_stand.jpeg" style="max-width:
100%;"/></a>
<div class="caption">A split design keyboard pairs nicely with a laptop stand.</div>

Having a split keyboard, specifically one that is completely split, is so nice
from an ergonimic use. I can basically lay my arms on my desk in whichever way
is most comfortable... and move my keyboard to match it.

Additionally, the split design allows it to pair nicely with laptop stands, as
I can have them sit closer to me, which helps with the smaller screen.

### Thumb keys
<a href="../../img/posts/ergodox-ez-initial-review/ergodox_wood.jpeg"><img alt="ergodox on wood desk" src="../../img/posts/ergodox-ez-initial-review/ergodox_wood.jpeg" style="max-width:
100%;"/></a>
<div class="caption">The thumb cluster of keys has allowed me to better utilize my thumbs, which has been a nice change</div>


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

ZSA Trainer

### Cost

It is expensive, especially for a unique board you might hate. That being said,
if the ergodox works for you, it actually isn't that bad of a deal. While
expensive, the ergodox-ez is a solid board, with the ability to customize both
it's hardware and firmware to fit your needs over a span of many years. When
compared to other 'ergonomic' keyboards, it isn't really even priced that bad.


### It's difficult to switch back to my HHKB...

Laptop keyboards are fine. For whatever reason however... my HHKB feels so
squished.

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
