+++
title  = "Reset Plasma 5 Monitor Configuration"
date   = "2018-11-14"
author = "Ryan Himmelwright"
image  = "img/header-images/nc-sun-in-trees1.jpg"
caption= "North Carolina Arboretum (Pisgah National Forest), Asheville, NC"
tags   = ["Hardware", "Monitors", "Linux", "KDE"]
draft  = false
Comments = "True"
+++

Extending a laptop's screen to an external display can often be a nightmare.
Sometimes, it might be best to just hit the reset button and configure from
scratch. With KDE Plasma 5, you can. Here's how.

<!--more-->

## Issue

While I love having a [dock-able laptop](../my-t470/) and [my 43" 4k LG
monitor](new-lgud4379b), getting them configured and agreeing with each other
can sometimes be a headache. Luckily, KDE Plasma 5 (the desktop environment
I've been using for awhile now) is fantastic and remembers previous display
configurations.

However, when I am playing around with resolutions or multiple inputs,
sometimes I set something that doesn't work... and it is remembered, causing
more problems.

## The Fix

Luckily, there is an easy fix: just delete the saved profile, and
re-setup the display again. However, I often forget these very simple steps...
hence, this post (and to help anyone else that needs it, of course :P).

#### Delete old profile

The first step is to delete the plasma profile that saves the screen settings.
Note, this may remove the profiles for *all* previously configured displays,
but I am okay with it for *my* use case.

```bash
cd ~/.local.share
rm -rf kscreen
```

#### Extend monitors when docked

<a href="../../img/posts/reset-plasma5-monitor-config/extended-monitor.png"><img alt="The KDE Plasma 5 extend display GUI" src="../../img/posts/reset-plasma5-monitor-config/extend-monitor.png" style="max-width: 100%;"/></a>
<div class="caption">The KDE Plasma 5 extend display GUI.</div>

After deleting the config, dock or reconnect the laptop to the display. A GUI
with extension layout options should pop up. If it does, select the preferred
layout option.

#### Close laptop lid (don't disable)

After extending the display, I usually try to make the monitor the primary
display and disable the laptop screen. This doesn't seem to work (It causes my
monitor to blank). However, I have learned that if I simply *close my laptop
lid* once it is connected... it does both of those things for me. I always
forget this... but now it's documented!

#### (Optional) Reset kscreen

After flipping around the displays so much, plasma shell may have gotten a bit
frazzled. If so, just reset it using the following command:

```bash
kquitapp5 plasmashell && kstart plasmashell
```

I like to execute this in krunner (alt-F2) so that it runs in the background,
and because I can usually still get to krunner, even if something goes terribly
wrong with plasmashell during the process.

## Conclusion

That's it. While this post is rather short (for once), hopefully it will be useful. Enjoy!
