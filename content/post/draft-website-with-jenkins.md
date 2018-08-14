+++
title    = "Creating a CI/CD 'Draft' Website with Jenkins"
date     = "2018-08-11"
author   = "Ryan Himmelwright"
image    = "img/header-images/atc-back1.jpg"
caption  = "American Tobacco Campus, Durham NC"
tags     = ["Linux", "Homelab", "Network", "Nginx", "Website", "DevOps", "Hugo"]
Comments = "True"
draft    = "True"
+++

Over the last few months I have been learning about the open source
automation server, [Jenkins](https://jenkins.io/). As I have digging
into it, I have been thinking of ways to improve my home
environment. One such way has been to utilize Jenkins to automatically
build and deploy a "drafts" website, so I can stage a new post/website
change on the home network, before publishing it to
"production".

<!--more-->

## My Website

<a href="../../img/posts/draft-website-jenkins/jenkins-logo.png"><img
src="../../img/posts/draft-website-jenkins/jenkins-logo.png" style="max-width:
50%; float: left; margin: 0px 12px 0px 0px;" alt="Jenkins Logo" /></a> 

As I have [previously written about](../website-transition-to-hugo/),
I [currenty generate my website](../website-switched-to-hugo/) using
the [Hugo](https://gohugo.io) static website generator. To organize
this system, I have two git repos: One that contains all the hugo
source files (where I write content), and one that contains the hugo
generated static website (that gets deployed to my web host).

When I am writting a post, I use `hugo server -D -F` to live view the
page in my browser. However, I often want to view the state of all the
*commited code* in the *repo*, to see what the site would look like if
I decided to publish a post. So, I created a "drafts" webstite, which
shows the current state of my website's *source* repo (including draft
and future posts). If I want to check how a post is looking on my
phone or any other device, I can just check the draft website after
pushing my changes.

<a href="../../img/posts/draft-website-jenkins/mr-mime.png"><img
src="../../img/posts/draft-website-jenkins/mr-mime.png" style="max-width:
45%; float: right; margin: 20px 0px 0px 10px;" alt="Jenkins Logo" /></a> 

## Jenkins

On my home network, I have created a dedicated Jenkins server
(Mr. Mime), using a CentOS7 VM hosted on my home server. However, any
Jenkins setup should work. To get started, checkout the [Jenkins
Website](https://jenkins.io/download/), and don't be afraid to browse
[the documentation](https://jenkins.io/doc/) for help.

*Note: make sure hugo is installed on the Jenkins server, as we need
it to generate the website.*


### Github Integration

#### Jenkins Service
My website is currently hosted on github, so we need to configure that
project to work with our Jenkins server. To do that, go to the
project's github page, and then click on **Settings** ->
**Integrations & services**. Click the **Add service** drop-down and
select *Jenkins (Git Plugin)*. Then, add the Jenkins server url
(assuming the server is accessable from the internet. If not, hosting
the jenkins server on something like [Digital
Ocean](http://digitalocean.com) might be a solution). Lastly, make
sure the **Activate** box is selected, and click the **Add Service**
button.

#### SSH Keys

While on the project's Github page, make sure that the Jenkins
server's ssh keys are added to the project. To add them, click on
**Deploy Keys**, again under the project's **Settings** tab. Then
select **Add deploy key**, and add the public key.

## A Nginx Server

<a href="../../img/posts/draft-website-jenkins/nginx.png"><img
src="../../img/posts/draft-website-jenkins/nginx.png" style="max-width:
100%; float: center; margin: 0px 0px 0px 0px;" alt="Default Nginx Page" /></a> 

With Jenkins ready, lets setup the web server before configuring the
Jenkins project. Any webserver will do, but I used
[nginx](https://nginx.org/en/) in my setup. It just needs to be able
to serve our generated *static* website. Just make sure it's installed
and running, and know *where* the files need to go. If using nginx, it
can be installed, enabled, and started with (on Ubuntu):

```bash 
## Install
sudo apt install -y nginx

## Check it is running
sudo systemctl status nginx
```

After installing, nginx will by default serve content at
`/user/share/nginx/html/`, so remember that location.

*Note: Don't forget to add the `jenkins` user's ssh key from the
jenkins server to the `authorized_keys` file of the nginx server. This
will make file transfers easier when setting up the jenkins project.*

## Configuring a Project

Lets configure our Jenkins project! Log in to the Jenkins
server and click the **New Item** option on the left side bar. Enter a
name for the project, select the **Freestyle Project** option, and hit
**OK**.

<a href="../../img/posts/draft-website-jenkins/general-config.png"><img
src="../../img/posts/draft-website-jenkins/general-config.png" style="max-width:
100%; float: center; margin: 0px 0px 0px 0px;" alt="The Project's General Configuration Section" /></a> 
<div class="caption">The Project's General Configuration Section</div>

In the **General** section of the configuration screen, optionally
write a description about the project. Next, select the "*GitHub
Project*" checkbox, and add the github repo's url into the *Project
url* text box.

#### Source Control

<a href="../../img/posts/draft-website-jenkins/credentials.png"><img
src="../../img/posts/draft-website-jenkins/credentials.png"
style="max-width: 100%; float: center; margin: 0px 0px 0px 0px;"
alt="Setting Credentials" /></a> 
<div class="caption">Setting Credentials</div>

In the **Source Code Management** section of the configuration, select
the *Git* option. Then, enter the repo's url (I did ssh url) for the
*Repository URL* box. For *Credentals*, click *Add* if they aren't
already setup. Select *SSH Username with private key* for *Kind*,
`jenkins` for the *Username*. 

More options can for the source control can be added here, but this
should be the minimum setup required. Again, for any of this to work
public keys for the `jenkins` user on the jenkins server must be
generated, and added as a deployment key on Github.

#### Build Trigger

Under the **Build Triggers** section, select *Poll SCM*. Without adding
any schedule parameters, it will just pull each time it detect a new
commit. This is what we want.

#### Build Step

In the **Build** section, click **Add build step**, and select
**Execute shell**. This is where we can add the shell commands to
build the website with hugo.

```bash
hugo -D -F -b "http://10.1.1.77" -d public
```

The `-D` tells hugo to include all draft posts, while the `-F` flag
has it include all posts with a future date. The `-b` flag sets the
url for the generated website. This sould the be url or ip address of
the nginx server setup previously. Lastly, the `-d` flag tells hugo to
output the generated static website to the `public` directory. This
will be useful to know when deploying the build.

#### Deploy to Webserver

Our deployment step will be another shell command, so I've actually
added it as another build step. So, add another **Execute shell**. I
used rsync to copy the build files to the nginx webserver:

```bash
rsync -r "$WORKSPACE/public/" ryan@10.1.1.77:/usr/share/nginx/html/
```

I used the jenkins `$WORKSPACE` variable to get the location of this
build, and was able to append the `public` directory to that, since we
defined it with the `-d` flag in the hugo build step above. This will
copy the generated website, to the webserver to be served.

Hit **Save**, and test it out by hitting the **Build Now** link on the
left. If the build is successfull, check the nginx website to see if
the website is deployed!

*Note: If it doesn't work, double check all permissions and
credentials between accounts and servers.*

## Beter Yet... Pipelines

What's better than using Jenkins for auto draft website deployments?
Using a Jenkins Pipeline:



## Conclusion

In the future, could automate publication by deploying when that repo
is changed.
