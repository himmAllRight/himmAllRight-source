+++
title   = "Disable Seafile Notifications on Gnome 40"
date    = "2021-06-16"
author  = "Ryan Himmelwright"
image   = "img/posts/disable-seafile-notifications-gnome40/the-dunes-sound-header.jpeg"
caption = "Jockey's Ridge Stage Park, Nags Head, NC"
tags    = ["Linux", "seafile", "Gnome"]
draft   = "True"
Comments = "True"
+++

This should be a short and quick post. Basically, I have had issues figuring out
and then remembering how to disable Seafile notifications when setting up Gnome
on an machine, because of how they hide desktop icons. I need to disable this
now, because I sync my obsidian with Seafile, so it constantly sends
notifications when I'm writing notes otherwise. Because I'm apt to forget my
work-around, I'll document it in a post even though it's a unique case.

<!--more-->

### Install Tray Icons: Reloaded extension

<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/install-extension.png"><img alt="Installing the gnome extension" src="../../img/posts/disable-seafile-notifications-gnome40/install-extension.png" style="max-width: 100%;"/></a>
<div class="caption">Installing 'Tray Icons: Reloaded' from Gnome extensions website</div>
</center>

The first step is to install an extension that allows application tray icons.
One extenstion that seems to "work" as of now (with a catch, more on that
below), is [Tray Icons: Reloaded](https://extensions.gnome.org/extension/2890/tray-icons-reloaded/). 


### (Optionally) Install Gnome Extensions app

<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/install-gnome-extensions.png"><img alt="Installing gnome-extensions app" src="../../img/posts/disable-seafile-notifications-gnome40/install-gnome-extensions.png" style="max-width: 100%;"/></a>
<div class="caption">Installing the Gnome extensions app</div>
</center>


### Switch to an Xorg Session 

<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/switch-to-xorg.png"><img alt="Swithing to Xorg Session" src="../../img/posts/disable-seafile-notifications-gnome40/switch-to-xorg.png" style="max-width: 100%;"/></a>
<div class="caption">Switching to Xorg Session</div>
</center>

(this is the step I always forget)


### Use the now visible Seafile desktop icon to open it's settings, and disable the notifications

<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/seafile-icon-select-settings.png"><img alt="Accessing seafile settings from toolbar icon" src="../../img/posts/disable-seafile-notifications-gnome40/seafile-icon-select-settings.png" style="max-width: 100%;"/></a>
<div class="caption">Accessing seafile settings from toolbar icon.</div>
</center>

### Seafile Settings

*Screenshot of un-checking setting*
<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/seafile-settings.png"><img alt="Changing notification setting" src="../../img/posts/disable-seafile-notifications-gnome40/seafile-settings.png" style="max-width: 100%;"/></a>
<div class="caption">Changing notification setting</div>
</center>

## Conclusion