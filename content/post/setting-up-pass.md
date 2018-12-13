+++
title  = "Configuring Pass, the Standard Unix Password Manager"
date   = "2018-12-12"
author = "Ryan Himmelwright"
image  = "img/header-images/liberty-brick-lock.jpg"
caption= "Liberty Warehouse Apartments, Durham, NC"
tags   = ["Linux", "Homelab", "Network", "Dotfiles"]
draft  = false
Comments = "True"
+++

I've been using `pass` to manage my passwords for quite some time.
During the early days of use, I occasionally had difficulty configuring it on
new machines, but those days appear to be long gone. It is a simple, generic,
yet flexible system.  Here's how to get started.

<!--more-->

*(but first, some background... feel free to skip ahead)*

## My Password Manager History

For the longest time, I didn't use a password manager (in my defence, not many
people did). Then in college, I started using
[LastPass](https://www.lastpass.com/). It was simple and made it easy to switch
all of my passwords to randomly generated ones. I had a good system that
worked for a few years, and  was even able to integrate my
[yubikey](https://www.yubico.com) with it.


<center>
<a href="../../img/posts/setting-up-pass/LastPass-Logo.png"><img alt="LastPass logo" src="../../img/posts/setting-up-pass/LastPass-Logo.png" style="max-width: 100%;"/></a>
</center>

Then in 2015, Lastpass was acquired by [LogMeIn](https://www.logmeininc.com),
which had a questionable past of Linux support. Like many others in the open
source community... I started looking for alternatives.

I had already been searching for a LastPass replacement even before the
acquisition. My search was mainly fueled by one big issue I had with
LastPass... it required a web browser to use.  Additionally, to utilize it's full
feature set, it needed to run as a Chrome or Firefox plugin. As someone who
often uses alternative web browsers (like [qutebrowser](https://qutebrowser.org)),
or works on headless machines, I try not to use applications that exist solely
as a FireFox/Chome app.  I am also not a fan of pure website-apps in
general.

So, as the I watched others switch password managers amongst the acquisition
hype, one switch I remember seeing was Chris Fischer of the Linux Action Show.
In episode 387 of LAS, Chris and Noah (his co-host) discussed LastPass alternatives, and
Chris highlighted his switch to
[pass](https://www.youtube.com/watch?v=OfgZ5Fh-NfE&feature=youtu.be&t=4935).
While I don't think he kept with the system long-term... I have.

## What I like about [pass](https://www.passwordstore.org)

#### Unix Philosophy "Simplicity"

Okay. The average computer user will not think `pass` is "simple". I agree.
However, being designed to follow the [Unix
philosophy](https://en.wikipedia.org/wiki/Unix_philosophy), pass's *architecture
is*. Basically, pass is just a nice wrapper around a bunch of
[gpg](https://en.wikipedia.org/wiki/GNU_Privacy_Guard) encrypted text files. It
is a minimal, but tested solution.  This model makes pass easily compatible
with many other great tools, such as bash, git,
[dmenu](https://git.zx2c4.com/password-store/tree/contrib/dmenu),
[xmonad](https://hackage.haskell.org/package/xmonad-contrib-0.13/docs/XMonad-Prompt-Pass.html)
and [emacs](https://git.zx2c4.com/password-store/tree/contrib/emacs).

#### Command Line Tool

As a command-line tool, I can use pass anywhere. It doesn't matter how conventional or strange the
setup may be. I can have it on my desktop, on a headless server, or even inside a container. It
makes no difference.  Even if I am on a public computer, if I can `ssh` into one of my servers, I
can access my passwords.

#### Flexible

By default, pass assumes the first line of a store file is the password.  However, the
multi-line contents of a pass file can be anything. For example, pass could be used securely store
encrypted notes. This gives the system a ton of flexibility, as the password items don't *have* to
conform to any sort of template.

## Installing Pass & Help Packages

On Fedora, pass can be installed using `dnf`. For other systems, check out the
"Download" section of the [pass website](https://www.passwordstore.org/).

```bash
sudo dnf install pass
```

## Configuring Pass

After installing pass, there are few steps to configure it. First, we need to create a gpg key if
one doesn't already exist. Then, we need to initialize a password-store using that key.

**Note:** *I went a little heavy with the animation images in the remainder of
the post. Sorry. I hope they are more useful than annoying. Being a visual learner, at the very
least they are helpful for me when I reference this post in the future. ...*

### New GPG Key

<img alt="animation running gpg --gen-key" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/generate-gpg-keys.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Generate a new gpg key with `gpg2 --full-gen-key`.</div>

To create a gpg key, the `gpg2 --gen-key` command is normally used.  However, I opted to use `gpg2
--full-gen-key`, which allows for a bit more control during setup.  The command will prompt for
several bits of information, and the default selections are generally fine for most of the options
(Personally, I use a 4096-bit key, because... why not?). At the end it will ask for a
name, Password, and optional comment.

*It should be noted that `gpg2` most likely needs to be used instead of `gpg`
for pass. However, it may vary depending on distribution and the package
versions.*


### Pass Init

<img alt="Crating new pass store with pass init" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/pass-init.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Initialize a new pass store with `pass init`.</div>

After a gpg key has been generated, it can be used with pass.  First, find the key's ID by using
`gpg2 --list-secret-keys`. Then, configure pass with `pass init GPG-KEY-ID`. This will create a
password-store directory, located by default at `~/.password-store/`.


### Add some items

<img alt="Adding, editing, and retrieving some passwords with `pass`, `pass insert`, `pass generate`, and `pass edit`" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/pass-add-demo.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Adding, editing, and retrieving some passwords with `pass`, `pass insert`, `pass generate`, and `pass edit`.</div>

With pass initialized, lets start adding passwords to it! Here are *some* of
the most common commands to do so:

#### insert

Simply put, `pass insert` ... inserts a password. Call it with the desired folder/file
structure for the password, and pass will then prompt for the password to
save. That's it.

```
pass insert Shopping/amazon.com/ryan
```

#### pass generate

In addition to inserting existing passwords, pass can also *generate new* ones
using `pass generate`. Just provide the password path, and optionally the
length of the password. Pass will then generate a random password, spit it out
on screen, and insert the entry to the password-store.

```
pass generate Shopping/SomeFakeStore/ryan 35
```

#### pass edit

Generating passwords is great, but being a forgetful person, I like to keep additional information
in my pass entries (username, email, website url). This is where `pass edit` comes in. When called,
`pass edit` will open up the contents of the entry in the default editor. From there, make the
changes, and save.

For example:

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

Lastly, to retrieve stored passwords, call `pass` with the
password entry. Optionally, use the `-c` flag to copy the password
(first line if a multi-line entry) to the clipboard instead of spewing it into
the terminal.

```bash
pass Shopping/SomeFakeStore/ryan
## or ##
pass -c Shopping/SomeFakeStore/ryan
```

## Making Pass Better

With pass's flexibility, there are many additional features to help improve it for each user's
needs.  For me, there are two extensions that make my pass experience *much* more enjoyable.

### Pass Git

<img alt="Managing and maintaining the password-store with `pass git`" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/pass-git.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Use git to automatically maintain your password-store</div>

Password-Store items are text files, which allows them to be easily version controlled.
Consequently, pass has built in support for git with the `pass git` command. If a password-store
is linked up to a git repo, normal git commands (`add`, `mv`, `rm`...) can be used with the store.

Additionally, when modifying the store's contents, `pass git` will automatically create commits
that reflect the changes. After adding or modifying a password, issue the command `pass git push` on the updated
machine, and then `pass git pull` on others to sync the changes.


### Passmeu

<center>
<video style="max-width:100%;" controls>
  <source src="../../img/posts/setting-up-pass/passmenu_demo.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
<div id="caption">`passmenu` lets you easily search and select a pass item.</div>
</center>

While having a CLI password manager is nice when working with headless systems, it can be a bit
cumbersome for normal day-to-day use. Hence,
[passmenu](https://git.zx2c4.com/password-store/tree/contrib/dmenu/passmenu).

Passmenu is a script (now built into the upstream project) that wraps
[dmenu](https://tools.suckless.org/dmenu/) around pass. When `passmenu` is run, `dmenu` opens up
with all the password-store items to search/filter from. When an item is
selected in dmenu, the user is prompted for the gpg password (if it hasn't been unlocked recently),
after which the password is then temporarily added to the user's clipboard.

On all my computers, I bind the command `passmenu` to the keys `SUPER` + `SHIFT` + `P`.  Whenever I
need a password, I just hit those three keys, and dmenu pops up so I can search for the password I
want.  After typing in my master passphrase, I can paste the password wherever I need it.  Passmenu
makes pass much more reasonable to use.

*See Also: [rofi-pass](https://github.com/carnager/rofi-pass)*

## Setting up your pass setup on a new system

Now that I've done it over a hundred times, setting up a new system is easy. Here's my usual steps:

#### Export GPG Key

<img alt="Export a gpg key to use with pass on another system" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/export-key.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Export a gpg key to save or use on another system.</div>

First, export the password-store's gpg key.  To do that, use `gpg2 --list-secret-keys` to confirm the
key's ID, then export that key to a file with the following command:

```
gpg2 --export-secret-keys KEY-ID >> key-filename.gpg
```

Next, transfer that file to the new machine.

#### Import GPG Key

<img alt="Import a gpg key and trust it to use with pass" src="../../img/posts/setting-up-pass/animation-hover.png" onmouseover="this.src='../../img/posts/setting-up-pass/pass-import-gpg-key.gif'" onmouseout="this.src='../../img/posts/setting-up-pass/animation-hover.png'" style="max-width: 100%;"/>
<div class="caption">Import and trust a gpg key to use it with pass.</div>

On the new machine, import the gpg key using the following command (note, you
will be required to enter the key's passphrase):

```
gpg2 --import key-filename.gpg
```

After the key is imported, its *trust level* will have to be set to *ultimate*. Use the command
`gpg2 --edit-key KEY-ID` to enter the edit prompt. From there, type `trust` and hit `ENTER`. The
various levels will be shown on screen. Enter and confirm `5`, to select 'Ultimate'. Lastly, use
`quit` to leave the gpg key editor.


#### Pull Pass Repo

With the keys configured, the last step is to pull down the password-store to the new machine. If using git, this can be done with `pass git
clone`... but if I'm being honest, I usually just do a normal `git clone`, and then move
the folder to `~/.password-store/`. If not using git, just copy the store's directory and files to
the new machine. The important thing is that the store can be found at `~/.password-store` (by
default, this of course can be changed using `pass init`).

### Conclusion

That's about it. As I previously stated, I've been loving pass for years, and I
don't plan to be switching off of it any time soon. At this point, if there is
something I want to improve with my password setup... I'm sure the community
has already figured out how to do it with pass!
