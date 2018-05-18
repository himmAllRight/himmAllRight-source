+++
title   = "Emacs Config Redo - Evil & Use-Package"
date    = "2018-05-18"
author  = "Ryan Himmelwright"
image   = "img/header-images/roger-williams-park-leaves1.jpg"
caption = "Roger Williams Park, Providence RI"
tags    = ["Linux", "Programming", "Dev", "Emacs","dotfiles"]
+++

After switching to [Spacemacs](http://spacemacs.org) for the last year
or two, it's about time to back and pull togeather *my own* emacs
configuration again. However, spacemacs has shown me several packages
that I want to incorporate into my new emacs setup. Rather than
resuruct and Frankenstein the changes into my old `.emacs`
file... I'm starting from scratch.

<!--more-->

<a href="../../img/posts/emacs-config-evil-usepackage/newemacs1.png"><img src="../../img/posts/emacs-config-evil-usepackage/newemacs1.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="New Emacs Window" /></a>

<div class="caption">A window of my New Emacs configuration</div>

## Evil Mode

#### History

The one emacs package that spacemacs *really* got me addicted to was
[Evil](https://github.com/emacs-evil/evil), which emulates the main
features of the [vim](https://www.vim.org) text editor. I *started*
with emacs in college, but eventually switched to Vim which, became
the first power editor that I *really* got into (I even bought a
[book](https://www.amazon.com/dp/059652983X/?tag=mh0b-20&hvadid=78271540595342&hvqmt=b&hvbmt=bb&hvdev=c&ref=pd_sl_y7m3vu93e_b)
to learn it better). I stuck with Vim until I became a professonial
LISP developer, and the switch back to Emacs was impossible to ignore,
and obvious.

<a href="../../img/posts/emacs-config-evil-usepackage/vim.png"><img src="../../img/posts/emacs-config-evil-usepackage/vim.png" style="max-width: 100%; float: left; margin: 0px 15px 0px 0px;" alt="A Vim Window" /></a>

<div class="caption">The Vim editor</div>

Even after switching to back Emacs, I have still enjoyed using command
line applications like [cmus](https://cmus.github.io),
[ranger](https://github.com/ranger/ranger), and
[w3m](http://w3m.sourceforge.net), many of which are influenced by Vim
and often incorporate similar keyboard commands (at least the `j`,
`k`, `l`, `;` navigation). While it isn't ideal for everything (I
prefer to *write*, but not nessicarially *edit* code with emacs-syle
navigation), I never lost my love for the homerow-centric, and
efficient vim-style movement commands.


#### Best of Both Worlds

For the last two years, [Spacemacs](http://spacemacs.org/)'s default
Vim configuration has provided the best of both worlds. It had all of
the Evil packages pre-configured and optimized, but I could simply hit
`Ctrl-z`, and jump back to Emacs-mode.

Spacemacs was easy to use and I enjoyed it, but it really started to
have stability issues on my Windows 10 work computer. I thought that
going back to a stock emacs configuration may tone down the
complexity, and increase stability. I started to build a *new*
configuration based around `Evil`. During setup, I was happily
surpised to learn that the `Ctrl-z` option to switch back to
Emacs-mode was a default `Evil` behavior... so I still have the best of
both worlds!

#### Starting Config

Here is my starting `Evil` setup. I've nested other `use-pacages`
inside of it, so that if `evil` is configured, the packages that
depend on it go ahead and configure themselves too. I'm sure this will
grow over time as I add missing packages, but so far, it seems to
provde all the core functionality I need.

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

I think it needs more key bindings over time...

## Use Package

After my setting up an initial install of the Evil mode parts, I
discovered the amazing
[use-package](https://github.com/jwiegley/use-package). I have come
across it before reading blog posts, but never actually tried
it. After realizing how well it worked, I immediately combed through
my `.emacs` file, converting all of my `(require 'package-name)` calls
to `use-package` forms instead.

#### Setup

After ensuring the [MELPA](http://melpa.org) repos are added and
initialized:

```lisp
;; Add Melpa packages to Repos
(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))
(package-initialize)

```

The `use-package` package can be installed next. I wrapped the
install commands in an `unless`, so that when my emacs loads, it
only installs `use-package` if it is not already installed.

Afterwards, make sure to `(require 'use-package)`. It only needs to
happen during compile, so I have mine in an `(evail-when compile ...)`.

```lisp
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(eval-when-compile
  (require 'use-package))
```

I keep all of this at the top of my configuration, which works well
even when initializing a new computer.

#### Bye Bye emacs_init.el

When I last had my own custom emacs config, I had to also maintain an
`emacs_init.el` file. This was an emacs-lisp script that used a
`mapcar` to apply `#'package-install` across an ever-growing list of
emacs packages my configuration required. My goal was to have a
script, so that when configuring Emacs on a new system, I could just load
and evaluate the contents of `emacs_init.el`, and everything required
for `.emacs` would automatically install.

The reality was that it never fully worked. There were always a few
packages that would error, or that I had forgoten to add the last time
I updated my `.emacs` file. With `use-package`, this might be an issue
of the pastm, as it allows me to combine my emacs init script *with*
my configuration files.


#### Key Bindings

After convirting all of my `(require 'PACKAGE-NAME)` calls and related
expressions to filled `use-package` wrappers, I learned about the `:bind`
parameter. Instead of manually setting key binds with a `setq`,
`:bind` takes a list of dotted pairs and binds the function (defined
in the second spot of the pair), to the key sequence stated in the
first spot of the pair.

For example, to setup my preferred `ispell` key-bindings, I used the
following `:bind` parameter in my `ispell` `use-package` call:

```emacs-lisp
(use-package ispell
  :ensure t
  :bind
  (("C-c w" . 'ispell-word)
   ("C-c r" . 'ispell-region)))
   ```
   
This helps to keep the configuration a bit cleaner and organized. The
syntax is also straight-forward and easy to remember.


## System Specific Load Files

Finally, I moved all my work-specific emacs configuration (setting up
Allego Common Lisp, defining some helper functions... and anything
Windows specific) into it's own `emacs-work.el` file. With that in it's
own seperate file, I just needed to `load` it from my main `.emacs`
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
 overlaping use-cases. However, I already have to deal with that in a
 single configuration (which *section* to put it in), and my process
 of converting everyting to `use-package` has actually started to
 minimize that issue. So it might work...

## Next Steps

Now that I have an "`Evil`" Emacs setup configured, things should be
returning to business as usuall. As I work, I sure there'll be a
forgotten package here or there that needs to added. However, with
`use-package`, that should be a piece of cake, and easy to maintain
from here on out.
