+++
title  = "SQL Intro"
date   = "2018-03-14"
author = "Ryan Himmelwright"
image  = "img/header-images/container-building-umich.jpg"
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

Can change the table schema (Add or edit fields), the `ALTER` command can be
used.

``` SQL
ALTER TABLE tblCustomerInfoBkup DROP custInfoDOB varchar(10)
```

``` SQL
mysql> ALTER TABLE tblCustomerInfoBkup MODIFY custInfoDOB year;
Query OK, 4 rows affected (0.03 sec)
Records: 4  Duplicates: 0  Warnings: 0
```


NOTE: Depending on the type of SQL database being used, the command may be:

``` SQL
mysql> ALTER TABLE tblCustomerInfoBkup ALTER COLUMN custInfoDOB year;
```


#### Delete

First, we can delete all the *data* in a table with `DELETE * FROM tblName`,
*without* deleting the table schema. However, this is almost never used because
there are better commands to do that.


Specific items from the table can be removed using more specific `DELETE FROM`
commands:

``` SQL
mysql> SELECT * FROM tblCustomerInfoBkup;
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------|-------------+
| custInfoFirstName | custInfoLastName | custInfoAddr1 | custInfoAddr2 | custInfoCityName | custInfoState | custInfoZipCode | custInfoPhone | custInfoDOB |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------|-------------+
| June              | Fill             | 1191 Oak St   |               | Allston          | CA            | 90200           | 2127447333    |        NULL |
| John              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123445533    |        NULL |
| Jane              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123443833    |        NULL |
| Jan               | Jones            | 111 Main St   |               | City             | OH            | 43200           | 2123447333    |        NULL |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------|-------------+
4 rows in set (0.00 sec)

mysql> DELETE FROM tblCustomerInfoBkup WHERE custInfoState='CA';
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM tblCustomerInfoBkup;
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------|-------------+
| custInfoFirstName | custInfoLastName | custInfoAddr1 | custInfoAddr2 | custInfoCityName | custInfoState | custInfoZipCode | custInfoPhone | custInfoDOB |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------|-------------+
| John              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123445533    |        NULL |
| Jane              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123443833    |        NULL |
| Jan               | Jones            | 111 Main St   |               | City             | OH            | 43200           | 2123447333    |        NULL |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------|-------------+
3 rows in set (0.00 sec)
```

You can also use multiple criteria:

``` SQL
mysql> DELETE FROM tblCustomerInfoBkup WHERE custInfoState='John' AND custInfoLastName='Johnson';
Query OK, 0 rows affected (0.00 sec)
```


#### Indexes

Speeds up access to getting values in a table. However, comes at a speed cost
for updating the table. Want to index columns or tables that are frequently
searched on. Want to have unique values as often as possible.

Use with `CREATE INDEX`. Again though, different dbs may have different
commands.

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

mysql> CREATE INDEX indexCustInfoID ON tblCustomerIDInfo (custID);
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

#### Drop Table


As we already know, you can drop the whole table:

``` SQL
mysql> SHOW TABLES;
+--------------------------+
| Tables_in_dbCustomerInfo |
+--------------------------+
| tblCustomerIDInfo        |
| tblCustomerInfo          |
| tblCustomerInfoBkup      |
| tblTest                  |
+--------------------------+
4 rows in set (0.00 sec)

mysql> DROP TABLE tblTest;
Query OK, 0 rows affected (0.00 sec)

mysql> SHOW TABLES;
+--------------------------+
| Tables_in_dbCustomerInfo |
+--------------------------+
| tblCustomerIDInfo        |
| tblCustomerInfo          |
| tblCustomerInfoBkup      |
+--------------------------+
3 rows in set (0.00 sec)
```

However, like many things, `DROP` can be used with other specifications...

Some versions will use `ALTERTABLE tblCustomerIDInfo DROP INDEX
indexCustInfoID;`, while others may have a different command:

``` SQL 
mysql> DROP INDEX indexCustInfoID ON tblCustomerIDInfo;
Query OK, 0 rows affected (0.00 sec)
Records: 0  Duplicates: 0  Warnings: 0
```
 
 
#### Truncate

