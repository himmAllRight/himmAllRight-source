+++
title   = "Multi-hop ssh Connections"
date    = "2021-06-25"
author  = "Ryan Himmelwright"
image   = "img/posts/multi-hop-ssh-connections/duke_alumni_center_header.jpeg"
#image   = "img/posts/multi-hop-ssh-connections/durham_bulls_sunset_header.jpeg"
#image   = "img/posts/multi-hop-ssh-connections/durham_bulls_night_header.jpeg"
caption = "Karsh Alumni Center (Duke University), Durham NC"
tags    = ["Linux", "ssh", "network", "shell"] 
draft   = "True"
Comments = "True"
+++

Last weekend, I wanted to ensure that I could work on a personal project while I
was away for a few hours. Specifically, I wanted to use my typical setup. This
consists of using VS Code on my macbook air, but connected remotely to my Linux
desktop, where all of the coding is being done. However, when outside of my home
network, connecting to the desktop requires multiple `ssh` hops. Fortunately, it
is actually quite easy to configure `ssh` to handle a multi-hop setup. *And*....
it even works with the VSCode remote plugin. Here's how.

<!--more-->

### Problem

So to restate the problem: If I am outside of my home network, I need to make
multiple `ssh` '*hops*' in order to get to my desktop (charmeleon). For example:

```
Laptop -> Ponyta (SSH Entry Node) -> Charmeleon (Desktop)
```

Normally, this requires `ssh`'ing into my home network (`ponyta`), and then from
*there*, `ssh`'ing *again* to whatever device I want to connect to (In this
*example, `Charmeleon`). Out of pure laziness, I
want to run these steps as a single command. Additionally, for tasks that are
outside of a shell, connecting to my desktop really *needs* to be a single step
in order to work. For example, using remote sessions in VS Code. 

## Solution

An simple solution is to create a new host item in the ssh config file. In this
file, we can utilize the `ProxyCommand` command to setup a multi-hop scenario.
For example, I added the following my `~/.ssh/config`:

```
Host remote-charmeleon
	Hostname HOST-IP
	User ryan
	ProxyCommand ssh -p PORT ryan@PUBLIC_FACING_HOSTNAME_OR_IP -W %h:%p
```

Now, I only need to run `ssh remote-charmeleon` to kick off the the full `Laptop
-> (Ponyta) -> Charmeleon` sequence. Easy.


## Setting it up in VSCode

<center>
<a href="../../img/posts/multi-hop-ssh-connections/vscode-multi-hop-connect.png"><img alt="Connecting via a multi-hop ssh connection in vscode" src="../../img/posts/multi-hop-ssh-connections/vscode-multi-hop-connect.png" style="max-width: 100%;"/></a>
<div class="caption">Connecting to a multi-hop system via ssh in VS Code</div>
</center>

Now, how can this be used in a VS Code session? 

All I had to do was add the config sequence to the ssh config file that *VSCode* uses
(which I usually have set to be different from my default.)

To do this, in VSCode, call the Remote command to open the ssh config file. Select
the one you have set to use (it should give it as an option in the bar), and
then add the same code from above to that config. From then on, you can reference
that host item when ssh connecting in VSCode.

For example, I run `ssh remote-charmeleon` when VSCode prompts for the host to
connect to.

## Conclusion

That's all. It's a simple solution that I very much appreciate. I always forget
how powerful `ssh` is, especially when you start setting up custom configs. It's
worth taking a look at! As always, `man ssh` is a great place to start 😉.