+++
title  = "Testing out Tarsnap"
date   = "2017-09-19"
author = "Ryan Himmelwright"
image  = "img/posts/back-to-solus/install-header.png"
tags   = ["Linux", "Solus", "Homelab",]
draft  = true
+++

Several months ago, I setup my [encrypted external hard drive ZFS backup system](../zfs-backups-to-luks-external/) and have continuted to use it for (somewhat) regular backups. More recently, I have started to quickly [spin up my own git repos](../creating-a-git-remote), whenever I want to version control a set of files I do not want publicly available (ex: passwords, config files, or TODO lists). While my external drive backup system works well for my *data*, I am not currently backing up my repos (besides them being distributed across my computers). So, I have started to look for a remote backup solution. Starting with [Tarsnap](https://www.tarsnap.com).

<!--more-->

I first heard of Tarsnap