Delete the data, but leave table with names of columns all the same... again,
still be careful because it *will* delete all the data.

``` SQL
mysql> TRUNCATE TABLE tblCustomerInfoBkup;
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT * FROM tblCustomerInfoBkup;
Empty set (0.00 sec)
```

#### Auto Increment

An Integer value, that once assigned, auto increments by 1 everytime the table
is updated.

You can auto increment a key. Very useful for IDs in a table.

``` SQL
mysql> CREATE TABLE tblEmpInfo(empID int PRIMARY KEY AUTO_INCREMENT,empLastName varchar(50),empSSN varchar(11)); 
Query OK, 0 rows affected (0.01 sec)

mysql> SHOW FIELDS FROM tblEmpInfo;
+-------------|-------------|------|-----|---------|----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------|-------------|------|-----|---------|----------------+
| empID       | int(11)     | NO   | PRI | NULL    | auto_increment |
| empLastName | varchar(50) | YES  |     | NULL    |                |
| empSSN      | varchar(11) | YES  |     | NULL    |                |
+-------------|-------------|------|-----|---------|----------------+
3 rows in set (0.00 sec)

mysql> INSERT INTO tblEmpInfo (empLastName,empSSN) VALUES ('Smith','11112223344');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO tblEmpInfo (empLastName,empSSN) VALUES ('Jones','11199223344');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM tblEmpInfo;
+-------|-------------|-------------+
| empID | empLastName | empSSN      |
+-------|-------------|-------------+
|     1 | Smith       | 11112223344 |
|     2 | Jones       | 11199223344 |
+-------|-------------|-------------+
2 rows in set (0.00 sec)
```

You can also set the auto increment value:

``` SQL
mysql> ALTER TABLE tblEmpInfo AUTO_INCREMENT=1000;
Query OK, 0 rows affected (0.00 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> INSERT INTO tblEmpInfo (empLastName,empSSN) VALUES ('Banard','27199223344');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM tblEmpInfo;
+-------|-------------|-------------+
| empID | empLastName | empSSN      |
+-------|-------------|-------------+
|     1 | Smith       | 11112223344 |
|     2 | Jones       | 11199223344 |
|  1000 | Banard      | 27199223344 |
+-------|-------------|-------------+
3 rows in set (0.00 sec)
```

Just be careful when setting the auto increment value that it isn't set to
something that could eventually overwrite a value in a table that has to be
unique, or it will error.


To change a varchar column to an INT, if empty:

``` SQL
mysql> SELECT * FROM tblCustomerIDInfo;
Empty set (0.01 sec)

mysql> ALTER TABLE tblCustomerIDInfo MODIFY custID int AUTO_INCREMENT;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0
```


### SQL Functions

SQL statements that don't directly manipulate data, but are related to the
SELECT function.

#### COUNT

Shows us the result of a function was ask it to do. In this case, the count of
items fitting that criteria.

``` SQL
mysql> SELECT * FROM tblCustomerInfo;
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| custInfoFirstName | custInfoLastName | custInfoAddr1 | custInfoAddr2 | custInfoCityName | custInfoState | custInfoZipCode | custInfoPhone |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| John              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123445533    |
| Jane              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123443833    |
| Jan               | Jones            | 111 Main St   |               | City             | OH            | 43200           | 2123447333    |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
3 rows in set (0.00 sec)

mysql> SELECT COUNT(*) FROM tblCustomerInfo;
+----------+
| COUNT(*) |
+----------+
|        3 |
+----------+
1 row in set (0.00 sec)

mysql> SELECT * FROM tblCustomerInfo;
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| custInfoFirstName | custInfoLastName | custInfoAddr1 | custInfoAddr2 | custInfoCityName | custInfoState | custInfoZipCode | custInfoPhone |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| John              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123445533    |
| Jane              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123443833    |
| Jan               | Jones            | 111 Main St   |               | City             | OH            | 43200           | 2123447333    |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
3 rows in set (0.00 sec)

mysql> SELECT COUNT(*) FROM tblCustomerInfo;
+----------+
| COUNT(*) |
+----------+
|        3 |
+----------+
1 row in set (0.00 sec)
```


