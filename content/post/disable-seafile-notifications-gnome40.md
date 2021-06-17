+++
title   = "Disable Seafile Notifications on Gnome 40"
date    = "2021-06-17"
author  = "Ryan Himmelwright"
image   = "img/posts/disable-seafile-notifications-gnome40/the-dunes-sound-header.jpeg"
caption = "Jockey's Ridge Stage Park, Nags Head, NC"
tags    = ["Linux", "seafile", "Gnome", "Fedora", "obsidian"]
draft   = "False"
Comments = "True"
+++

Quick post here. Basically, I keep figuring out and then forgetting how to
disable Seafile notifications on Gnome, because it doesn't allow tray icons.
This time, I'm recording the process.

<!--more-->

## Background

First, why do I need to disable *Seafile* notifications specifically?  Because I
sync my [obsidian](https://obsidian.md) vaults using
[Seafile](/post/trying-out-seafile/). While this sync method 
works wonderfully, it unfortunately has the side effect of whenever I type
in obsidian, seafile... uh... *politely notifies me*... that it has synced my
changing notes. Which is incredibly annoying, to say the least. 

However, I don't want to solve the problem by simply disabling *all* system
notifications. Luckily, seafile has a setting to do this... if you can get to
it.

### Install Tray Icons: Reloaded extension

<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/install-extension.png"><img alt="Installing the gnome extension" src="../../img/posts/disable-seafile-notifications-gnome40/install-extension.png" style="max-width: 100%;"/></a>
<div class="caption">Installing 'Tray Icons: Reloaded' from the Gnome extensions website</div>
</center>

The first step is to install an extension that allows application tray icons.
One such extension that seems to "work" currently (with a catch, more on that
below), is [Tray Icons:
Reloaded](https://extensions.gnome.org/extension/2890/tray-icons-reloaded/). So,
to install it, open up the page in
[Firefox](https://www.mozilla.org/en-US/firefox/new/?redirect_source=firefox-com),
and click the slider tab on the top right of the page, to switch it from `OFF` to `ON`.

*Note: If this is the first extension being installed, Firefox may ask you to
install a plugin. This is normal. Just hit accept and it will do it for you.*


### (Optionally) Install Gnome Extensions app

<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/install-gnome-extensions.png"><img alt="Installing gnome-extensions app" src="../../img/posts/disable-seafile-notifications-gnome40/install-gnome-extensions.png" style="max-width: 100%;"/></a>
<div class="caption">Installing the Gnome extensions app</div>
</center>

Next, while possibly optional, it is ideal to have the *Gnome Extensions* app
installed. So, open up Software Center, and install it from there. 
Alternatively, install it as a flatpak from the command line:

```bash
sudo flatpak install org.gnome.Extensions
```

This app allows you to configure and enable gnome extensions. With Gnome
Extensions opened, make sure `Tray Icons: Reloaded` is turned on. *Note, icons
likely won't show up yet, even with the extension enabled*.

### Switch to an Xorg Session 

<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/switch-to-xorg.png"><img alt="Swithing to Xorg Session" src="../../img/posts/disable-seafile-notifications-gnome40/switch-to-xorg.png" style="max-width: 100%;"/></a>
<div class="caption">Switching to Xorg Session</div>
</center>

This is the step I always forget (and hence why I'm writing this post). While
`Top Icons: Reloaded` "works" in Gnome 40... it only does in Xorg sessions. So,
log out, switch the session to `GNOME on Xorg` (gear icon at the bottom right of
the login screen), and log back in. Once logged in, the top icons extension should now work, *hopefully* displaying the Seafile icon (assuming
`seafile-client` is running).


### Edit the Seafile Settings
<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/seafile-icon-select-settings.png"><img alt="Accessing seafile settings from toolbar icon" src="../../img/posts/disable-seafile-notifications-gnome40/seafile-icon-select-settings.png" style="max-width: 100%;"/></a>
<div class="caption">Accessing seafile settings from toolbar icon.</div>
</center>

To open up the Seafile settings, right click on the icon and select `Settings`.

<center>
<a href="../../img/posts/disable-seafile-notifications-gnome40/seafile-settings.png"><img alt="Changing notification setting" src="../../img/posts/disable-seafile-notifications-gnome40/seafile-settings.png" style="max-width: 100%;"/></a>
<div class="caption">Changing notification setting</div>
</center>

From there, notifications can be **disabled** by **unchecking** the `Notify when libraries are synchronized` checkbox. Hit `OK`, and that's it. Feel free to log out and back in under a `Wayland` 🙂.

## Conclusion

Short post, but I forgot how to do this simple process twice now, so I wrote it.
Hopefully this helps that *one* other person also experiencing this issue, or at
least a few more that are confused for similar reasons. Enjoy! 