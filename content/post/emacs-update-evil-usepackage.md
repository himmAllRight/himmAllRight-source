+++
title   = "Emacs Config Redo - Evil & Use-Package"
date    = "2018-06-06"
author  = "Ryan Himmelwright"
image   = "img/header-images/roger-williams-park-leaves1.jpg"
caption = "Roger Williams Park, Providence RI"
tags    = ["Linux", "Programming", "Dev", "Emacs","dotfiles"]
+++

It's about time I move off of [Spacemacs](http://spacemacs.org), and
pull togeather *my own* emacs configuration again. However, spacemacs
has shown me several packages that I wanted to incorporate into my
emacs configuration... so much so that I decided I might as well start
from scratch.

<!--more-->

<a href="../../img/posts/emacs-config-evil-usepackage/newemacs1.png"><img src="../../img/posts/emacs-config-evil-usepackage/newemacs1.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="New Emacs Window" /></a>

<div class="caption">A window of my New Emacs configuration</div>

## Evil Mode

#### History

The one emacs package that spacemacs *really* got me addicted to using
was [Evil](https://github.com/emacs-evil/evil). Evil mode emulates the
main features of [vim](https://www.vim.org) text editor. While I
*started* with emacs in college, I switched to Vim and it became the
first power editor that I *really* got into (I even bought a
[book](https://www.amazon.com/dp/059652983X/?tag=mh0b-20&hvadid=78271540595342&hvqmt=b&hvbmt=bb&hvdev=c&ref=pd_sl_y7m3vu93e_b)
to learn it better). I stuck with Vim until I became a professonial
LISP developer, and the switch back to Emacs was obvious.

<a href="../../img/posts/emacs-config-evil-usepackage/vim.png"><img src="../../img/posts/emacs-config-evil-usepackage/vim.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="A Vim Window" /></a>

<div class="caption">The Vim editor</div>

Throughout the years, I have also enjoyed using command line
applications like [cmus](https://cmus.github.io),
[ranger](https://github.com/ranger/ranger), and
[w3m](http://w3m.sourceforge.net), many of which are influenced by Vim
and often incorporate similar keyboard commands (at least the `j`,
`k`, `l`, `;` navigation. So, I have never really lost my love for the
homerow-centric, and efficient vim-style movement. However, it isn't
ideal for everything, as I prefer to *write* (not nessicarially
*edit*) code with emacs-syle navigation.

#### Best of Both Worlds

So, for the last two years I have been getting the best of both worlds
by using [Spacemacs](http://spacemacs.org/) with it's default Vim
configuration. I liked how it had all of the Evil packages already
setup, but if I wanted to jump back to Emacs-style commands, I could
just hit `Ctrl-z`.

Spacemacs was easy to use and I enjoyed it, but it really started to
have stability issues on my Windows 10 work computer. I thought going
back to a stock emacs configuration might help the issue. I decided to
build a new configuration based around `Evil`. During configuration, I
was happily surpised to learn that the `Ctrl-z` option to switch back
to Emacs-mode was a default `Evil` behavior. So, I still have the best
of both worlds.

#### Starting Config

Here is my starting `Evil` setup. I've nested other `use-pacages`
inside of it, so that if`evil` gets configured, the packages that
depend on it go ahead and configure themselves too. I'm sure this will
grow over time as I add packages I miss from the spacemacs
configuration, but so far, it seems to do all the core functionality
that I need.

```lisp
;; Evil Mode
(use-package evil
  :ensure t
  :config

  (evil-mode 1)
  (use-package evil-leader
    :ensure t
    :config
    (global-evil-leader-mode t)
    (evil-leader/set-leader "<SPC>")
    (evil-leader/set-key
      "s s" 'swiper
      "d x w" 'delete-trailing-whitespace)) 

  (use-package evil-surround
    :ensure t
    :config (global-evil-surround-mode))

  (use-package evil-indent-textobject
    :ensure t)

  (use-package evil-org
    :ensure t
    :config
    (evil-org-set-key-theme 
	  '(textobjects insert navigation additional shift todo heading))
    (add-hook 'org-mode-hook (lambda () (evil-org-mode))))

  (use-package powerline-evil
    :ensure t
    :config
    (powerline-evil-vim-color-theme)))
```

I bet I will add a bunch of key bindings over time...

## Use Package

After my setting up a base install of the Evil mode parts, I
discovered the amazing
[use-package](https://github.com/jwiegley/use-package) emacs
package. I think I have com across it before, but never actually
looked at it. After realizing how well it worked, I immediately combed
through my `.emacs` file, converting all of my `(require
'package-name)` calls to `use-package` instead.

#### Setup

After making sure the [MELPA](http://melpa.org) repos are added:

```lisp
;; Add Melpa packages to Repos
(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))
(package-initialize)

```

The `use-pckage` package can be installed from there. I wrapped the
install commands up in an `unless`, so that when my emacs loads, it
checks to see if `use-package` is installed, and installs it if it
isn't (now that basically *everything* in my config requires it).

After that, make sure to `(require 'use-package)`, although it only
needs to happen during compile.

```lisp
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(eval-when-compile
  (require 'use-package))
```

I keep all of this at the top of my configuration, and works well even
when setting up a new computer.

#### Bye Bye emacs_init.el

When I last had my own custom emacs config (before spacemacs), I had
to also maintain an `emacs_init.el` file. This was a simple emacs-lisp
script that used a `mapcar` applied a `#'package-install` across my
list of ever-growing emacs packages I needed installed for my
configuration. The idea was that when I was configuring Emacs on a new
system, I could just load and evaluate the contents of
`emacs_init.el`, and everything required for `.emacs` would
automatically install. 

The reality was that it never fully worked. There were always a few
packages that would error, or a few I forgot to add the last time I
updated my `.emacs` file. With `use-package`, I think this might be
an issue of the past. It effectively allows me to combine my emacs
init script *with* my configuration files.


#### Organize by package

I can move all of my configuration code related to a package inside
the `:config` keys.

#### Key Bindings

After moving the configs into the wrapper, I learned of the `:bind`
parameter, which lets me do my key bindings in the `use-package` call,
with a simple list of cons pairs. Ex:

```emacs-lisp
(use-package ispell
  :ensure t
  :bind
  (("C-c w" . 'ispell-word)
   ("C-c r" . 'ispell-region)))
   ```


## System Specific Load Files

I finally moved all my work-specific emacs configuration (setting up
Allego Common Lisp, defining some helper functions... and anything
with a Windows pathname) a `emacs-work.el` file. With that in it's own
seperate file, I just needed to `load` it from my main `.emacs`
configuration. The only issue with that, is I only want it to load on
my *work computer*. So, I wrapped it with a nice little handler:

```emacs-lisp
(when (string-equal system-name "LAFAYETTE")
  (load "~/.emacs-work.el"))
```

This works because I don't name my home computers with the same name
as my work machine. This little tweak worked so well, that I decided
to make another file, `emacs-linux.el`, that I could dump my linux
and/or home specific configuration into. I only load it when on a
GNU/Linux machine:

```emacs-lisp
(when (string-equal system-type "gnu/linux")
  (load "~/.emacs-linux.el"))
```

I've really enjoyed the ability to only load parts of my configuration
when a certain condition is met. Breaking down my configuration into
use-specific components seems like a good idea (like abstracting messy
code to smaller functions). Right now, I try to keep my configuration
file partitioned into sections, based on use-case (Writting,
Development, Appearance, etc). However, as I continue to fine-tune my
emacs setup, I think I might break those sections into actual *files*,
and then `load` them from the main config. 

The only issue I can see with that is that it can be confusing with
configurations overlap use-cases. However, I already have to deal with
that in a single configuration (which *section* to put it in), and my
process of converting everyting to `use-package` has actually started
to minimize that issue (because even preferences like *key bindings*
can be defined inside the `use-pacage`). This might work...

## Next Steps
