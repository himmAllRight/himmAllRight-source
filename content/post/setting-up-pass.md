+++
title  = "Configuring Pass, the Standard Unix Password Manager"
date   = "2018-12-04"
author = "Ryan Himmelwright"
image  = "img/header-images/liberty-brick-lock.jpg"
caption= "Liberty Warehouse Apartments, Durham, NC"
tags   = ["Linux", "Homelab", "Network", "Dotfiles"]
draft  = false
Comments = "True"
+++

I've been using `pass` for several years now to manage my passwords. I used to have issues setting
it up on a new machine, but those days appear to be ove. It is a simple, but flexible system.
Here's how to get started.

<!--more-->

## My Password Manager History

For the longest time... I didn't use a password manager (but in my defence, not
many people did). Then in college, I started using
[lastpass](https://www.lastpass.com/). It was simple and made it easy for me to
switch all my passwords to randomly generated ones. It even allowed me to
configure my [yubikey](https://www.yubico.com) with it. It was a good system
and worked for years.


<center>
<a href="../../img/posts/setting-up-pass/LastPass-Logo.png"><img alt="LastPass logo" src="../../img/posts/setting-up-pass/LastPass-Logo.png" style="max-width: 100%;"/></a>
</center>

Then, in 2015, Lastpass was acquired by [LogMeIn](https://www.logmeininc.com),
which had a questionable past of Linux support. Like many others in the open
source community... I started looking for alternatives. I had already started
to keep my eyes opened for a replacement even before the acquisition because
there was one big issue I had with LastPass... it largely worked as a Chrome or
Firefox plugin. As someone who occasionally uses other browsers like
[qutebrowser](https://qutebrowser.org), or works on headless machines, I try
not to use applications that exist solely as a FireFox/Chome app.
Additionally... I'm not a fan of web-apps.

So, as I watched others switch their password manager, I watched Chris Fischer
of the Linux Action Show, switch to
[pass](https://www.youtube.com/watch?v=OfgZ5Fh-NfE&feature=youtu.be&t=4935).
While I don't think he kept with the system long-term... I have.

## What I like about [pass](https://www.passwordstore.org)

#### Unix Philosophy "Simplicity"

While the average computer might not think `pass` is "simple", designed to follow the [Unix
philosophy](https://en.wikipedia.org/wiki/Unix_philosophy), pass's architecture is. At its core,
pass is just a bunch of [gpg](https://en.wikipedia.org/wiki/GNU_Privacy_Guard) encrypted text
files. This model makes pass easily compatible with many other great tools, like bash, git,
[dmenu](https://git.zx2c4.com/password-store/tree/contrib/dmenu),
[xmonad](https://hackage.haskell.org/package/xmonad-contrib-0.13/docs/XMonad-Prompt-Pass.html) and
[emacs](https://git.zx2c4.com/password-store/tree/contrib/emacs).

#### Can access on a headless system

Being a command-line tool, I can use pass anywhere, no matter how strange my setup may be. I can
have it on my desktop, on a headless server, or even inside a container. This means that even if I
am on a public computer, if I can `ssh` into one of my servers... I can access my passwords.

#### Flexible

*Add animation of making a saved note password*

As mentioned, pass is just a bunch of encrypted plain text files. While pass can automatically
return the first line to the clipboard for easy password entering, the contents of a pass file can
really be anything. This gives the system a ton of flexibility, as my password items don't have to
conform to any sort of template.

## Installing Pass & Help Packages

On Fedora, pass can be installed with dnf. For other systems, check out the "Download" section of
the [pass website](https://www.passwordstore.org/).

```bash
sudo dnf install pass
```

## Configuring Pass

#### New GPG Key

*TODO: Make animation a hover-over*
<a href="../../img/posts/setting-up-pass/generate-gpg-key.gif"><img alt="animation running gpg --gen-key" src="../../img/posts/setting-up-pass/generate-gpg-keys.gif" style="max-width: 100%;"/></a>
<div class="caption">Generate a new gpg key with `gpg --gen-key`.</div>


#### Pass Init

*TODO: Make animation a hover-over*
<a href="../../img/posts/setting-up-pass/pass-init.gif"><img alt="Crating new pass store with pass init" src="../../img/posts/setting-up-pass/pass-init.gif" style="max-width: 100%;"/></a>
<div class="caption">Initialzie a new pass store with `pass init`.</div>


#### Add some items

## Making Pass Better

#### `pass git`

#### `passmenu`


## Setting up your pass setup on a new system

### add gpg keys

#### export

#### import

### Pull pass repo

### init


### Conclusion
