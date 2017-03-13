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


\* *Note: All of these commands should be run under the lfs user created in [the previous LFS post](../LFS-Getting-Started/), since that is the user account LFS will be built from.*

### Ensuring the $LFS Variable is *Always* Set
There are several ways to ensure that the *$LFS* variable. The book recommends editing the *.bash-profile* in both the home and */root/.bash_profile*, by adding the export command explained in the section above. This way every time the build machine is reset, simply logging into the system (which loads *bash*, assuming it's the default), will export the *$LFS* variable.

### Mounting the LFS Partition(s)
After setting the *$LFS* variable, I had to actually mount my LFS drive/partition to that location. I first ensured that the directory actually existed by running:

`mkdir -pv $LFS`

*Note: In this command, the -v again means verbose, so a message will be printed for each directory created. The -p flag is for --parents, and will allow mkdir to also make parent directories, as needed. So, if `/mnt/` does not already exist, will be created along with `/mnt/lfs`.*

After making the directories, I mounted them with the command:

`sudo mount ext4 /dev/sdb`

*In Ubuntu I could only mount the drive as root, so I did it from my <b>ryan</b> account, which has sudo privileges.*

If you are using multiple partitions for LFS (*ex: a separate `/home` partition*), they should also be mounted at this time.

After mounting my partition, the LFS book recommended that I check that the partition was not mounted with restrictive permissions. After running the `mount` again, but this time without any parameters, I was able to see and confirm that the partition was not mounted with restrictive permissions, such as `nosuid` or `nodev`. If either of these options are set, the partition needs to be remounted.

Lastly, if a *swap* partition is being used, do not forget to enable it using `swapon`:

`swapon -v /dev/xxx`  (with *xxx* the name of the swap partition)


### Conclusion
Remember, whenever the LFS host system is restarted, these steps must be completed upon logging into the rebooted system. If steps were taking to *always* complete these steps, even during reboot (such as adding the *$LFS* variable to the bash profile, or mounting the partitions in the *fstab* file), still check to make sure they *actually* set as  intended. This can prevent several headaches down the road.


<img src="../../img/posts/LFS-Repeated-Setup-Steps/Setting-LFS-var-play.png" name="pic" onclick=swap("../../img/posts/LFS-Repeated-Setup-Steps/Setting-LFS-var.gif")> 

</center>

