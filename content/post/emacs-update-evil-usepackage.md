+++
title   = "Emacs Config Update - Evil Mode & Use-Package"
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

## Evil Mode


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

```emacs-lisp
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

```emacs-lisp
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(eval-when-compile
  (require 'use-package))
```

I keep all of this at the top of my configuration, and works well even
when setting up a new computer.

#### Bye Bye emacs_init.el

No longer need my `emacs_init.el` file with it's `mapcar`s for
installing packages.

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
