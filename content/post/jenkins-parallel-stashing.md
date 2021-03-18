+++
title   = "Jenkins Parallel Stashing"
date    = "2021-03-15"
author  = "Ryan Himmelwright"
image   = "img/posts/m1-air-initial-thoughts/m1_air_header.jpeg"
caption = "Durham, NC"
tags    = ["jenkins", "devops", "containers"]
draft   = "True"
Comments = "True"
+++

Recently at work, I hit a snag while creating a Jenkins pipeline. I was
having trouble having metadata files persist across the entire pipeline. In
the end, the solution was for me to just use the stash feature, as it is
intended XD. However, I found little support for my issue online, so I
figured I might as well write a short post about my experience in case
someone else experiences a similar problem in the future.

<!--more-->

## Background

<a href="../../img/posts/jenkins-parallel-stashing/pipeline.png"><img alt="Pipeline stages" src="../../img/posts/jenkins-parallel-stashing/pipeline.png" style="max-width: 100%;"/></a>
<div class="caption">Pipeline stages</div>

So, this pipeline is basically running an integration test suite I am working
on. It contains mostly sequential stages, but there are occasional parallel
stages. Specifically, there is a provisioning and tear-down stage, and each
runs in parallel across the number of components we want to run integration
testing on.

Aditionally, our Jenkins instance is hosted on
[Openshift](https://www.openshift.com), and uses containers for the job
nodes. The containers being used change across different stages, which means
that the local filesystem does not persist throughout the entire pipeline.
This created a problem, as we wanted to keep metadata from the each
provisioning stage, to use for dynamic tests, as well as the tear down stages

The issue is further complicated by the parallel provisioning stages. Each
provisioner runs in it's own container, all at the same time. On top of that,
*which* provisioner stages that runs can be different during each pipeline
execution, as they are dynamic. The pipeline might run using data
provisioners *A*, *C*, and *D*, in one run, and *A*, *B*, *C*, *G*, and *H*
for the next, depending on what integration tests we want to run. This means
that my solution couldn't be one that only worked with a static environment.


## My Plan

I had two initial approaches to try out:

1) Set up the containers to use persistent volumes

2) Use the Jenkins stash/unstash functionality

I looked very briefly into changing the volume configuration, but my proof of
concept pipeline hit an un-expressive issues right away (it hung forever
without any log or indication why). I decided to come back to that *if* the
stashing method didn't work. I thought the volumes might be more complicated
to implement with our infrastructure.

To simplify *what* to stash, and to have it work with the dynamically
changing parallel stages, I decided to try and stash a *single* `metadata`
directory that the stages could all write to. My thought was that I could
then stash it, and unstash it at the begging of the first stage in each
subsequent node.

```groovy
sh "mkdir metadata"
sh "touch metadata/metadata_init" // Stash won't work with empty dirs
stash includes: 'metadata/', name: 'metadata', allowEmpty: true
```

```groovy
unstash 'metadata'
```

So, I added in the stash calls, having everything write to a `metadata`
stash. It was a good idea, but there was a problem...

## *My* Problem

Because of how the stash is done in parallel, and individually, it meant that
only the files of the *latest* parallel stage was being saved and stored.


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