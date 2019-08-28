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
#### Some things to note/consider:

- Install packages required for pipeline
- If `sudo` required, manage the `gitlab-runner` user/group in `visudo`
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
<div class="caption">Gitlab Runner**s** Settings Page</div>

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

Now, it's time to link up the runner to a CI/CD job. This can be done with
tagging, but I currently just have one pipeline using my runners, so haven't
used the tags as much. Edit the runner by clicking the runner's `edit` icon.

<a href="/img/posts/create-gitlab-runner/runner-edit.png">
<img alt="Gitlab Runner Settings" src="/img/posts/create-gitlab-runner/runner-edit.png" style="max-width: 100%;"/></a>
<div class="caption">Gitlab Runner Edit Page</div>

In the runner edit menu, ensure that the "`Active`" checkbox is checked. I've
also checked the "`Run untagged jobs`" box for this runner. This will allow it
to pick up any job that does *not* have a tag. If the runner is to be assigned
to a *specific* project, that can be enabled/assigned below in the "`Restrict
projects for this Runner`" section.

## Test Run

To test out the runner, start a new build in a project! (Note, if there are
several runners setup 1) why are you reading this, 2) it might be a good idea
to pause the others to ensure the new one will run with the test).

I won't go into writing a `gitlab-ci.yml` now, but for my test I made an empty
demo repo with the following pipeline:

```
before_script:
  - whoami
  - pwd
  - sudo dnf update -y

build-base:
  stage: build
  script:
    - echo "Hello world!"
```

After committing it, a build kicked off with the new runner and finished
successfully!

*Note that the job indeed ran on `post-runner`, the runner I setup
specifically for this post*

<a href="/img/posts/create-gitlab-runner/pipeline-run.png">
<img alt="Gitlab Runner Settings" src="/img/posts/create-gitlab-runner/pipeline-run.png" style="max-width: 100%;"/></a>
<div class="caption">Gitlab Demo Job Run Results</div>

If the job is more complicated, more runs might have to be manually started
after tweaking the runner settings again. Pipelines can be manually started by
going to the project's `CI/CD->Pipelines` page via the side menu, and hitting
the `Run Pipeline` button.

## Conclusion
