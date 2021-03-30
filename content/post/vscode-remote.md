+++
title   = "Using Remote VSCode"
date    = "2021-03-31"
author  = "Ryan Himmelwright"
image   = "img/posts/jenkins-parallel-stashing/pennsburg_sky.jpeg"
caption = "Pennsburg, PA"
tags    = ["dev", "linux", "macos", "applications"]
draft   = "True"
Comments = "True"
+++

I have stated in previous posts that I usually work on [my
desktop](/post/selecting-charmeleons-upgrades/), but often from another
computer, like my [laptop](/post/m1-air-initial-thoughts/). The simpleest
method for this is usually combing neovim and tmux (and
[tmuxp](https://github.com/tmux-python/tmuxp) for ease), but more and more
often, I find myself using [vscode](https://code.visualstudio.com) with it's
[remote development
plugin](https://code.visualstudio.com/docs/remote/remote-overview). Here's
how.

<!--more-->

## Install remote plugin

First, make sure that VS code is installed on your machine. This can be found
on the project's [website](https://code.visualstudio.com), or even as a
[flatpak from
flathub](https://flathub.org/apps/details/com.visualstudio.code)

*Screen Capture/image installing package?*

Next, to instal the plugin, click the Extensions tab in the side bar (The
icon with four squares). From there, search for the extension by using
something like 'remote development' as the search term. The `Remote
Development` extension should appear in the list. Select it.

This extension is actually a package that bundles three extensions: `Remote -
SSH`, `Remote - WSL`, and `Remote - Containers`. Optionally, you can install
just the one you need.


## Connect to Server/ Accept config

With the remote plugin installed, lets connect to a remote machine. I mostly
connect usign `ssh`, so make sure you have ssh keys shared with whatever
device you want to remote to. 

## Working on Remote Projects


### Open remote window/dir


### Using the remote terminal

I still use tmux and sometimes vim still


## Conclusion

