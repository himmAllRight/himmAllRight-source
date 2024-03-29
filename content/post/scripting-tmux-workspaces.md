+++
title  = "Scripting A Tmux Work-space Start-up"
date   = "2019-03-27"
author = "Ryan Himmelwright"
image  = "img/posts/scripting-tmux-workspaces/parking-garage-sunset1.jpg"
caption= "Liberty Warehouse, Durham NC"
tags   = ["Linux", "Dev", "Dotfiles", "Customization", "Shell",]
draft  = "False"
Comments = "True"
+++

I love the terminal multiplexer, [tmux](http://www.tmux.com). It adds
functionality to the terminal, such as multiple tabs, pane splitting, and the
ability to detach and re-attach everything later (which is *amazing* when
combined with `ssh`). I have been utilizing tmux even more at work, and recently
started to script the start up/configuration a tmux session for each project.
The other day, I decided to write a script to spin up a session for working on my
website... and thought it would be a great tutorial!

<!--more-->

### Tmux

<img alt="tmux demo animation" src="../../img/posts/scripting-tmux-workspaces/animation-hover.png" onmouseover="this.src='../../img/posts/scripting-tmux-workspaces/tmux-demo.gif'" onmouseout="this.src='../../img/posts/scripting-tmux-workspaces/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Small tmux demonstration</div>

When working on a project, I like to use tmux to maintain all of the terminal
windows related to it. This keeps everything together, and even allows me to
detach the session, switch to another computer, ssh into the previous computer,
and re-attach my working tmux session. Paired with the fact that I've started
using VIM again, it works seamlessly. Scripting the initialization makes
getting started even smoother.

### Automating tmux initialization for working on my website
#### New Script

First, lets create a new script. Start by opening a new file, and adding a bash
[shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) line to the top:

```bash
#!/bin/bash

```

This line tells the system that the following text will be a
[bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) script.

*Optional: Save and close the file, then re-open it to take advantage the text
editor's bash syntax highlighting if it didn't automatically switch it on.*


#### Create a new tmux session (with var name)

Next, lets define a variable to store the tmux session name. This will make it
easier to change the session name later on. Using the session variable, a new
tmux-session with our desired name can be created.

```bash
# Session Name
session="Website"

# Start New Session with our name
tmux new-session -d -s $session
```

#### Name initial default Window (and switch to `zsh`)

Let's customize the default window and give it a new name. Lets call this first tmux
window `"Main"`, and have it simply run a [zsh](https://ohmyz.sh/) shell. After
creating a new session, there is only one window, so I know it will be
identified with the number `0`. I can use this with `-t` to rename the window.

``` bash
# Name first Window and start zsh
tmux rename-window -t 0 'Main'
tmux send-keys -t 'Main' 'zsh' C-m 'clear' C-m
```

I can then use the `send-keys` command with the new window name to start zsh.
This is the equivalent of typing `zsh`, `[Enter]`, `clear`, `[Enter]` into the
command line.


#### Add a new (named) window for hugo server

With the main tmux window setup, I want to add a few more for
different tasks. First, I want a window that can run the hugo server
as I'm writing a post. With a session already created, I can name the
window as I create it, using just the `new-window` comamnd with the
`-n` flag.

```bash
# Create and setup pane for hugo server
tmux new-window -t $session:1 -n 'Hugo Server'
tmux send-keys -t 'Hugo Server' 'hugo serve -D -F' C-m
```

Again, I used tmux `send-keys`, this time to send the `hugo serve -D
-F` command to start up a hugo server for local draft editing.

#### Add a new (name) pane for vim

Now, I need a place to write website posts... so lets fire up a new tmux
window, and open up neovim inside of it.

```bash
# setup Writing window
tmux new-window -t $SESSION:2 -n 'Writing'
tmux send-keys -t 'Writing' "nvim" C-m
```

#### Another shell

Lastly, lets create one more shell window, just in case it's needed. Why not?

```bash
# Setup an additional shell
tmux new-window -t $SESSION:3 -n 'Shell'
tmux send-keys -t 'Shell' "zsh" C-m 'clear' C-m
```

#### Attach Session

With the tmux session all configured and customized, we can tell the script to
go ahead and attach it, using the `attach-session` command with the session
name variable.

```bash
# Attach Session, on the Main window
tmux attach-session -t $SESSION:0
```

*Note: the `0` tells tmux to attach the first window (`Main`). Using
another index value will attach a different window. For example, `1`
would open the `Hugo Server` window when attaching*

#### Bonus: Minor improvement

<img alt="tmux demo animation" src="../../img/posts/scripting-tmux-workspaces/animation-hover.png" onmouseover="this.src='../../img/posts/scripting-tmux-workspaces/tmux-duplicate-windows.gif'" onmouseout="this.src='../../img/posts/scripting-tmux-workspaces/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">The script would create duplicate windows if the tmux
session already existed.</div>

At this point, I was done with the tmux script. It worked well for creating my
session and attaching it. However, there was *one* issue I still had. If I ran
the script when there was a tmux session with the same name *already*, it would
just double up the windows in that session. If I accidentally did this, I would
have to go through each window, close out whatever and was running, and then
close the window.

To fix this issue, I decided to wrap the initialization commands inside of an
`if` statement, and only run them if the tmux session *didn't* already exist.

##### Checking if the Session Already Exists

First, I needed a way to *check* whether the desired tmux session already existed
or not. This can be done by "grep'ing" the output of `tmux list-sessions` for
the session name, which we've already conveniently stored in our `$SESSION`
variable. For Cleanliness, I took the output of that process and saved it in a
`SESSIONEXISTS` variable, defined directly under `SESSION` in the script.
```bash
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)
```

If the session exists, `SESSIONEXISTS` will be a string of the line which `grep`
matched. Otherwise, it will just be an empty string (`""`).


Now, I can use the `SESSIONEXISTS` variable with an `if` condition to wrap the tmux
setup code so that it only runs if `SESSIONEXISTS` is `""`.
```bash
if [ "$SESSIONEXISTS" = "" ]
then
...
fi
```

The `attach-session` command should be *outside* of the `if` body,
because it will be run in both cases (even if the session doesn't have
to be created, we still want to attach the one that already exists).


### Conclusion

That is it. Here is the script with everything all put together:

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

    # setup Writing window
    tmux new-window -t $SESSION:2 -n 'Writing'
    tmux send-keys -t 'Writing' "nvim" C-m

    # Setup an additional shell
    tmux new-window -t $SESSION:3 -n 'Shell'
    tmux send-keys -t 'Shell' "zsh" C-m 'clear' C-m
fi

# Attach Session, on the Main window
tmux attach-session -t $SESSION:0
```

I hope this post has been helpful! Although, I have to admit that this post
*may* be moot if I decide check out
[tmuxinator](https://github.com/tmuxinator/tmuxinator) (which a co-worker
recommended) ... oh well. I guess this endeavor was still a good exercise in
some bash scripting :P.
