+++
title   = "My New Dotfiles Management - Using GNU Stow"
date    = "2017-03-07"
author  = "Ryan Himmelwright"
tags    = ["Linux", "dotfiles",]
caption = "Rodney Bay, St Lucia"
image   = "/img/header-images/st-lucia-beach-feet.jpg"
+++


I have maintained a "dotfiles" repository since I made my github account in 2013. However, overtime it became more of a post-apocalyptic wasteland, cluttered with remnants of obsolete configurations and scraps of scripts. It was no longer the pristine, culled, collection that I desired. I also did not have an efficient method of easily linking the files on a new system. I had to manually make symlinks for each dotfile. I knew there were *much* better dotfiles setups out there, but I never got around to it. Until now.

<!--more-->

One day, after reading [this post](http://brandon.invergo.net/news/2012-05-26-using-gnu-stow-to-manage-your-dotfiles.html), I finally decided to sit down and clean up my dotfiles directory. I wanted to re-organize it so that I could use [GNU Stow](http://freecode.com/projects/gnustow) to initialize my dotfiles. 

After setting it all up, I decided to just start from scratch with a [new repository](https://github.com/himmAllRight/dotfiles).

## Using Stow and dotfiles
If you haven't seen it before, I highly suggest reading the post I have linked above. But in the meantime, I can provide a quick summary of how my dotfiles are setup. 

<center><img alt="My Dotfiles Dir" src="../../img/posts/new-dotfiles/dotfiles.png" style="max-width: 100%;"/></center>

Each application has an associated sub-directory (ex: `dotfiles/emacs`), which contains all of the dotfiles/folders associated with that application. Structurally, I treat the items in each application directory as if they were in my `~`. For example, the `vim` sub-directory has my `.vimrc`, as well as the `.vim/colors/` directory. This is so that when I use stow, it will properly link them in `~`.

<center><img alt="Vim dotfiles directory" src="../../img/posts/new-dotfiles/vim-dots.png" style="max-width: 100%;"/></center>

When I setup my dotfiles on a new system, or install an application for which I already have dotfiles saved for, setting them up is as easy as typing:

 `stow application-dir` (ex: `stow vim`). 
 
GNU Stow then links the files under my home directory. In my vim example, this means symlinks are created for `~/.vimrc` and `~/.vim/colors/*`, pointing to their respective locations in `~/dotfiles/vim/`.

<center><img alt="Vim dotfiles in Home" src="../../img/posts/new-dotfiles/vim-home.png" style="max-width: 100%;"/></center>

I think this setup is brilliant. Initializing an application's directory is so simple, and I can choose to only initialize specific sub-directories.

In the future, I might make multiple branches of the repository, one for each of my computers, so I can maintain specific configurations. In theory, I could also just make different folders (ex `vim-laptop` and `vim-server`), but I like the branch idea better because it's a little easier for me to merge changes. We shall see. 

Anyway, that's the new setup. Enjoy :-D
