+++
title   = "Setup Optfine with Minecraft Flatpak Install"
date    = "2020-09-20"
author  = "Ryan Himmelwright"
image   = "img/posts/setup-optifine-minecraft-flatpak/obx-pier-post.jpeg"
caption = "Kitty Hawk, NC"
tags    = ["linux", "flatpak", "fedora",]
draft   = "True"
Comments = "True"
+++

Over the last couple of months I have started playing Minecraft (Java) on my
desktop again. With my [graphics card update](), I wanted to start using some
shaders. Nothing fancy, but something to bring the game up to the next level.
However, unlike when I was in college, these days I can install and play
minecraft using a [flatpak](). This makes it convienient to install, but can
make figuring out how to install something like mods or Optifine a bit more
complicated. So here's how to do it.

<!--more-->

*Note: Beforea we start, I have only done this on Fedora Linux. It is possible
that paths and locations may differ on other distros*.


### Install Minecraft Flatpak

*Image of Minecraft Launcher?*

First, if minecraft isn't already installed as a flatpak, lets do that first.
Make sure [flathub is enabled]() and then run the following command to install
Minecraft:

```bash
flatpak install com.mojang.Minecraft
```

Open up the launcher, and login to verify that everything is working.

### Optifine
#### Background info

[Optifine]() is a Minecraft optimiziation mod which supports installing shader
and texture packs. These can either help minecraft look better, and some can
actually help the game perform better. I use shaders that help some of the
textures look a bit better from the default, but nothing too fancy.

#### Download

*Image of Optifine download page?*

To obtain optifine, go to the [download page](https://optifine.net/downloads)
and download the version which corresponds to the minecraft version you are
running. If you are running a version which is more recent, you might have to
run a *Preview version* of optifine, which in my experience is fine.

### Install Optifine
#### Finding the minecraft folder
Before we install Optifine, there is one bit of information we need to know for
the install process: the `.minecraft` folder location. This is where running a
flatpak verion differs from a normal minecraft install, as the folder will not
be at `~/.minecraft/`.

#### Install Optifine

### Configure in Launcher

### Shaders
#### Download

#### Move to Location

### Enable in game


### Conlusion
