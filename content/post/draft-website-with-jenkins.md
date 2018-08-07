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

### Project Setup

## A Nginx Server

## Configuring a Project

## Beter Yet... Pipelines

## Conclusion

In the future, could automate publication by deploying when that repo
is changed.
