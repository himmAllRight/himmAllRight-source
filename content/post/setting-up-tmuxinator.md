+++
title  = "Setting up Tmuxinator"
date   = "2019-05-25"
author = "Ryan Himmelwright"
image  = "img/posts/scripting-tmux-workspaces/parking-garage-sunset1.jpg"
caption= "Liberty Warehouse, Durham NC"
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


#### (also) Pane splits

## Launch

<a href='../../img/posts/setting-up-tmuxinator/start-website-tmuxinator.gif'>
<img alt="Launching Website tmux session with tmuxinator" src="../../img/posts/setting-up-tmuxinator/starting-website-tmuxinator.png" onmouseover="this.src='../../img/posts/setting-up-tmuxinator/start-website-tmuxinator.gif'" onmouseout="this.src='../../img/setting-up-tmuxinator/start-website-tmuxinator.gif'" style="max-width: 100%;"/>
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
