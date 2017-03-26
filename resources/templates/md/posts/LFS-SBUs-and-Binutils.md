{:layout :post
:title  "Linux from Scratch - SBUs and Binutils"
:date "2017-03-26"
:author "Ryan Himmelwright"
:tags ["Linux" "LFS"]
:draft? false
}

Well, after all of the preparation, we are ready to start compiling some packages. This post won't go into compiling all the packages, but it will detail the first compilation of [Binutils](https://www.gnu.org/software/binutils/), which is one of the most important packages to compile. Why is compiling Binutils so crucial? It determines the SBU time for your build system. What's an SBU? Read on to find out!

<!-- more -->

### SBUs