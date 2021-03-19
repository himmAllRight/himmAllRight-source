+++
title   = "Jenkins Parallel Stashing"
date    = "2021-03-19"
author  = "Ryan Himmelwright"
image   = "img/posts/jenkins-parallel-stashing/pennsburg_sky.jpeg"
caption = "Pennsburg, PA"
tags    = ["jenkins", "devops", "containers"]
draft   = "True"
Comments = "True"
+++

I recently hit a snag while creating a Jenkins pipeline at work. I was having
difficulty preserving files across the entire pipeline run. In the end, my
solution was to use the stash feature. However, I found little support for my
specific type of issue online, so I figured I might as well write a short
post about my experience. 

<!--more-->

## Background

The pipeline runs an integration test suite I am working on. It contains
mostly sequential stages, but there are a few that run in parallel.
Specifically, there are provisioning and tear-down stages, that each run in
across the number of components we want to run the integration
testing with.

<a href="../../img/posts/jenkins-parallel-stashing/pipeline.png"><img alt="Pipeline stages" src="../../img/posts/jenkins-parallel-stashing/pipeline.png" style="max-width: 100%;"/></a>
<div class="caption">Pipeline stages</div>

The Jenkins instance is hosted on
[Openshift](https://www.openshift.com), and uses containers for the job
nodes. The pipeline uses several containers across the different stages,
which means that the local filesystem does not persist throughout the entire
pipeline. This was a problem, because we wanted to maintain the metadata files
from each of the provisioning stages, to use during the dynamic tests, as well
as during each tear down stage.

The issue is further complicated by the parallel provisioning stages. Each
provisioner runs in its own container, all at the same time. On top of that,
the number of provisioner/tear-down stages is dynamic. The pipeline might run
using data provisioners for components `A`, `C`, and `D`, in one run, and
`A`, `B`, `C`, `G`, and `H` for during next. It all depends on what
integration tests we want to perform. This meant that my solution also had to be dynamic and flexible.

## My Plan

I looked briefly into changing the containers' volume configuration, but my
proof of concept pipeline hit a silent failure right away (the pipeline would
endlessly hang, with no error). I decided to revisit that approach *if*
my next plan, implementing stash and un-stash, didn't work.

To simplify *what* to stash, and to have it work with the dynamically
changing parallel stages, I decided to try a *single* stash location. I made
a `metadata` directory that the stages could all write to and stashed it. My
thought was that I could then unstash it at the begging of the first stage in
each subsequent node, and re-stash the contents at the end of a node.

```groovy
sh "mkdir metadata"
sh "touch metadata/metadata_init" // Stash won't work with empty dirs
stash includes: 'metadata/', name: 'metadata', allowEmpty: true
```

```groovy
unstash 'metadata'
```

I added the calls to my pipeline, having everything write to a
`metadata` stash. It was a good idea, but there was a problem...

## *My* Problem

Because the stash is executed individually in parallel, only the files from
the *latest* parallel stage were being saved and stored.


## The Solution
As most solutions in software, the fix wasn't genius or even complicated. All
I really did was swapped my stash call to use the feature
*as intended*. Still, I had trouble finding *anything* online talking about
*using stash the way I needed to, so I thought I'd share.

```groovy
// Stash each builder's metadata if success
stash includes: 'metadata/', name: 'metadata-${testLabel}', allowEmpty: true
```

```groovy
// Un-stash all successful builder metadata into single dir
for(label in testLabel) {
    unstash "metadata-${label}"
}
```


My solution was to continue to use the single directory method, but *dynamically
change the name of the stash* during that initial parallel stage. It turns out,
that it only overwrote because they had the same stash name. I only needed to
parallel stash during the initial parallel stage, as the second one was at the end of
the pipleline where the metadata would no longer be appended. 

I guessed I could have multiple stashes, one for each para stage, and then
merge them into one location, that becomes *the* stash for the rest of the
pipeline. I thought merging shouldn't be too hard, and I could even write a
function to do it.

Before making things complicated by unmerging to a different location from
where I wanted `metadata` to be, I first decided to see what happens if I
just `unstashed` everything directly to the `metadata` dir. Luckily,
everything wrote to it fine, and merged itself with no overwrites. So... I
didn't have to do anything else. Problem Solved

## Conclusion

So that's it. Often, the solution to a seemingly complicated problem is a
simple one. This can be made more difficult if all of the online discussion
seems tangential, but not exactly what you need. In those cases, it is
probably best to pull aside a buddy to bounce ideas off of. Even if they
don't know how to immediately solve your problem, they can highlight problem
areas that you might be able to find a solution in. This is how this solution
surfaced. My buddy [Elyezer](https://elyezer.com) pointed out that the
stashes were being over-written *because* they had the same stash name. Even
though I *knew* that, having him re-emphasize it to me zoned my in and helped
me surface the idea of dynamically making different stashes and then merging
them for the rest of the pipeline.

Teamwork. It really effective! 

(P.S. Thanks Elyezer!)