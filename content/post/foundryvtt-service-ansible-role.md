+++
title   = "Creating Systemd Unit Files using Ansible"
date    = "2020-07-30"
author  = "Ryan Himmelwright"
image   = "img/posts/foundryvtt-service-ansible-role/unc-campus.jpeg"
caption = "UNC-Chapel Hill Campus, Chapel Hill, NC"
tags    = ["Linux", "systemd", "Customization",]
draft   = "True"
Comments = "True"
+++


<!--more-->

## Creating the Ansible Role
- Create role's directory and touch files


## Defining Variables
- Fill out the defaults file with vars needed in template
- Look to see if there is an *actual* way to mark vars as required, or just use
    my hacky way...


## Making a Template
- Paste in service unit file contents as a template file
- Replace parameterized parts with the vars we defined


## Ansible Tasks
- Create tasks file
- Define the tasks to:
    - Setup for service (create dirs, etc)
    - create/move the file to the location
    - Start the service, open ports, and other post start tasks


## Conclusion

Wrap up, that's it.
