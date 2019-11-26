+++
title  = "Setup Mosh"
date   = "2019-11-26"
author = "Ryan Himmelwright"
image  = "img/posts/setup-mosh/north-buchanan-boulevard.jpeg"
caption= "North Buchanan Boulevard, Durham, NC"
tags   = ["linux", "homelab", "ssh", "shell"]
draft  = "True"
Comments = "True"
+++

Ever since I [built my desktop](/post/charmeleon-desktop-design/), whenever I
am working on another, more portable machine, I find myself `ssh` back to the
desktop to work on it remotely. It has the power, and much of my work flow is
in a terminal window, so why not? The only issue I have with `ssh` is that if I
have a spotty internet connection, or if I sleep/suspend my computer while
moving around, my `ssh` session is terminated.
[Tmux](/post/scripting-tmux-workspaces/) and
[tmuxinator](/post/setting-up-tmuxinator/) make this not too much of an issue,
since I can re-attach my session, but I still wish my remote session could be a
bit more seamless. They can be... by using `mosh`.


<!--more-->

<!-- Just keeping this here for when I want to add an image eventually.


<a href="/img/posts/switching-to-bitwarden/bigtwarden-flathub.png">
<img alt="Bitwarden on Flathub Page" src="/img/posts/switching-to-bitwarden/bitwarden-flathub.png" style="max-width: 100%;"/></a>
<div class="caption">Bitwarden on Flathub</div>


-->

#### Mosh


#### Mosh Install

Mosh should be in most Linux repos, and is also available on macos or Windows.
For more information on how to install it on your platform, just head over to
the [getting mosh](https://mosh.org/#getting) page. For me, it was a simple
`dnf`/`yum` install to get it on both my laptop and server:

```
sudo dnf install mosh
```

#### Open Firewall Ports

After I installed `mosh`... it didn't work. That is because as usual, I forgot
to first open the required ports.

#### Connect


#### SSH Options


#### Conclusion
