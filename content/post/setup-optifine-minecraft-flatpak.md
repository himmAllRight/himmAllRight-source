+++
title   = "Setup Optfine with Minecraft Flatpak Install"
date    = "2020-09-30"
author  = "Ryan Himmelwright"
image   = "img/posts/setup-optifine-minecraft-flatpak/obx-pier-post.jpeg"
caption = "Kitty Hawk, NC"
tags    = ["linux", "flatpak", "fedora",]
draft   = "True"
Comments = "True"
+++

Over last few months, I picked up Minecraft (Java) on my desktop again. After
[upgrading my graphics card](/post/rx580-upgrade), I wanted to start using
shaders. However, unlike when I was in college, these days I can install and
play minecraft as a [flatpak](http://flatpak.org). While using the flatpak
makes installing minecraft convenient, it also complicates installing a mod
like Optifine. So here's how to do it.

<!--more-->

*Note: Beforea we start, I have only done this on Fedora Linux. It is possible
that paths and locations may differ on other distros*.


### Install Minecraft Flatpak

*Image of Minecraft Flathub Page?*

First, lets install the minecraft flatpak. Ensure that [flathub is
enabled](https://flatpak.org/setup/Fedora/) and then run the following command
to install Minecraft:

```bash
flatpak install com.mojang.Minecraft
```

Open up the launcher, and login to verify that everything is working.

*(Logging into the official launcher at least once is required to install
Optifine in the later steps).*

### Optifine
#### Background info

[Optifine](https://optifine.net/home) is a Minecraft optimiziation mod which
supports installing shader and texture packs. These help minecraft look better,
but some can actually help the game *perform* better. I use shaders that render
some textures a bit more realistically from the default, but nothing too fancy.

#### Download

*Image of Optifine download page?*

To obtain optifine, go to the [download page](https://optifine.net/downloads)
and download the version which corresponds to the minecraft version you are
using. If you are running a version which is more recent, you might have to try
a *Preview version* of optifine, which in my experience, usually works fine.

### Install Optifine
#### Finding the minecraft folder
Before we install Optifine, there is one piece of information we need to know:
the `.minecraft` folder location. This is where running a flatpak verion
differs from a normal minecraft install, as the folder will not be at
`~/.minecraft/`.

This is because flatpak applications are sandboxed from the system. While good
for security, it means that the *'home directory'* seen inside the application
is different from the user's (it's like a `chroot`).

*Screenshot of my actual .minecraft folder?*

On my computer, the flatpak applications are located at `/home/ryan/.var/app/`,
making my `/home/ryan/.minecraft/` folder *actually* at
`/home/ryan/.var/app/com.mojang.Minecraft/data/minecraft/`. Find and remember
this location. *(Hint: it should be similar to mine)*

#### Install Optifine

*Image of install window, adding in custom minecraft folder location*

To install optifine which is a `jar` file, open a terminal, navigate to the
download, and run it with java:

```bash
cd ~/Downloads
java -jar preview_OptiFine_1.16.3_HD_U_G3_pre1.jar
```

This will open the installer.

<center>
<a href="/img/posts/setup-optifine-minecraft-flatpak/optifine_install.png">
<img alt="The optifine installer" src="/img/posts/setup-optifine-minecraft-flatpak/optifine_install.png" style="max-width: 100%;"/></a>
<div class="caption">The Optifine installer window</div>
</center>

Switch the folder to the `minecraft` one we found previously, and click
*Install*. Note: If the official minecraft launcher was not already logged
into, this step will *not* work as it will fail to find minecraft (the launcher
downloads content on the first login).

### Configure in Launcher

<center>
<a href="/img/posts/setup-optifine-minecraft-flatpak/select_optifine.png">
<img alt="The minecraft launcher, selecting optifine" src="/img/posts/setup-optifine-minecraft-flatpak/select_optifine.png" style="max-width: 100%;"/></a>
<div class="caption">Select Optifine in the Minecraft Launcher</div>
</center>

With Optifine installed, we need to configure it in the minecraft launcher. If
Optifine was correctly installed, it should now be a selectable option at the
bottom left of the window (Next to settings)

#### Add your own installation

<center>
<a href="/img/posts/setup-optifine-minecraft-flatpak/diy_launcher.png">
<img alt="Creating a new minecraft launcher install" src="/img/posts/setup-optifine-minecraft-flatpak/diy_launcher.png" style="max-width: 100%;"/></a>
<div class="caption">Select Optifine in the Minecraft Launcher</div>
</center>

If for some reason optifine *is not* an option, a custom installer can be
added. To create a new install, click *Installations* at the top of the
launcher, and hit the *New* button. From that window, give the install a name
and select your latest Optifine version from the drop-down menu. If optifine
isn't an option, then it wasn't installed correctly or in the right location.

Lastly, remember to switch the *Game Directory* to the location of the flatpak
minecraft directory we've been using. Hit *Create* and switch to it.

### Shaders

The main motivation behind the hassel to install Optifine, is to be able to use
shader (at least for me). So, with Optifine all configured, what's finish what
we came here for.

#### Download

First, obtain some shader. I've mostly been using the [BSL] shader pack and
loving them. They keep a more 'classic' minecraft style without changing too
much, but improve things like the lighting, water, and add swaying plants.

When you find a shader you want, just download the package and move it to the
*shaders* folder in our flatpak minecraft folder. [Here is]() where I
downloaded the one I use.

*FYI, not every shader I tried worked.*

### Enable in game

<center>
<a href="/img/posts/optifine-minecraft-flatpak/minecraft_video_settings.png">
<img alt="Minecraft Video Settings" src="/img/posts/setup-optifine-minecraft-flatpak/minecraft_video_settings.png" style="max-width: 100%;"/></a>
<div class="caption">Minecraft Video Settings</div>
</center>

With the shader package in place, we should be able to enable it in game. Fire
up minecraft (the optifine instal), and select *Options*, then the *Video
Settings*. From there, you should now see a newly available *Shaders* option.
Click it to open up the shaders menu.

<center>
<a href="/img/posts/optifine-minecraft-flatpak/minecraft_shader_settings.png">
<img alt="Minecraft Shader Settings" src="/img/posts/setup-optifine-minecraft-flatpak/minecraft_shader_settings.png" style="max-width: 100%;"/></a>
<div class="caption">Minecraft Shader Settings</div>
</center>

If the shader package was moved to the correct location, it *should* show up
here now. If so, select the desired shader (the laucher might restart when
a new shader isselected). If not, open the *Shaders Folder*
to double check the location.

After selecting the shader, hit *Done* and try it out in game!

### Conlusion

<center>
<a href="/img/posts/optifine-minecraft-flatpak/minecraft_with_shaders.png">
<img alt="Minecraft with Shaders" src="/img/posts/setup-optifine-minecraft-flatpak/minecraft_with_shaders.png" style="max-width: 100%;"/></a>
<div class="caption">Minecraft using the BLS Shaders</div>
</center>

Much better! Shaders bring playing minecraft up to a new level. While they
might seem difficult to use with a flatpak install, it really isn't bad *if*
you know (and remember) where to look. Enjoy!
