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


<!--more-->

## Background

*Screenshot of example pipeline*

- Explain some background about the pipeline
  - It is multi staged
  - There are provisioning and tear-down stages that run in parallel
  - Different groups of stages run in different container nodes
  - This means that the data doesn't persist
  - We wanted to keep metadata from the setup functions, to use in testing and tear down stages


## My Plan
  - However, the metadata doesn't persist because of the different containers running
  - Additionally, the problem is complicated by the parallel running stages
    - These also change with each run. They aren't static.
  - I had two approaches
    1) Setting up the containers to use persistent volumes
    2) using jenkins stash/unstash
  - I looked quickly at the volumes, but they hit un-expressive issues right
  away, and I decided to come back to that if I couldn't get the stashing to
  work, since I thought the volumes might be more complicated to implement with our infrastructure.
  - To simplify what to stash, and to have it work with the dynamically
  changing parallel stages, I decided to try to stash a single `metadata`
  directory that I the stages could write to, I could stash it, and then unstash it at the start of the stage in a new node.
  - Good idea, but there was a problem...

## *My* Problem
- Because of how the stash is done in parallel, and individually, it meant that only the files of the latest was being saved and stored.


## The Solution
The solution wasn't a big "aha" moment, as it's really just using the feature as intended, but still, I had trouble finding anything online about how to do something like this, so I thought I'd share.

*Code Snippet of fixed solution*

My solution was to continue to use the single dir method, but dynamically
change the name of the stash for that initial parallel stage. It turns out,
that it only overwrote because they had the same stash name. I only needed to
do this for the inital parallel stage, as the second one was at the end of
the pipleline where no more metadata would be added. I figured I could have
multiple stashes, one for each para stage, and then merge them into one
location, that becomes *the* stash for the rest of the pipeline. I thought merging
shouldn't be too hard, and I could even write a function to do it. 

Before making things complicated by unmerging to a different location than
where I wanted `metadata` to be, I first decided to see what happens if I
just `unstashed` everything directly to the `metadata` dir. Luckily,
everything wrote to it fine, and merged itself with no overwrites. So... I
didn't have to do anything else. Problem Solved