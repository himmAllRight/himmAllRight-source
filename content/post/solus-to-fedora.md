+++
title  = "Migrating from Solus to Fedora for now"
date   = "2017-07-25"
author = "Ryan Himmelwright"
image  = "img/posts/solus-to-fedora/fedora26-upgrade-header.png"
tags   = ["Linux", "Fedora", "KDE", "Solus",]
+++

For awhile, I have been debating the idea of switching back to Fedora (from Solus). At least on my [main computer](/pages/homelab/#alakazam). First, let me state this right up front: I am still *very* satisfied with Solus. I think it is one of the best current Linux distros, and I want to still contribute to the project. However, there are a few reasons why Solus isn't the best fit for my needs *right now*, and I will highlight them below.

<!--more-->

### Why Switch
<center>
<img alt="Solus and Fedora Logos" src="../../img/posts/solus-to-fedora/logos.png"  style="max-width: 85%;"/>
</center>
*The Solus (Left) and Fedora (right) Project Logos*


The first phrase stated on the [Solus Project homepage](https://solus-project.com) is "Solus is an operating system that is designed for **home computing**." I find this to be true, and Solus does a great job at it. The Linux community needs a few good, focused, distros. While I have been using Solus for my "*home*" computing, the computing tasks I've focused on recently do not fall into the category of standard *home computing* use. Recently, my main top computing activities and goals are:

- Writing (okay... but still)
- Running all sorts of VMs
- Trying various Server Technologies
  - ZFS
  - KVM
  - Containerization Technologies (LXC, Docker, ...)
  - Ansible and other automation tools
  - Etc.
- Learning about Clustering
  - OpenMP
  - High Availability
  - Distributed File systems
- Trying to get involved with some other Open Source Projects
  - Fedora (Infrastructure, Dev)
  - NixOS

As you can see, many of the above items are not desktop based, but really
*server* based operations. Solus is *not* a server distribution, as it doesn't
*try* to be one. Which is a good thing. It is focused on its audience. I
just happen to not be in that audience at the moment.

Additionally, one of my goals for the near future is to transform my long-time Proxmox server into a [CentOS](https://www.centos.org/) box. Using Fedora on my main workstation does help me get accustom to that environment. It also allows me to more accurately test out ideas before I plan the big move.

Lastly, I had been eyeing up the Plasma desktop, and wanted to try that out again. At the time of writing this post, Solus doesn't fully support the Plasma desktop (yet). However, Fedora *does* have a [KDE Plasma Desktop Spin](https://spins.fedoraproject.org/kde/).


### The Switch

<center>
<img alt="Solus and Fedora Logos" src="../../img/posts/solus-to-fedora/fedora25.png"  style="max-width: 100%;"/>
</center>
*Screenfetch on my new Fedora Install*

I eventually (and somewhat sporadically), made the switch to Fedora. I switched
the week before the 26 release, so I decided to start with 25, and then upgrade
later (although I did test out 26 on my other laptop). This let me ensure that
the 26 issues were ironed out before upgrading. I also got to test out the `dnf`
system upgrade process. I recorded *post-switch* notes during the last few weeks
to document how everything went.

>"Well... I did it. I switched to Fedora on Alakazam yesterday. I went with the
>Fedora 25 KDE spin and did all of the hoops to get that up and going. Not only
>is it taking some time to get used to Fedora again, but I am needing to
>reacquaint myself with the KDE environment... it does seem different that other
>Plasma setups I've used in the past... But I like it."

I got used to it in no time:

>Alakazam is doing well on Fedora. I've been enjoying it and think I will stay on
>it.


### Updates

I ran some updates that I thought *might* be problematic, based
on [previous issues](/post/back-on-arch/#fedora) I've encountered with Fedora. I
made sure to note the results as well. The first notable update was from the
first time I updated the kernel, and the second was  upgrading from
Fedora 25 to 26. Both updates went very smoothly without any issues:

#### Kernel Upgrade

>So I am about to do my first Kernel update since being on Fedora again (on
>Alakazam). We'll see how the video drivers respond... To note, I am still on 25
>so it hopefully won't be too bad...

*...reboot...*

>No issues whatsoever :)


#### Upgrade to Fedora 26
<center>
<a href="../../img/posts/solus-to-fedora/fedora26-upgrade.png"><img alt="Solus and Fedora Logos" src="../../img/posts/solus-to-fedora/fedora26-upgrade.png" style="max-width: 100%;"/></a>
</center>
*I upgraded my Fedora 25 Plasma Install to Fedora 26*

Other than some odd issues with the GUI tool, the upgrade from 25 to 26 was
smooth and uneventful.

>I just upgraded Alakazam from Fedora 25 KDE, to Fedora 26 this morning. I couldn't really get the
>graphical installer to start, but that could be because I have several desktop environments setup
>(Plasma & Gnome), so it may have been confused (I was using the Gnome Software App in Plasma...)

>I just did the upgrade using the (command line) dnf upgrade tool, like I normally use, and it worked
>wonderfully. It even looks like my nvidia drivers stayed and my monitors were configured correctly
>after rebooting. The only difference is I don't seem to have the same Plasma animations I had
>before, but that is fine, and likely part of the update.


So that it. Those are my reasons for switching (for now), and the results of my
switch. I am still happy with Fedora, at least on Alakazam, and will likely
remain on it until I have a convincing reason to leave.
