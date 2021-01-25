+++
title   = "Automatically Create and Run Podman Container Using Systemd"
date    = "2021-01-30"
author  = "Ryan Himmelwright"
image   = "img/posts/create-podman-systemd-services/moss_tree_header1.jpeg"
caption = "Emerald Outback, Beech Mountain, NC"
tags    = ["linux", "podman", "containers", "systemd"]
draft   = "True"
Comments = "True"
+++

No, this isn't the same thing as the last post, although it build off of it.
Basically, while that solution works for many cases... it didn't for my
jellyfin server. It seems like I've been 

<!--more-->

## The Issue
- The container would eventually break, causing it not to startup. 
- THis happened more often then I wanted, and it was a pain to regenerate the service each time

##  A Different Approach
- I knew the container worked each time if it was newly created each time, as I use to use the `--rm` flag when I started it manually..
- I wondered if I could write my own systemd service file using the *run* command, to both create and start a *new* container on boot up, instead of starting a persistent one...


## Another Short Post...
- To just test out the theory, I decided to start by editing the file I made in the previous post using `podman generate`, and go from there...
- However, I never had to go anywhere else. It seens to have been working ever since... So yea, another short post thanks to `podman`...