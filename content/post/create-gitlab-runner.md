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
First, install the `gitlab-runner` package. This can be done from following the
instructions found
[here](https://docs.gitlab.com/runner/install/linux-repository.html).
*However*, I have been encountering issues installing it on my Fedora 30 VMs,
as this install method currently isn't supported for 30 yet. If installing on a
Fedora 30 node, skip down to the next section.

#### Add GitLab's Repo

```
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.rpm.sh | sudo bash
```

#### Install gitlab runner
```
sudo dnf install gitlab-runner
```

## (Alternative) Copr install

I've been having trouble on Fedora 30 with the normal install. Apparently as of
now the service they use for distribution doesn't support Fedora 30 yet. Check
out [this issue](https://gitlab.com/gitlab-org/gitlab-runner/issues/4401) for
more info. For now, I have been using the copr install posted in the comments
of that issue. However, first check if that issue is resolved first, as it
might change from the time of writing this post.

For the copr install, first enable the copr repo:

```
sudo dnf copr enable snecker/gitlab-runner -y
```

Next, install:

```
sudo dnf install gitlab-runner -y
```

#### Register the Runner

Instructions for registering the runner can be found
[here](https://docs.gitlab.com/runner/register/index.html).

```
sudo gitlab-runner register
```

Enter the coordinator URL (ex: `https://gitlab.com`)

Then, enter the *gitlab-ci* token for the runner.

<a href="/img/posts/create-gitlab-runner/gitlab-runner-settings.png">
<img alt="Gitlab Runner Settings" src="/img/posts/create-gitlab-runner/gitlab-runner-settings.png" style="max-width: 100%;"/></a>
<div class="caption">Gitlab Runner Settings Page</div>

To obtain a gitlab-ci token, got to **Admin Area** -> **Overview** ->
**Runners**. Then, on the right there should be a token to use during setup.

When the runner registrations asks for the token, use the "registration token"
listed in the "Set up a shared Runner manually" section.

Next, provide a short description for the runner, and then add a tag or two
for it (when prompted).

Lastly, enter the executor (what system on the runner *does* stuff). For now,
I've just been using `"shell"` for my needs, as these VMs are fully dedicated
to be used as runners.

Congrats, the runner should be registered! Now to set it up...

## Link to CI/CD Builds

## Test Run
