{:layout :post
:title  "Updating the Pi Cluster with Ansible"
:date "2017-05-23"
:author "Ryan Himmelwright"
:tags ["Homelab" "Cluster" "Pi" "DevOps" "Ansible"]
:draft? false
}

With Ansible configured on the Pi cluster, it's time to get it to do something useful. When working with a clustered system, even simple tasks can become tedious and time consuming. Once such task is updating the system. While I could manually update each of the 3 pi nodes, it isn't really scalable with 10 or 30 nodes, let alone 100. Tools like Ansible, make doing tasks like updating clustered systems, trivial again. In this post, I will walk through setting up an Ansible playbook to update my Pi cluster.

<!-- more -->

### Hosts File

### Ping Hosts

### Playbooks

### Apt Module

### Update Cluster Playbook
