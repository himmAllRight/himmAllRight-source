+++
title  = "Creating \"Sub\"-Monitor Workflows Using xrandr"
date   = "2019-04-22"
author = "Ryan Himmelwright"
image  = "img/header-images/ncsu-bridge1.jpg"
caption= "NC State Campus, Raleigh NC"
tags   = ["Homelab", "Hardware", "Monitors", "Linux",]
draft  = "False"
Comments = "True"
+++

A couple months ago, I swapped out my duel monitor setup for a single (but
massive), [42.5" UHD IPS display](/post/new-lgud4379b/). While I dicided that
the larger display was better than an ultrawide or 1440p monitor, I sometimes wish
that I had their more focused workspace, as sometimes mine gives me *too much*
space, which can actually be distracting, or inefficient.

<!--more-->

### Reasoning


### Problem 1: Scaling

To get "sub"-resolutions working, I had to fix two problems. The first was that
even if I select a smaller resolution on my computer, most monitors will
display that resolution, but scaled to the size of the display. For example, if
I set my computer to 1920x1080, by default it will display that, full-size on
my monitor, making eveything gigantic... the exact opposite of what I wanted.

After playing around in my monitor's input settings, I noticed that there is an
"Aspect Ratio" field, with a `1:1` option. When selected, the monitor displays
an image at its native resolution. So a 1920x1080 pixel display shows as a
smaller image, but with the monitor's native pixel density, in the center of my
screen. Problem #1 solved!

### Problem 2: New Resolution Sets

The second problem, is that by default many of the resolutions I want to try
out do not show up in my display settings. This makes sense, as *most* people
won't be selecting `21:9` resolutions on a `16:9` panel. So, I needed to add
new options using `xrandr`.

<< Image of Display Settings *Without* Custom Options >>

After playing around with `xrandr`, and some help from [this post](http://www.arunviswanathan.com/node/53), I was able to create new `xrandr` modes, and set my monitor to use them.

#### Creating a new xrandr mode

To create a new xrandr mode, I first need to calculate my first modeline. This
can be done by using the `gtf` tool. For example, to calculate a modeline for a
3440x1440 resolution at 59.9 hertz, use the following:

```bash
➜  ~ gtf 3440 1440 59.9

  # 3440x1440 @ 59.90 Hz (GTF) hsync: 89.25 kHz; pclk: 418.41 MHz
  Modeline "3440x1440_59.90"  418.41  3440 3688 4064 4688  1440 1441 1444 1490  -HSync +Vsync

➜  ~
```
The line that starts with *Modeline* (but *not including* "Modeline") is what
we want. Copy that and give it to `xrandr` to create a new mode:

```bash
xrandr --newmode "3440x1440_59.90"  418.41  3440 3688 4064 4688  1440 1441 1444 1490  -HSync +Vsync
```

Lastly, to add that mode to a display, use that same line but with the
`--addmode` flag, and the monitor to switch (`DP-1` in my case):

```bash
xrandr --addmode DP-1 "3440x1440_59.90"  418.41  3440 3688 4064 4688  1440 1441 1444 1490  -HSync +Vsync
```

*Note: To find the available monitor names, enter a plain `xrandr` command, and
it will spit out all the available outputs.*

#### Switching to the new mode
##### arandr
To switch to the new mode, I like to use the GUI tool, `arandr`.  Simply right
click on the display's rectangle, and select the new mode name from the
"Resolution" list (Or *Outputs* -> *Monitor Name* -> *Resolution* -> *New MODE
NAME* in the menubar).

<a href="/img/posts/sub-monitor-workflows-with-xrandr/arandr-select-newmode.png"><img alt="Using arandr to select new mode" src="/img/posts/sub-monitor-workflows-with-xrandr/arandr-select-newmode.png" style="max-width: 100%;"/></a>
<div class="caption">Using `arandr` to select new mode</div>

##### xrandr
If you are too [1337](https://en.wikipedia.org/wiki/Leet) to use a GUI app,
never fear! The display can be switched to the new mode using `xrandr` with the
`--output` and `--mode` flags:

```bash
xrandr --output DP-1 --mode "3440x1440_59.90"  418.41  3440 3688 4064 4688  1440 1441 1444 1490  -HSync +Vsync
```


### But Wait, There's More! Scripting it:
After running these commands to create and enable custom xrandr twice... I
realized it would be easy enough to automate. So I did with this script:

```bash
# add-xandr-.sh
# --------------
#!/bin/bash

# A function to prompt the user if they want to switch to the new mode now.
switch_to_new_mode () {
	echo -n "Switch to mode $modename now? [y/n]: "
	read change
	if [ "$change" == "y" ]
	then
		echo "switching monitor..."
		xrandr --output $MONITOR --mode $modename
	else
		echo "Okay, no switch. Enjoy!"
	fi
}

# Create a new mode for the display
create_new_mode () {
	echo "Adding new mode: $gtf_output"
	xrandr --newmode $gtf_output
	echo "Adding new mode $modename to display $MONITOR"
	xrandr --addmode $MONITOR $modename
	echo "Done!"
}

# Message if the mode appears to already exist
mode_already_exists () {
	echo "Hmmm... I think the mode $modename already exists."
}

## Main Function to set vars and code
main () {
	# Input Vars
	WIDTH=$1
	HEIGHT=$2
	MONITOR=$3
	ESLEEP=3
	# Fancier Vars :P
	gtf_output=$(gtf $WIDTH $HEIGHT 59.9 | grep -i "modeline" | sed -e 's/\<Modeline\>//g')
	modename=$(echo $gtf_output | grep -o  "\(\".*\"\)")
	modeexists=$(xrandr | grep -i $modename)

	# Run
	if [ "$modeexists" == "" ]
	then
		create_new_mode
	    switch_to_new_mode
	else
		mode_already_exists
	    switch_to_new_mode
	fi
}

## Execute Main
main "$@"
```

Basically, this script is run by providing it the desired width, height, and
`xrandr` display to apply the new mode to. For example, to create a new
`3440x1440` mode for my `DP-1` display, I would run the following command:

```bash
./add-xrandr.sh 3440 1440 DP-1.
```

Then, it will check to see if the mode already
exists. If it does, it will tell the user that it thinks the mode already
exists, and print output of the `xrandr` command for the user to check (after a
short delay). If the mode is not already detected, It will ask the user if they
wish to switch to the new mode right away, and will do it for them if they
respond "`y`".

### Pros/Cons

#### What this solves
- When I have the monitor set to a sub-resolution, I don't experience any of
    the "edge shadowing" issues I mentioned in the review post.
- I can test out any resolution setup less than UHD. (Including Ultrawide
    setups)
- Using a smaller resolution is friendlier to my tiling wm setups
- I can use a better "single focus" monitor setup, like the equivalent of a 28"
    1440p display.
- I can set my monitor to a smaller resolution to better play full screen games (so that
    the resolution better fits my gpu performance *and* so the game is in my
    field of view)

#### What it doesn't fix
- The *physical* size of my monitor stays the same. (MASSIVE Bezels :P )
- I can't really do multiple displays setups, even though my monitor supports
  multiple inputs and picture-by-picture (ex: I can't do a horizontal +
  vertical 1080p setup, even using pbp because it will center each one).
- The dpi is slightly bigger than if I got the *common* size/pixel monitors.
- Any *curving* or other physical attributes another monitor form factor has.
### Conclusion

