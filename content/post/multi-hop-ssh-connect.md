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

Last weekend, I knew I would want to work on a personal project while I was away
for a few hours. I wanted to use my typical setup, which consists of VS Code
opened on my macbook air, but connected remotely to my Linux desktop, where all
of the coding is being done. However, connecting to my desktop required multiple
`ssh` hops when outside the network. Fortunately, it turns out that it is
actually quite easy to configure `ssh` to handle a multi-hop setup.
*And*.... it even works with the VSCode remote plugin. Here's how.

<!--more-->

### Problem

So to elaborate my problem: If I am outside of my home network, I need to make
multiple `ssh` '*hops*' in order to get to my desktop (charmeleon). For example:

```
Laptop -> Ponyta -> Charmeleon
```

Normally, this requires `ssh`'ing into my home network (ponyta), and then from
*there*, `ssh`'ing *again* to whatever device I want to connect to. Sometimes I
simply want to do this in a single command. Additionally, for tasks that are
outside of a shell, connecting to my desktop really *needs* to be a single step
(like remote sessions in VS Code). 

## Solution

An easy solution is to create a host item to the ssh config file. The
`ProxyCommand` actually allows us to configure a multi-hop scenario. For
example, I added the following my `~/.ssh/config`:

```
Host remote-charmeleon
	Hostname HOST-IP
	User ryan
	ProxyCommand ssh -p PORT ryan@PUBLIC_FACING_HOSTNAME -W %h:%p
```

Now, I just have to run `ssh remote-charmeleon`, and it does the `(Ponyta) ->
Charmeleon` sequence in that single command. This 1. makes it easier to do (I
only need 1 ssh instead of manually hopping myself), and 2. allows me to easier
use it in systems like VSCode.

## Setting it up in VSCode

<center>
<a href="../../img/posts/multi-hop-ssh-connections/vscode-multi-hop-connect.png"><img alt="Connecting via a multi-hop ssh connection in vscode" src="../../img/posts/multi-hop-ssh-connections/vscode-multi-hop-connect.png" style="max-width: 100%;"/></a>
<div class="caption">Connecting to a multi-hop system via ssh in VS Code</div>
</center>

So, how can I use this for a VS Code session? It's actually also very easy.

I just had to add the config sequence to the ssh config file that *VSCode* uses
(which I usually have set to be different from my default.)

In VSCode, you can call the Remote command to open the ssh config file. Select
the one you have set to use (it should give it as an option in the bar), and
then add the same code as above to that config. From then on, you can reference
that item when ssh connecting in VSCode.

For example, I run `ssh remote-charmeleon` when VSCode asks me for the command
to make the remote connection with.

## Conclusion

That's all. It's a simple soltuion that I very much appreciate. I always forget
how powerful `ssh` is, especially when you start setting up custom configs. It's
worth taking a look at!