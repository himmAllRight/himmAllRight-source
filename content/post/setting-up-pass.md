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

As mentioned, pass is just a bunch of encrypted plain text files. While pass can automatically
return the first line to the clipboard for easy password entering, the contents of a pass file can
really be anything. This gives the system a ton of flexibility, as my password items don't have to
conform to any sort of template.

## Installing Pass & Help Packages

On Fedora, pass can be installed using dnf. For other systems, check out the "Download" section of
the [pass website](https://www.passwordstore.org/).

```bash
sudo dnf install pass
```

## Configuring Pass

After installing pass, there are few steps to configure it. First, we need to create a gpg key if
one doesn't already exist. Then, we need to initialize a password store using that key.

*(I went a little heavy with the animation images below. Sorry. I hope they are useful. Being a
visual learner, at the very least they are helpful for me when I have to revist this post...)*

### New GPG Key

<img alt="animation running gpg --gen-key" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/generate-gpg-keys.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Generate a new gpg key with `gpg2 --full-gen-key`.</div>

First, lets create a new gpg key. To create a gpg key, the `gpg2 --gen-key`
command can be used.  However, I opted to use `gpg2 --full-gen-key` which is
just a bit more detailed.  The command will prompt for several bits of
information. The default selections are fine for most of the options (I usually
choose to use a 4096-bit key... because why not). At the end it will ask for a
Name, Password, and optional comment.

It should be noted that `gpg2` most likely needs to be used instead of `gpg`
for pass. However, it may vary depending on distribution and the package
version.


### Pass Init

<img alt="Crating new pass store with pass init" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/pass-init.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Initialize a new pass store with `pass init`.</div>

After a gpg key has been generated, it can be used to initialize pass.
First, get the key's ID using `gpg2 --list-secret-keys`. Then, initialize pass
using `pass init GPG-KEY-ID`. This will create and initialize a password-store
directory, located by default at `~/.password-store/`.


### Add some items

<img alt="Adding, editing, and retrieving some passwords with `pass`, `pass insert`, `pass generate`, and `pass edit`" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/pass-add-demo.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Adding, editing, and retrieving some passwords with `pass`, `pass insert`, `pass generate`, and `pass edit`.</div>

With pass initialized, lets start adding passwords to it! Here are *some* of
the most common commands to do so:

#### insert

`pass insert` ... inserts a password. Simply call it with the folder/file
structure desired for the password, and it will then prompt for the password to
save. That's it.

```
pass insert Shopping/amazon.com/ryan
```

#### pass generate

In addition to inserting existing passwords, pass can also *generate* new ones
using `pass generate`. Simply provide the password path, and optionally the
length of the password. Pass will then generate a random password, spit it out
on screen, and insert the entry to the password store.

```
pass generate Shopping/SomeFakeStore/ryan 35
```

#### pass edit

Generating a password is great, but being a forgetful person, I like to keep
additional information in my pass entries (username, email, website url). This
is where `pass edit` comes in. To use it, call it with a password entry, and it
will open up the contents of the entry in your favorite editor. Make your
changes and save.

```
pass edit Shopping/SomeFakeStore/ryan
```
Then, in vim:
```bash
<&DdU1x<&~&{;w7w"kvsWdHAF-\Vi"I9Q)I
---
Username: ryan
Password: <&DdU1x<&~&{;w7w"kvsWdHAF-\Vi"I9Q)I
URL: https://www.some-bs-store.com
Notes: I love this place!
```

#### pass

It should be noted to actually *get* stored passwords, just use `pass` with the
password entry location. Optionally, use the `-c` flag to copy the password
(first line if a multi-line entry) to the clipboard instead of spewing it into
the terminal.

```bash
pass Shopping/SomeFakeStore/ryan
## or ##
pass -c Shopping/SomeFakeStore/ryan
```

## Making Pass Better

#### `pass git`

<img alt="Managing and maintaining the password store with `pass git`" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/pass-git.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Use git to automatically maintain your password store</div>


#### `passmeu`

<center>
<video style="max-width:100%;" controls>
  <source src="../../img/posts/setting-up-pass/passmenu_demo.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
<div id="caption">`passmenu` lets you easily search and select a pass item.</div>
</center>

## Setting up your pass setup on a new system

### add gpg keys

#### export

<img alt="Export a gpg key to use with pass on another system" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/export-key.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Export a gpg key to save or use on another system.</div>

#### import

<img alt="Import a gpg key and trust it to use with pass" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/pass-import-gpg-key.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Import and trust a gpg key to use it with pass.</div>

### Pull pass repo



### Conclusion
