+++
title   = "Setting up NFS"
date    = "2021-04-18"
author  = "Ryan Himmelwright"
image   = "img/posts/setup-nfs/pocosin_lakes_wildlife_header.jpeg"
caption = "Pocosin Lakes Wildlife Refuge, NC"
tags    = ["linux", "filesystem", "homelab"]
draft   = "True"
Comments = "True"
+++

The thing I loved most about [upgrading my desktop] was that it enabled me to
run virtual machines using VFIO passthrough. Now, on a daily basis, I find
myself sitting in front for a virtualized Linux system. While this setup is
quite satisfying, it does come with a few complications. One such
complication is sharing files on the host with those VMs. After trying a few
methods, I determine that nfs was the simplest to get up ans going. Here's
how.

<!--more-->

## The Problem

*Screenshot of missing music error in VM lollypop? (Or large folder sizes?)*

My desktop is my main workstation. It is the hub that hold all of the files
and data I want to use, including documents, music, and videos. When I am working in a VM, I often want to access this data. For example, I may want to listen to music while I work.

However, it would be quite inefficient (both in time and disk space) to copy
all the files I wanted to each VM I used. So, setting up a network filesystem is ideal here. After trying a few methods, I eventually came to the conclusion that for my use (linux guests on a linux host), NFS worked. If you want to share with more Windows guests, something like samba might work better.


## Server Setup

The first thing we want to setup is the sever. Make sure to run the following
steups on the *host* machine.

### Install Dependencies

Being on a Fedora host, I was able to install the dependencies using the following `dnf` command:

```bash

```

### Define the Exports File

After we have everything installed, we want to create an *exports* file. This file will define all of our nfs shares we want to make available. Create and open the file `/etc/exports`, and add something similar for each directory you want to share:

```
/home/ryan/Seafile      10.0.7.0/24(rw,all_squash,insecure)
/home/ryan/Music        10.0.7.0/24(rw)
/Data/Videos            10.0.7.0/24(rw)
```

I like to share my Music and Video folders, along with my Seafile library (so
I don't have to set it up on each VM).

Each line breaks down as follows:

- The directory location to share (ex: `/home/ryan/Music`)
- The address space that are allowed to access the share (I use `10.0.7.0/24`, which allows any device on my home network)
- The properties fir each share in `()`. I use `rw` to allow read and write permissions.

That should be it. Feel free to dig deeper into all the nfs share settings if
you need them, especially if you need to be a bit more secure in your setup!

### Firewall/other permissions

After creating the exports file, we need to allow the service in the
firewall. To do so, permanently open the nfs service ports:

```

```

Don't forget to reload the firewall!

### Start the service?

Last but not least, make sure the nfs service is started and (optionially) enabled to autostart after a reboot.

## VM Client Setup



### Permissions?


### Mount


### (Optional) Add to FStab

## Conclusion