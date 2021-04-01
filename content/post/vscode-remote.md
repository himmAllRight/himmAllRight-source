+++
title   = "Using Remote VSCode"
date    = "2021-03-31"
author  = "Ryan Himmelwright"
image   = "img/posts/remote-vscode/duke_campus_header.jpeg"
caption = "Duke University, Durham NC"
tags    = ["linux", "macos", "applications", "ssh"]
draft   = "True"
Comments = "True"
+++

I have previously stated that I mostly work on [my
desktop](/post/selecting-charmeleons-upgrades/), but usually *from* another
computer. For example, I work from my
[laptop](/post/m1-air-initial-thoughts/) most mornings. The most common
method I use for this has been combining `neovim` and `tmux` (with
[tmuxp](https://github.com/tmux-python/tmuxp), for ease). However, more 
often than not, I now find myself using [VS Code](https://code.visualstudio.com) with it's
[remote development
plugin](https://code.visualstudio.com/docs/remote/remote-overview). Here's
how.

<!--more-->

## Install the Remote Development Plugin

To get started, first make sure that VS code is installed on your machine.
This can be found on the project's [website](https://code.visualstudio.com),
or even as a [flathub
flatpak](https://flathub.org/apps/details/com.visualstudio.code)

<center>
<video style="max-width:100%;" controls>
  <source src="/img/posts/remote-vscode/install_remote_vscode.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
<div id="caption">Installing the Remote Development Plugin</id>
</center>

Next, to instal the plugin, click the Extensions tab in the side bar (The
icon with four squares). From there, search for the extension by using
something like 'remote development' as the search term. The `Remote
Development` extension should appear in the list. Select it, and click `Install`.

This extension is actually a package that bundles three extensions: `Remote -
SSH`, `Remote - WSL`, and `Remote - Containers`. Alternatively, you can just install the one you need.


## Connect to the Server

<center>
<video style="max-width:100%;" controls>
  <source src="/img/posts/remote-vscode/remote_vscode_config.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
<div id="caption">Connecting to a remote machine in vs code</id>
</center>

With the remote plugin installed, we can now connect to a remote machine. I
mostly do this using `ssh`. Make sure you first have ssh keys copied to the
device you want to link to. Then, open the command pallet (`CMD/CTRL-Shift-P`), and search for the `Remote-SSH: Connect to Host...` command to run.

This will prompt you for an ssh host to connect to. Just enter a `host` like
you would when using `ssh`. For example, `ryan@example.com`. If it's the first time adding a host, the plugin will ask where to keep the config file for all the hosts. I usually just select one of the defaults it offers me.

<center>
<a href="../../img/posts/remote-vscode/remote_window_status.png"><img alt="Remote Window connected status" src="../../img/posts/remote-vscode/remote_window_status.png" style="max-width: 100%;"/></a>
<div class="caption">The connected status is displayed in the lower left of the window (top window: remote, bottom: local)</div>
</center>

When connecting to a remote machine, VS code will usually pop open a new
window. To verify, the ip address of the machine the window is connected to
can be found in lower left corner.

## Working on Projects, Remotely

<center>
<a href="../../img/posts/remote-vscode/open_remote_dir.png"><img alt="Opening a remote dir" src="../../img/posts/remote-vscode/open_remote_dir.png" style="max-width: 100%;"/></a>
<div class="caption">Opening a directory in the remote window</div>
</center>

When working in a remote VS Code window, everything is piped through from the
remote machine, as if you were sitting down at that computer. When opening a
new file or folder, you browse the contents of the *remote filesystem*, not
the local one.

Even the built in terminal runs on the remote machine. I still work in
`tmux`, so I have my vscode terminal attach whatever `tmux` session I need.
This provides me with the flexibility to switch to a new machine, and to
pickup where I left off. Using this setup, I get a full graphical IDE window,
while still reaping the benefits of `vim` + `tmux`.

<center>
<a href="../../img/posts/remote-vscode/working_remote_window.png"><img alt="Working on a post in vs code with vim and tmux opened in the shell" src="../../img/posts/remote-vscode/working_remote_window.png" style="max-width: 100%;"/></a>
<div class="caption">Working on this post, with `vim` opened in `tmux` in the built-in terminal</div>
</center>

And yes... you *can* run `vim`, *inside* `tmux`, *in* VScode's built-in
terminal, *in* a VScode remote window. This is something I actually do quite
often XD.


## Conclusion

I am almost always working *from* a different machine than the one which my
files and work are on. This setup has been idea for how I work. It is easy to
use, yet very powerful.

Sitting in front a gruvbox-themed VSCode window, connected to my desktop, and
typing using vim keybindings (via a vim plugin) has become my new default, no
matter what computer (or VM) I am physically working from. I love it.