{:layout :post
:title  "Linux from Scratch - Final Preparation Steps"
:date "2017-03-15"
:author "Ryan Himmelwright"
:tags ["Linux" "LFS"]
:draft? false
}


Now that the *repeated* setup steps have been defined in [previous LFS post](../LFS-Repeated=Setup-Steps/), there are a *few* more preparation steps to complete in order to start building the LFS system. I promise... we will start compiling soon. If all goes well, this should be the last preparation post.

<!-- more -->

### Downloading Sources
When it comes down to it, Linux from scratch is just the Linux kernel and a bunch of packages, compiled from source and linked together. To compile all of that, we need the source code... for all of those packages. Luckily, LFS keeps a list of what we need, and makes it simple to download all of it. *(Note: These commands should be run as <b>root</b>)*

<center>
![Making the sources directory](../../img/posts/LFS-Final-Preparation-Steps/make-sources-dir.png)
</center>

To make the directory:

`mkdir -v $LFS/sources`

The LFS wanted this directory to be writable, and sticky. A "Sticky" directory allows only the file owner to delete a file in the directory. To make the directory both writable and sticky, I used the command:

`chmod -v a+wt $LFS/sources`


<center>
<img src="../../img/posts/LFS-Final-Preparation-Steps/wget-sources-play.png" name="pic" onclick=swap("../../img/posts/LFS-Final-Preparation-Steps/wget-sources.gif")> 
</center>

To download all of the source packages at once, I first download [the LFS wget list](http://www.linuxfromscratch.org/lfs/view/stable-systemd/wget-list):


`wget http://www.linuxfromscratch.org/lfs/view/stable-systemd/wget-list`

After I had the wget list, I could use it as the input-file for wget, to download all the sources with one command:

`wget --input-file=wget-list --continue --directory-prefix=$LFS/sources`

It should take a few minutes to download everything (or longer if on a poor connection).


<center>
<img src="../../img/posts/LFS-Final-Preparation-Steps/sources-md5-play.png" name="pic" onclick=swap("../../img/posts/LFS-Final-Preparation-Steps/sources-md5.gif")> 
</center>


Since LFS-7.0, there is now a [md5sums file](http://www.linuxfromscratch.org/lfs/view/stable-systemd/md5sums) that can be downloaded and used to verify the downloaded packages.

### Creating the $LFS/tools Directory

### Adding the LFS User

### Setting up the Build Environment