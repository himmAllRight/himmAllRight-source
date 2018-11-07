+++
title  = "Reset Plasma 5 Monitor Configuration"
date   = "2018-11-04"
author = "Ryan Himmelwright"
image  = "img/homelab/new_monitor4.jpg"
tags   = ["Hardware", "Monitors", "Linux", "KDE"]
draft  = true
Comments = "True"
+++

A quick post, but one that could be usefull since I have to do it often...

<!--more-->

## Issue


## The Fix

- Delete old profile

```bash
cd ~/.local.share
rm -rf kscreen
```

- Extend monitors when docked

- Close laptop lid (don't disable)

- (Optional) Reset kscreen

```bash
kquitapp5 plasmashell && kstart plasmashell
```
