+++
title  = "Setting up Tmuxinator"
date   = "2019-05-23"
author = "Ryan Himmelwright"
image  = "img/posts/setting-up-tmuxinator/mountain-trees.jpg"
caption= "Port Angeles, WA"
tags   = ["Linux", "Dev", "Dotfiles", "Customization", "Shell",]
draft  = "False"
Comments = "True"
+++

Several weeks ago I wrote about [scripting a tmux session's
initialization](/post/scripting-tmux-workspaces/). At the end of the post I
mentioned that while writing it, I had learned about
[tmuxinator](https://github.com/tmuxinator/tmuxinator). I even teased that it
looked so good, I may switch to it eventually. Well... that didn't take long. I've
scrapped my tmux shell scripts, and have converted to using tmuxinator. Here's
how.

<!--more-->

## What is Tmuxinator?
[Tmuxinator](https://github.com/tmuxinator/tmuxinator) is a command line
application that makes it easy to create and manage tmux sessions. It allows a
user to define how to setup a session, including naming windows, splitting
panes, and what commands initially run in each pane. The configuration is done
in yaml, so it is very easy to figure out and get started.

## Install
Most distros probably have `tmuxinator` in their offical repos. These days, I
mostly run Fedora on all of my machines and I was able to find it there:

```shell
sudo dnf install termixinator
```

**However**, I found that this version was quite out of date (`0.6.11`) even on my new
Fedora 30 install, so I recommend using the method stated on
the project's Github page (requires `rubygems`) to install a much more current
version (`1.1.0`):

```shell
gem install tmuxinator
```


## Create
To create a new tmuxinator profile, pass the desired project name to `tmuxinator new`:

```sh
tmuxinator new Website
```

This will open up a new tmuxinator template inside your default editor. The
default template contains a bunch of comments that help guide how to configure
it.


#### Header

The first thing to set at the top of the template is the `name` field, followed
by the `root` directory. The tmux session name is defined with `name`, and
`root` will be the directory which all of the windows/panes open up in by
default. For example, when converting my website script, I set `name` to
`Website` and `root` to the location where I keep my website's git working
directory, `~/Documents/himmAllRight-source`:

```yaml
# /home/ryan/.config/tmuxinator/Website.yml

name: Website
root: ~/Documents/himmAllRight-source
```

#### Windows

Next, I needed to configure my windows. To convert the script from my previous
post, I wanted a dedicated 'Main' window, one for the server, one for vim, and
one for an extra shell. Additionally, since that last post I've added a window
that launches my hugo-served website in a web browser. To recreate *all of
that* with tmuxinator:

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

Done. Save the file and that's it! See the benefit of using tmuxinator??

#### Pane splits

While I don't use them in this example configuration, it should be noted that
setting up pane splits is also quite easy with tmuxinator. For example, if I
wanted to split the server window into two panes, one running the hugo server
and one running htop, I could use:

```yaml
- Server:
    layout: even-vertical
    panes:
        - hugo
        - htop
```

The `layout` key defines which
[tmux layout](http://man7.org/linux/man-pages/man1/tmux.1.html#WINDOWS_AND_PANES) to
use when splitting the panes, and `panes` is a list that defines what to run in
each pane.


## Launch

<a href='../../img/posts/setting-up-tmuxinator/start-website-tmuxinator.gif'>
<img alt="Launching Website tmux session with tmuxinator" src="../../img/posts/setting-up-tmuxinator/starting-website-tmuxinator.png" onmouseover="this.src='../../img/posts/setting-up-tmuxinator/start-website-tmuxinator.gif'" onmouseout="this.src='../../img/posts/setting-up-tmuxinator/starting-website-tmuxinator.png'" style="max-width: 100%;"/>
</a>
<div class="caption">Launching my website tmux session with tmuxinator</div>

To start up the newly defined tmuxinator project, use `tmuxinator
start`:

```sh
tmuxinator start Website
```

## Manage

All of the tmuxinator profile templates are stored at `~/.config/tmuxinator`,
which means they can easily be copied to a new machine, or even
saved/maintained in source control.

*Note: I think older versions stored them at `~/.tmuxinator/`, so check there
if they are missing.*


## Conclusion

That's it. While scripting my own method was a good bash exercise and helped me
learn the details of `tmux` a little bit better, I ultimately think that
`tmuxinator` is the way to go. This is especially true when using tmux to work
on several projects or even across multiple machines. If you *still* haven't
tried `tmux`... I *highly* recommend checking it out!
