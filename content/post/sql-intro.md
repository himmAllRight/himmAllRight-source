+++
title  = "SQL Intro"
date   = "2018-03-14"
author = "Ryan Himmelwright"
image  = "img/header-images/baltimore-dock-gray.jpg"
tags   = ["DevOps", "Linux", "Database",]
draft  = true
+++

After putting postgresql on pause for a bit, I have switched our rue-rss app to
use SQLite3. In doing so, I figured it would be useful to finally dig in and learn some SQL.

<!--more-->

## Install Setup

Started with mysql for some testing. Went to the [mySQL download
Page](https://dev.mysql.com/downloads) and installed the version for me VM. This
may differ based on Distro/DB.

Update... can't get `/usr/bin/mysql_secure_installation` command to run...
getting a permission denied issue...

I think I figured it out... the first time mysql is run it creates a temp
password in the log, located at `/var/log/mysqld.log`. Lets test it out.

It worked. I guess that's something that's out of date from my tutorial video...

## create user

From shell: `mysql -u root -p mysql`, where `-u` is for the user, and `-p` is
for the DB to connect to.

## DBs and Commands:

Generally, SQL commands are typed in all CAPS. Also, statements end with a `;`
to terminate.

Show databases: `SHOW DATABASES;`

Create database: `CREATE DATABASE dbTest;`

Drop a database (delete): `DROP DATABASE dbTest`

Select DB to use: `USER dbTest;`

### Tables

Show Tables: `SHOW TABLES;`

Create Table: `CREATE TABLE tblCustomerInfo (custInfoFirstName varchar(50),custInfoLastName varchar(50),custInfoAddr1 varchar(50),custInfoAddr2 varchar(50).custInfoCityName varchar(50),custInfoState varchar(10),custInfoZipCode varchar(10),custInfoPhone varchar(12));`

Drop (delete) Table: `DROP TABLE tblTest;`

**NOTE: Using `DROP` commands will delete the entire structure, even if there is
data in it. Be Careful!**


