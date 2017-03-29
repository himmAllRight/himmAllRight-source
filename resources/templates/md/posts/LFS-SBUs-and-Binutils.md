{:layout :post
:title  "Linux from Scratch - SBUs and Binutils"
:date "2017-03-28"
:author "Ryan Himmelwright"
:tags ["Linux" "LFS"]
:draft? false
}

Well, after all of the preparation, we are ready to start compiling some packages. This post won't go into compiling all the packages, but it will detail the first compilation of [Binutils](https://www.gnu.org/software/binutils/), which is one of the most important packages to compile. Why is compiling Binutils so crucial? It determines the SBU time for your build system. What's an SBU? Read on to find out!

<!-- more -->

### SBUs
When completing LFS, people commonly want to know how long it will take to compile the packages. Unfortunately, build times are very much dependent on the power and configuration of the system the packages are being compiled on. Some packages may only take a few minutes on a powerful workstation, but hours on an aged laptop. While we cannot say how long a specific build will take on any device, we can normalize how long each package build takes comparatively to each other. This normalization is done using Stand Build Units, or SBUs.

An SBU is the amount of time it takes to compile a standard package. Each package in the LFS book has a SBU value, so that compilation times can be gauged. So, if The first package to be compiled in the book (and in this post), is Binutils, so that is the package which SBUs are set against. For example, if it took 10 minutes to build Binutils on your machine, then for you, 1 SBU = 10 minutes. So, this means if a 4.5 SBU package is being compiled on that machine, it can be expected to take ~45 minutes to build.

#### SBU Accuracy
SBUs are not completely accurate, because there are still many factors that differ between setups. They should be used as an estimate at best, but remember that they could be off by dozens of minutes in worst-case scenarios.

For example, machines with multiple cores can run a "parallel make" by providing the `-j` makeflag, as in `make -j 4`. This allows the package to be compiled using multiple cores, potentially speeding up the build process significantly. However, due to how compilation jobs have to be divided for parallel builds, SBUs are even harder to predict and may be even more sporadic. Just remember that. Also, if you ever run into a problem during a build step, it is a good idea to first retry it with a single processor build. If this doesn't fix the issue itself, the error message can at least be properly analyzed.

### Building Notes



### Building BinUtils
It is important that Binutils is built first. This is mostly because when Glibc and GCC are built, they perform various tests on the linker and assembler to figure out which of their features to enable.

To start building BinUtils, first move to the sources directory (`$LFS/sources`) and extract the package.
