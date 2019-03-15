+++
title  = "Scriping A Tmux Workspace Startup"
date   = "2019-03-20"
author = "Ryan Himmelwright"
image  = "img/posts/charmeleon-desktop-design/rht-header.jpg"
caption= "Red Hat Tower, Raleigh NC"
tags   = ["Linux", "Dev", "Dotfiles", "Customization", "Shell",]
draft  = "True"
Comments = "True"
+++

For years, I have enjoyed the terminal multiplexer [tmux](http://www.tmux.com).
It allows you to open a shell in the terminal that can be split horizontally and
vetically into multiple panes. Like a browser, there can also be multiple tabs
or even sessions of these split terminals. Best of all, tmux sessions can be
detached and re-attached later (which is wonderful combined with ssh). As I
have been utilizing tmux even more at work now, I've learned how to script the
startup/configuration of my tmux sessions for each project.

<!--more-->

After scripting some of my tmux workflow setups for projects at my job, I
decided that I want to script a tmux startup session for when I'm writing
website posts. Which is a perfect example to write a post about :D.


Some outlining for the post. The intro might be broken up and put in a
background section...

### tmux background/demo?

### How I scripted my work stuff/What workflow I want for the website stuff

### Walk through making the new script
#### New Script
```bash
#!/bin/bash

```

#### Create new tmux session (with var name)


#### Name initial default Pane (and switch to `zsh`)


#### Add a new (named) pane for server
Also kick off hugo?

#### Add a new (name) pane for vim
Open VIM?

### Demo workflow, how I'd use it

### Conclusion
