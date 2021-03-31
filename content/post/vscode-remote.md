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

<center>
<video style="max-width:100%;" controls>
  <source src="../../img/posts/remote-vscode/install_remote_vscode.webm" type="video/webm">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
<div id="caption">Installing the Remote Development Plugin</id>
</center>

Next, to instal the plugin, click the Extensions tab in the side bar (The
icon with four squares). From there, search for the extension by using
something like 'remote development' as the search term. The `Remote
Development` extension should appear in the list. Select it.

This extension is actually a package that bundles three extensions: `Remote -
SSH`, `Remote - WSL`, and `Remote - Containers`. Optionally, you can install
just the one you need.


## Connect to Server/ Accept config

<center>
<video style="max-width:100%;" controls>
  <source src="../../img/posts/remote-vscode/remote_vscode_config.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
<div id="caption">Connecting to a remote machine in vs code</id>
</center>

With the remote plugin installed, lets connect to a remote machine. I mostly
connect usign `ssh`, so make sure you have ssh keys shared with whatever
device you want to remote to.

<center>
<a href="../../img/posts/remote-vscode/remote_window_status.png"><img alt="Remote Window connected status" src="../../img/posts/remote-vscode/remote_window_status.png" style="max-width: 100%;"/></a>
<div class="caption">The connected status is displayed in the lower left of the window (top window: remote, bottom: local)</div>
</center>

When connecting to a remote machine, VS code will usually pop open a new
window, with ip address of the machine the window is connected to in the
lower left corner.

## Working on Projects, Remotely

<center>
<a href="../../img/posts/remote-vscode/open_remote_dir.png"><img alt="Opening a remote dir" src="../../img/posts/remote-vscode/open_remote_dir.png" style="max-width: 100%;"/></a>
<div class="caption">Opening a directory in the remote window</div>
</center>

When working in a remote VS Code window, everything is piped through from the
remote machine, as if you were sitting down at that machine. When opening a new file or folder, you browse the contents on that remote machine, not the local.

Even the built in terminal, runs on the remote machine. I still usually work
in `tmux` containers, so I usually have the vscode terminal attach the `tmux`
session for whatever project I'm working on. This allows me the flexibility
to pickup where I left off, or easily switch to another terminal window
and/or entirely different machine. Combining `tmux` with ther VScode remote
plugin provides me the convenience of a full IDE window, with the flexability
of running a `vim` + `tmux`. 

<center>
<a href="../../img/posts/remote-vscode/working_remote_window.png"><img alt="Working on a post in vs code with vim and tmux opened in the shell" src="../../img/posts/remote-vscode/working_remote_window.png" style="max-width: 100%;"/></a>
<div class="caption">Working on this post, with `vim` opened in `tmux` in the built-in terminal</div>
</center>

And yes... you can also run `vim`, *inside* `tmux`, *in* VScode's built-in
terminal, *in* a VScode remote window. This is something I actually do quite
often XD.


## Conclusion

I am almost always working *from* a different machine machine than the one my
files or work are on. While more traditional remote setups still work, I find
*pairing* them with VS Code really provides me with the best of both worlds. I
*get all the benefits of my tmux setup, with the ability to use the great git
*and syntax plugins VS Code offers.


Sitting in front a gruvbox-themed VSCode window, connected to my desktop, and
typing still using vim keybindings (via a vim plugin) seems to have become my
new default, no matter what computer (or VM) I am working from. I love it.