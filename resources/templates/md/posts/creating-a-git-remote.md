{:layout :post
:title  "Creating a git Repo Remote"
:date "2017-07-10"
:author "Ryan Himmelwright"
:tags ["git" "Linux" "dev"]
:draft? false
}

I've been meaning to move my password-store repo to be just a simple self hosted
on. I don't need gitlab for all that. For as simple as the basic solution is,
all the guides I saw online went above and beyond what to do. It's like, 2 steps
so I'll quickly post them here.

<!-- more -->

Body

### SSH Keys
This step that should really be done is to setup ssh key authentication. If you
don't know how to do this, I included a small ssh key how-to [here](../Ansible-On-Pi-Cluster#ssh) in [a previous post](../Ansible-On-Pi-Cluster). Many of the git guides out there call for creating up a `git` user and setting up ssh keys for that user. This is a good idea if multiple people need access to the git repo, but for my purposes, I am the only one ever accessing it (Which is a good thing, since it's my password vault). So I just used 

###
