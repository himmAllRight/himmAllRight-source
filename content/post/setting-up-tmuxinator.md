+++
title  = "Setting up Tmuxinator"
date   = "2019-05-22"
author = "Ryan Himmelwright"
image  = "img/posts/setting-up-tmuxinator/mountain-trees.jpg"
caption= "Port Angeles, WA"
tags   = ["Linux", "Dev", "Dotfiles", "Customization", "Shell",]
draft  = "True"
Comments = "True"
+++

Several weeks ago, I wrote about [scripting tmux session
startups](/post/scripting-tmux-workspaces/). At the end of the post, I stated
that while writing the post, I had learned about [tmuxinator](https://github.com/tmuxinator/tmuxinator) and even teased
that I might be writing about setting up *that* rather soon. Well... I was
right. I've scrapped my tmux shell scripts, and have converted to using
tmuxinator. Here's how.

<!--more-->

## What is Tmuxinator?
[Tmuxinator](https://github.com/tmuxinator/tmuxinator) is a command line
application that makes it easy to create and manage tmux sessions. It lets a
user define how to setup a session, including name windows, splitting panes,
and what commands are run in each pane. The configuration is done in yaml, so
it is very easy to get started.

## Install
Most repos probably have `tmuxinator` in their offical repos. These days, I
mostly use Fedora on all of my machines and I was able to find it there. So to
install on Fedora:

```shell
sudo dnf install termixinator
```

Alternatively, it can be installed using the method on the project's Github
page:

```shell
gem install tmuxinator
```


## Create
To create a new tmuxinator profile, pass the desired session name to `tmuxinator new`:

```sh
tmuxinator new Website
```

This will open up a new tmuxinator template inside your default editor. The
default template contains a bunch of comments that help guide how to configure
one.


#### Header

The first thing to set is the `name` field at the top of the template, followed
by the `root` directory. The `root` will be the directory which all of the
windows/panes open up in by default. For example, when converting my website
script, I set the name to `Website` and `root` to the location where I keep my
website's git working directory, `~/Documents/himmAllRight-source`:

```yaml
# /home/ryan/.config/tmuxinator/Website.yml

name: Website
root: ~/Documents/himmAllRight-source
```

#### Windows

Next, I needed to configure my windows. To convert the script from my previous
post, I wanted a dedicated 'Main' window, one for the server, one for vim, and
one for an extra shell. Additionally, since my last post I added a window that
starts up my locally server website in a web browser. To recreate *all* that
with tmuxinator:

```yaml
windows:
  - Main:
      - zsh
      - clear
  - Server: hugo serve -D -F
  - Write: nvim
  - Shell: zsh; clear
  - Web: qutebrowser localhost:1313
```

Done. See the benefit? Save the file and that's it!

#### (also) Pane splits

While I don't use them for this configuration, it should be noted that setting
up pane splits is also quite easy with tmuxinator.

**PANE SPLIT EXAMPLE**

## Launch

<a href='../../img/posts/setting-up-tmuxinator/start-website-tmuxinator.gif'>
<img alt="Launching Website tmux session with tmuxinator" src="../../img/posts/setting-up-tmuxinator/starting-website-tmuxinator.png" onmouseover="this.src='../../img/posts/setting-up-tmuxinator/start-website-tmuxinator.gif'" onmouseout="this.src='../../img/posts/setting-up-tmuxinator/starting-website-tmuxinator.png'" style="max-width: 100%;"/>
</a>
<div class="caption">Launching website tmux session with tmuxinator</div>

To start up the newly defined tmux session with tmuxinator, use `tmuxinator
start`:

```sh
tmuxinator start Website
```


## Manage
All of the tmuxinator profile templates are stored at `~/.config/tmuxinator`,
which means they can easily be copied to a new machine, or even
saved/maintained in source control.

## Conclusion
