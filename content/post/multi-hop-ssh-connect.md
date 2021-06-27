+++
title   = "Multi-hop ssh Connections"
date    = "2021-06-27"
author  = "Ryan Himmelwright"
image   = "img/posts/multi-hop-ssh-connections/duke_alumni_center_header.jpeg"
#image   = "img/posts/multi-hop-ssh-connections/durham_bulls_sunset_header.jpeg"
#image   = "img/posts/multi-hop-ssh-connections/durham_bulls_night_header.jpeg"
caption = "Karsh Alumni Center (Duke University), Durham NC"
tags    = ["Linux", "ssh", "network", "shell"] 
draft   = "False"
Comments = "True"
+++

Last weekend, I wanted to ensure that I could work on a personal project using
my typical setup, while I was away for a few hours. This consists of running VS
Code on my [macbook air](/post/m1-air-initial-thoughts/), but [remotely
connected](/post/vscode-remote/) to my [Linux
desktop](/post/selecting-charmeleons-upgrades/). All of the coding actually
happens on the Linux computer, even though I am running VS code on my macbook.
However, when outside of my home network, connecting to the desktop requires
multiple `ssh` hops. Fortunately, configuring `ssh` to handle a multi-hop setup
is actually quite easy *and*....  it works with the VSCode remote plugin.
Here's how.

<!--more-->

### Problem

To restate the problem: If I am outside of my home network, I need to make
multiple `ssh` '*hops*' in order to get to my desktop (charmeleon). 

```
Laptop -> Ponyta (SSH Entry Node) -> Charmeleon (Desktop)
```

Normally, this requires me to first `ssh` into my home network (`ponyta`), and
then from *there*, `ssh` *again* to whichever device I want to connect to (In
this example, `Charmeleon`). Out of pure laziness, I want to run these steps as
a single command. Additionally, for tasks that are automated, or outside of a
shell, connecting to my desktop truly *needs* to be a single step in order to
work.  

## Solution

An simple solution is to create a new host item in the ssh config file. In this
file, we can utilize the `ProxyCommand` option to setup a multi-hop scenario.
So, I added the following my `~/.ssh/config` (make sure to swap out your `PORT`
and `HOSTNAME` values accordingly):

```
Host remote-charmeleon
	Hostname CHAMELEON-IP
	User ryan
	ProxyCommand ssh -p PORT ryan@PUBLIC_FACING_PONYTA_HOSTNAME -W %h:%p
```

Now, I only need to run `ssh remote-charmeleon` to kick off the the full `Laptop
-> (Ponyta) -> Charmeleon` sequence. Easy.


## Setting it up in VSCode

<center>
<a href="../../img/posts/multi-hop-ssh-connections/vscode-multi-hop-connect.png"><img alt="Connecting via a multi-hop ssh connection in vscode" src="../../img/posts/multi-hop-ssh-connections/vscode-multi-hop-connect.png" style="max-width: 100%;"/></a>
<div class="caption">Connecting to a multi-hop system via ssh in VS Code</div>
</center>

Now, how can this be used in a VS Code session? 

All I had to do was add the config sequence to the ssh config file that *VSCode*
uses, which I usually have set to be different from my default one.

To do this, call the `Remote-SSH: Open SSH Configuration File` in VS Code to
open the proper config file. Next, add the same code from above to the config.
From then on, you can select that host item when running `Remote-SSH: Connect to
Host...` in VS Code.

For example, I can now select `remote-charmeleon` when VSCode prompts for the
host to connect to.

## Conclusion

That's all. It's a simple solution that I very much appreciate. I always forget
how powerful `ssh` is, especially when you start setting up custom configs. It's
worth taking a look at! As always, `man ssh` is a great place to start 😉.