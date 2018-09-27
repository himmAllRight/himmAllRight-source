+++
title  = "Fedora ZFS Updates"
date   = "2018-10-15"
author = "Ryan Himmelwright"
image  = "img/homelab/new_monitor4.jpg"
tags   = ["Linux", "ZFS", "Fedora", "Homelab",]
draft  = true
Comments = "True"
+++
                                                                                                                                                                                                                                                                                                So for several weeks now I've been using an encrypted ZFS pool for the main Data store on my main computer (similar setup to this guide). For the most part, things have been great. However... kernel updates can pose issues. So far, I what seems to be working best is what I found from [this post](https://github.com/zfsonlinux/zfs/issues/6902). So I don't have to keep skimming through this post and others, I am just going to record what I do to get it to work (and ideally confirm it with someone), and save it as a post on my own site here.
                                                                                                                                                                                                                                                                                                    - Rebooted into latest Kernel, and switched to another tty
- Tried to `modprobe zfs`. When it fails, procede to load it
- First, I did a `dkms status` to see if it was listed (it wasn't), but more importantly to see the version of spl (which my zfs usually matches)
- Then I made sure it was added with `dkms add -m zfs -v 0.7.11`, which it seemed like it was. However, it wasn't built, so...
- `dkms install -m zfs - 0.7.11`, and it compiled. Afterwards, I was able to `modprobe zfs`.
- I thought it still wasn't working, but then remembered I had to import my pool, so `zpool import Data`. It has issues with my libvirt and snapd datasets, but that's because the system generates them if not found I guess. It didn't matter for first log in.
- I logged in then and was able to get to my stuff (normally can't log in... which tips off the issue. This is because my `/home` is a mount point on the pool. When it can't import the pool, it can't find my home when logging in.)
- I rebooted to check it was working. It seems to be up agian.


I'll try to find more info on this, clean it up, confirm it with someone, and turn it into a post.
