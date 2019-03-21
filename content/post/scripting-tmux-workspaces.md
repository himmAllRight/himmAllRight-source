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

```bash
# Session Name
session="Website"

# Start New Session with our name
tmux new-session -d -s $session
```

#### Name initial default Pane (and switch to `zsh`)

``` bash
# Name first Pane and start zsh
tmux rename-window -t 0 'Main'
tmux send-keys -t 'Main' 'zsh' C-m 'clear' C-m
```


#### Add a new (named) pane for server
Also kick off hugo?

```bash
# Create and setup pane for hugo server
tmux new-window -t $session:1 -n 'Hugo Server'
tmux send-keys -t 'Hugo Server' 'hugo serve -D -F' C-m
```
#### Add a new (name) pane for vim
Open VIM?

```bash
# setup Writting window
tmux new-window -t $SESSION:2 -n 'Writting'
tmux send-keys -t 'Writting' "nvim" C-m
```

#### Setup an extra shell. Why not?

```bash
# Setup an additional shell
tmux new-window -t $SESSION:3 -n 'Shell'
tmux send-keys -t 'Shell' "zsh" C-m 'clear' C-m
```

#### Attach Session

```bash
# Attach Session, on the Main window
tmux attach-session -t $SESSION:0
```

### Demo workflow, how I'd use it

#### Minor improvement

`if` wrapper for if the sessions already exists

##### check if session already exists

```bash
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)
```
Wrap the new session steps in an `if` conditional:

```bash
if [ "$SESSIONEXISTS" = "" ]
then
...
fi
```

### Conclusion

Everything all together:

```bash
#!/bin/sh

# Set Session Name
SESSION="Website"
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)

# Only create tmux session if it doesn't already exist
if [ "$SESSIONEXISTS" = "" ]
then
    # Start New Session with our name
    tmux new-session -d -s $SESSION

    # Name first Pane and start zsh
    tmux rename-window -t 0 'Main'
    tmux send-keys -t 'Main' 'zsh' C-m 'clear' C-m # Switch to bind script?

    # Create and setup pane for hugo server
    tmux new-window -t $SESSION:1 -n 'Hugo Server'
    tmux send-keys -t 'Hugo Server' 'hugo serve -D -F' C-m # Switch to bind script?

    # setup Writting window
    tmux new-window -t $SESSION:2 -n 'Writting'
    tmux send-keys -t 'Writting' "nvim" C-m

    # Setup an additional shell
    tmux new-window -t $SESSION:3 -n 'Shell'
    tmux send-keys -t 'Shell' "zsh" C-m 'clear' C-m
fi

# Attach Session, on the Main window
tmux attach-session -t $SESSION:0
```

This post might be moot now if I check out
[tmuxinator](https://github.com/tmuxinator/tmuxinator), which I've just learned
about... oh well. It was still a good exercise in bash scripting :P.