#### Average and Sum Functions

Starting out with a new test table:

``` SQL
mysql> SELECT * FROM tblItems;
+-------|----------|----------+
| empID | name     | numItems |
+-------|----------|----------+
|     1 | Person A |     2343 |
|     2 | Person B |    24573 |
|     3 | Person C |  4844573 |
|     4 | Person D |   234234 |
|     5 | Person E |   834234 |
|     6 | Person F |   783641 |
+-------|----------|----------+
6 rows in set (0.00 sec)
```

To get an average of the numbers in a column, use the `AVG` function:

``` SQL
mysql> SELECT AVG(numItems) from tblItems;
+---------------+
| AVG(numItems) |
+---------------+
|  1120599.6667 |
+---------------+
1 row in set (0.00 sec)
```

To get a total, use the `SUM` function:

``` SQL
mysql> SELECT SUM(numItems) from tblItems;
+---------------+
| SUM(numItems) |
+---------------+
|       6723598 |
+---------------+
1 row in set (0.00 sec)
```

Note again, statements can be combined:

``` SQL
mysql> SELECT COUNT(*),AVG(numItems),SUM(numItems) from tblItems;
+----------|---------------|---------------+
| COUNT(*) | AVG(numItems) | SUM(numItems) |
+----------|---------------|---------------+
|        6 |  1120599.6667 |       6723598 |
+----------|---------------|---------------+
1 row in set (0.00 sec)
```

### The Like Operator

The `LIKE` operator can be used to fix matching, with wildcards, `%`. For
example in the following searches, `%S` and `S%` yield different results because
the first looks for last names which *end* in an "s", and the second grabs last
names which *start* with "s".

Note, `LIKE` uses higher CPU usage. If possible, try to use it on columns which
are indexed.

``` SQL
mysql> SELECT *FROM tblCustomerInfo WHERE custInfoLastName LIKE '%s';
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| custInfoFirstName | custInfoLastName | custInfoAddr1 | custInfoAddr2 | custInfoCityName | custInfoState | custInfoZipCode | custInfoPhone |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| Jan               | Jones            | 111 Main St   |               | City             | OH            | 43200           | 2123447333    |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
1 row in set (0.00 sec)

mysql> SELECT *FROM tblCustomerInfo WHERE custInfoLastName LIKE 's%';
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| custInfoFirstName | custInfoLastName | custInfoAddr1 | custInfoAddr2 | custInfoCityName | custInfoState | custInfoZipCode | custInfoPhone |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
| John              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123445533    |
| Jane              | Smith            | 111 Main St   |               | Anytown          | NY            | 43211           | 2123443833    |
+-------------------|------------------|---------------|---------------|------------------|---------------|-----------------|---------------+
2 rows in set (0.00 sec)
```


### Views

Let you create a custom filter and display set of data to use. This can be
useful for difference scenarios. For example, the view can just be updated when
querying for dash boards, or reports, instead of going through everything.

``` SQL 
mysql> SELECT * FROM tblItems;                                                                   +-------|----------|----------+
| empID | name     | numItems |
+-------|----------|----------+
|     1 | Person A |     2343 |
|     2 | Person B |    24573 |
|     3 | Person C |  4844573 |
|     4 | Person D |   234234 |
|     5 | Person E |   834234 |
|     6 | Person F |   783641 |
+-------|----------|----------+
6 rows in set (0.00 sec)

mysql> CREATE VIEW myView AS SELECT COUNT(*),AVG(numItems),SUM(numItems) FROM tblItems WHERE numItems > 50000;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT * FROM myView;
+----------|---------------|---------------+
| COUNT(*) | AVG(numItems) | SUM(numItems) |
+----------|---------------|---------------+
|        4 |  1674170.5000 |       6696682 |
+----------|---------------|---------------+
1 row in set (0.00 sec)
```

### Joins

