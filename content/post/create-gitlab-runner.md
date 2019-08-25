+++
title  = "Setup a Runner VM for Gitlab"
date   = "2019-08-27"
author = "Ryan Himmelwright"
image  = "img/posts/back-on-org-mode-for-work/eno-rocks.jpg"
caption= "Eno State Park, Durham NC"
tags   = ["Linux", "Homelab", "Git", "KVM", "DEV", "Devops", "Fedora"]
draft  = "True"
Comments = "True"
+++


<!--more-->

## What/Why

## Setup a Machine/VM

### Pre-req's
- Need an instance url?

- If using docker runners, need `docker-machine` installed.

## Install runner
From the instructions found
[here](https://docs.gitlab.com/runner/install/linux-repository.html)

#### Add GitLab's Repo

```
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh | sudo bash
```

#### Install gitlab runner
```
sudo dnf install gitlab-runner
```

#### Register the Runner

Instructions for registering the runner can be found
[here](https://docs.gitlab.com/runner/register/index.html).

```
sudo gitlab-runner register
```


## Setup API key

## Link to CI/CD Builds

## Test
