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

#### create user

From shell: `mysql -u root -p mysql`, where `-u` is for the user, and `-p` is
for the DB to connect to.


#### Installing MariaDB on Ubuntu
Going over the new videos, they actually explain a way to fix this. Also, there
is a section that talks about how MariaDB is kind of replacing mySQL because
people aren't sure what Oracle's game plan is.

Still should run the secure setup to make it a bit safer:
`mysql_secure_installation`.


## DBs and Commands:

Generally, SQL commands are typed in all CAPS. Also, statements end with a `;`
to terminate.

Show databases: `SHOW DATABASES;`

Create database: `CREATE DATABASE dbTest;`

Drop a database (delete): `DROP DATABASE dbTest`

Select DB to use: `USER dbTest;`

### Tables

Show Tables: `SHOW TABLES;`

Create Table: 

``` SQL
CREATE TABLE tblCustomerInfo (custInfoFirstName varchar(50),custInfoLastName varchar(50),custInfoAddr1 varchar(50),custInfoAddr2 varchar(50),custInfoCityName varchar(50),custInfoState varchar(10),custInfoZipCode varchar(10),custInfoPhone varchar(12));
```

Drop (delete) Table: `DROP TABLE tblTest;`

**NOTE: Using `DROP` commands will delete the entire structure, even if there is
data in it. Be Careful!**


#### Constraints

Show the fields and types for a table: `SHOW FIELDS FROM tblCustomerInfo;`

To add constraints to an item, they come after the type. EX: `CREATE TABLE
tblCustomerIDInfo (custID varchar(10) PRIMARY KEY,...` creates an ID values that
is a PRIMARY KEY meaning it is *unique* and *not null*. 

``` SQL
mysql> SHOW FIELDS FROM tblCustomerIDInfo;
+-------------------|-------------|------|-----|---------|-------+
| Field             | Type        | Null | Key | Default | Extra |
+-------------------|-------------|------|-----|---------|-------+
| custID            | varchar(10) | NO   | PRI | NULL    |       |
| custInfoFirstName | varchar(50) | YES  |     | NULL    |       |
| custInfoLastName  | varchar(50) | YES  |     | NULL    |       |
| custInfoAddr1     | varchar(50) | YES  |     | NULL    |       |
| custInfoAddr2     | varchar(50) | YES  |     | NULL    |       |
| custInfoCityName  | varchar(50) | YES  |     | NULL    |       |
| custInfoState     | varchar(10) | YES  |     | NULL    |       |
| custInfoZipCode   | varchar(10) | YES  |     | NULL    |       |
| custInfoPhone     | varchar(12) | YES  |     | NULL    |       |
+-------------------|-------------|------|-----|---------|-------+
9 rows in set (0.00 sec)
```

Add an item to the table using `INSERT INTO`:

``` SQL
mysql> INSERT INTO tblCustomerInfo (custInfoFirstname,custInfoLastName,custInfoAddr1,custInfoAddr2,custInfoCityName,custInfoState,custInfoZipCode,custInfoPhone) VALUES ('John','Smith','111 Main St','','Anytown','NY','43211','2123445533');
Query OK, 1 row affected (0.00 sec)
```

View table information using a `SELECT FROM`:

``` SQL
mysql> SeLECT * FROM tblCustomerInfo;
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| custInfoFirstName | custInfoLastName | custInfoAddr1 | custInfoAddr2 | custInfoCityName | custInfoState | custInfoZipCode | custInfoPhone |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| John              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123445533    |
| Jane              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123443833    |
| Jan               | Jones            | 111 Main St   |               | City             | OH            | 43200           | 2123447333    |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
3 rows in set (0.00 sec)
```

Can insert contents of one table INTO another, with the `INSERT INTO` command,
mixed with the `SELECT FROM`. Good for doing a quick backup.

``` SQL
mysql> INSERT INTO tblCustomerInfoBkup (custInfoFirstname,custInfoLastName,custInfoAddr1,custInfoAddr2,custInfoCityName,custInfoState,custInfoZipCode,custInfoPhone) VALUES ('June','Fill','1191 Oak St','','Allston','CA','90200','2127447333');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM tblCustomerInfoBkup;
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| custInfoFirstName | custInfoLastName | custInfoAddr1 | custInfoAddr2 | custInfoCityName | custInfoState | custInfoZipCode | custInfoPhone |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| June              | Fill             | 1191 Oak St   |               | Allston          | CA            | 90200           | 2127447333    |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
1 row in set (0.00 sec)

mysql> INSERT INTO tblCustomerInfoBkup SELECT * FROM tblCustomerInfo;
Query OK, 3 rows affected (0.03 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM tblCustomerInfoBkup;
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| custInfoFirstName | custInfoLastName | custInfoAddr1 | custInfoAddr2 | custInfoCityName | custInfoState | custInfoZipCode | custInfoPhone |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| June              | Fill             | 1191 Oak St   |               | Allston          | CA            | 90200           | 2127447333    |
| John              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123445533    |
| Jane              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123443833    |
| Jan               | Jones            | 111 Main St   |               | City             | OH            | 43200           | 2123447333    |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
4 rows in set (0.00 sec)
```

Can also select specific columns from the table:

``` SQL
mysql> SELECT custInfoCityName,custInfoState FROM tblCustomerInfo;
+------------------|---------------+
| custInfoCityName | custInfoState |
+------------------|---------------+
| Anytown          | NY            |
| Anytown          | NY            |
| City             | OH            |
+------------------|---------------+
3 rows in set (0.00 sec)
```

Can also grab a column, after matching in another:

``` SQL
mysql> SELECT custInfoLastName FROM tblCustomerInfo WHERE custInfoState='NY';
+------------------+
| custInfoLastName |
+------------------+
| Smith            |
| Smith            |
+------------------+
2 rows in set (0.00 sec)
```

Can use LIKE to search or a pattern in a field. =, has to match exactly. <> is
not equal. When using number values, can use < and >.
