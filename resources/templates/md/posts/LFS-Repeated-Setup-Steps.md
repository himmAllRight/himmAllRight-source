{:layout :post
:title  "Linux from Scratch - Repeated Setup Steps"
:date "2017-03-09"
:author "Ryan Himmelwright"
:tags ["Linux" "LFS"]
:draft? true
}

During the Linux From Scratch process, there may be times when the build environment (computer, VM, chroot, whatever) must be restarted. If so, there are a few steps in the setup phase that have to be re-initialized. This post goes through those steps.

<!-- more -->


### Setting The $LFS Variable
After the virtual disk for my LFS build, I needed to define where I wanted to eventually mount it. This location is important, because it will also be the path that the $LFS variable is set to. The $LFS variable is used throughout the book, to easily point to where the LFS system is being built.

<center>[![Setting the LFS variable](../../img/posts/LFS-Repeated-Setup-Steps/Setting-LFS-var.png)](../../img/posts/LFS-Repeated-Setup-Steps/Setting-LFS-var.png)</center>

To set the #LFS variable, I ran the following command: *

`export LFS=/mnt/lfs`

To check that the variable set correctly, just printed it out using echo (this should print out the path that was specified).

`echo $LFS`


\* *Note: All of these commands should be run under the lfs user created in [the last LFS post](../LFS-Getting-Started/), since that is the user account LFS will be built from.*