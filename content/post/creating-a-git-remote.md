+++
title   = "Creating a git Repo Remote"
date    = "2017-07-19"
author  = "Ryan Himmelwright"
image   = "img/header-images/boston2.jpg"
caption = "Boston, MA USA"
tags    = ["git", "Linux", "dev",]
+++

For over a year or so, I have been using a
self-hosted [Gitlab](https://about.gitlab.com/) to host all of my private repos.
For a few months now, I have been meaning to migrate my Gitlab repos to bare, minimal
ones, hosted directly on a server. The majority of my code/configs are hosted
publicly on [my Github](https://github.com/himmAllRight) page, and it really
doesn't make sense to maintain a full Gitlab instance for the few (like...2)
private repositories that I keep. Moving the git repos to new ones right on the server
is actually fairly simple. For such a simple process, all the guides I saw
online went way above and beyond what I needed. So, here are the *two* steps I
did to migrate my repos.

<!--more-->

### SSH Keys
The *pre* (and somewhat optional) step to is to setup ssh key authentication. If ssh keys are not configured, git will prompt for the password of the repo's host user . When using a git service (ex: Github or Gitlab), this is usually unknown, so ssh keys are required. When rolling your own remote git repo, the password will likely be known. Still, setting up ssh authentication makes the process easier and more secure. If you
do not know how to configure ssh keys, I included a small ssh key how-to [here](/post/Ansible-On-Pi-Cluster/#ssh) in [a previous post](/post/Ansible-On-Pi-Cluster). Many of the git guides out there call for creating a `git` user and setting up ssh keys with that user. This is a great idea if multiple people need access to the git repo. However, for my purposes I will use my username, as I will be the only one accessing it (which in my case is a good thing).

### Creating Server Repo

<center>
<img src="../../img/posts/creating-remote-git-repo/init-bare-repo.png" name="bare init" onmouseover="this.src='../../img/posts/creating-remote-git-repo/init-bare-repo.gif'" onmouseout="this.src='../../img/posts/creating-remote-git-repo/init-bare-repo.png'" style="max-width: 100%;"/>
</center>
*Creating the remote git repo*

Once ssh authentication is configured, ssh into the remote server that will host the git repository. Creating the remote repo is a simple process. First, make a directory for the repo (the normal convention is to use a `.git` ending: `REPO-NAME.git`). Next, jump into the created directory (`cd`) and run the command `git init --bare`.

```
mkdir REPO-NAME.git
cd REPO-NAME.git
git init --bare
```


This will initialize the repository inside that directory. The `git init` command is used to create a git repository. The `--bare` option flag tells git to treat it as a bare repository. Bare repositories do not contain a working or checked out copy of the source files. Thus, the plain `git init` command creates a *working* repo, while `git init --bare` is used to create a *sharing(server) repo*. This allows the working repositories of many developers to be synced with the server repo.


### Cloning Repo

<center>
<img src="../../img/posts/creating-remote-git-repo/clone-new-remote.png" name="bare init" onmouseover="this.src='../../img/posts/creating-remote-git-repo/clone-new-remote.gif'" onmouseout="this.src='../../img/posts/creating-remote-git-repo/clone-new-remote.png'" style="max-width: 100%;"/>
</center>
*Clone the Remote to a Local Dir*

If the remote git repository is a totally new repository, it can be cloned down to a working directory on a developer machine fairly easily:

```
git clone user@hostname:REPONAME.git
```


### Pointing Local Repo to Server


<center>
<img src="../../img/posts/creating-remote-git-repo/point-to-new-remote.png" name="bare init" onmouseover="this.src='../../img/posts/creating-remote-git-repo/point-to-new-remote.gif'" onmouseout="this.src='../../img/posts/creating-remote-git-repo/point-to-new-remote.png'" style="max-width: 100%;"/>
</center>
*Pointing a working repo to the new remote*

However, I already had an existing working repository that I wanted to sync with the new remote shared repo. With the remote repo initialized, I wanted to point my existing git repository on the local machine to it. To do this, enter the directory of the git repository, and edit the config the (`.git/config`). To redirect the repo to point to the new remote, edit the `url` line to the location of the repo:

`username@hostname:reponame`

```
cd Server-Node-Files
vim ./git/config
```

After pointing to the new remote, feel free to push the content to it: (Only push everything (*) if it is desired)

```
git add *
git commit -m "First push to new Remote"
git push origin master
```

And that's it. Enjoy spinning up and using your own personal git repositories!

