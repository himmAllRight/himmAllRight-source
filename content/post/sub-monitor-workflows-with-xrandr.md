+++
title  = "Creating \"Sub\"-Monitor Workflows Using xrandr"
date   = "2019-04-01"
author = "Ryan Himmelwright"
image  = "img/posts/switching-to-mesh-network/flower-tree-innovation-train.jpg"
caption= "American Tobacco Campus, Durham NC"
tags   = ["Homelab", "Hardware", "wifi",]
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


### Solution


### But Wait, There's More! Scripting it:
After running these commands to create and enable custom xrandr twice... I
realized it would be easy enough to automate. So I did with this script:

```bash
# add-xandr-.sh
# --------------
#!/bin/bash

# A function to prompt the user if they want to switch to the new mode now.
switch_to_new_mode () {
	echo -n "Switch to new mode now? [y/n]: "
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
	echo "Adding new mode [$modename] to display [$MONITOR]"
	xrandr --addmode $MONITOR $modename
	echo "Done!"
	switch_to_new_mode
}

# Message if the mode appears to already exist
mode_already_exists () {
	echo "Hmmm... I think that mode already exists. Verify the xrandr output for me?"
	echo "Don't worry. I'll print it in $ESLEEP seconds..."
	sleep $ESLEEP
	xrandr
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
	else
		mode_already_exists
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
### Conclusion

