+++
title  = "Playing with Stratis"
date   = "2018-12-29"
author = "Ryan Himmelwright"
image  = "img/header-images/liberty-brick-lock.jpg"
caption= "Liberty Warehouse Apartments, Durham, NC"
tags   = ["Linux", "Homelab", "Filesystems"]
draft  = "True"
Comments = "True"
+++

While I have loved using ZFS for my server's filesystem over the last few years... I haven't always
loved using it on Linux. While Ubuntu has decided to just bite the bullet and distribute with ZFS
modules, Red Hat based distros aren't as keen to follow. With the Stratis Project now passed the
1.0 release and in full development, I don't think ZFS is coming to RHEL systems anytime soon. So I
decided to check out where stratis is, and get a taste of what the future might hold.

<!--more-->

I first heard of stratis (at least at a level where I took note to check it out, I may have heard
about it before) while listening to to [Linux Unplugged](https://linuxunplugged.com/270) on my
drive back to Durham from Raleigh
