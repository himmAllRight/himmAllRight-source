+++
title  = "SQL Intro"
date   = "2018-04-16"
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

Select DB to use: `USE dbTest;`

### Tables

*After a DB is selected with `USE dbName;`...*

#### Show Tables

To show all of the tables in a database, just use `SHOW TABLES;`. For example:

```SQL
mysql> SHOW TABLES;
+------------------+
| Tables_in_dbTest |
+------------------+
| tblUsers         |
+------------------+
1 row in set (0.00 sec)
```

#### Create Table

To create a *new* table, use `CREATE TABLE`. The `CREATE TABLE` function takes
1) the name of the new table and 2) a list of the table fields (with their
types). For example, to create a user information table that contains a user's
first name, last name, age, and state, as well as an identification number, the
following SQL command can be used:

```SQL
mysql> CREATE TABLE tblUsers (id int PRIMARY KEY AUTO_INCREMENT, firstname varchar(50),lastname varchar(50), age INT,state varchar(2));
Query OK, 0 rows affected (0.01 sec)
```

The `first name`, `last name`, and `state` columns have a `varchar` data type,
which is essentially strings of various sizes (50 and 2 characters in this
case). The `id` and `age` columns have the `int` data type. However, note that
the `id` column has some other junk defined after the `int` identifier....

#### Constraints and Fields

In addition to specifying data *type*, other *constraints* can be imposed on
columns when defining a new table. Constraints are used to limit the type of
data that goes into the table, and can be implemented at the column or table
level. To see the fields of a table, use the `SHOW FIELDS FROM tablename`
command:

``` SQL
mysql> SHOW FIELDS FROM tblUsers;
+-----------|-------------|------|-----|---------|----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------|-------------|------|-----|---------|----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| firstname | varchar(50) | YES  |     | NULL    |                |
| lastname  | varchar(50) | YES  |     | NULL    |                |
| age       | int(11)     | YES  |     | NULL    |                |
| state     | varchar(2)  | YES  |     | NULL    |                |
+-----------|-------------|------|-----|---------|----------------+
5 rows in set (0.00 sec)

```

The `id` column uses the `PRIMARY KEY` and `AUTO_INCREMENT` constraints.
The `PRIMARY_KEY` constraint is a combination of the `NOT NULL` and `UNIQUE`
constraints, meaning it ensures that all the values in the column are different
and not `NULL`. The `AUTO_INCREMENT` field allows a unique number to be
generated, and automatically incremented during each table insert.


#### INSERT INTO

To actually *add* data into the table, the `INSERT INTO` command is used. As an
example, to add some users to the table created in the previous step:

```SQL
mysql> INSERT INTO tblUsers (firstname,lastname,age,state) 
VALUES ('Joe','Fry',32,'RI');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO tblUsers (firstname,lastname,age,state) 
VALUES ('Emily','Flanders',22,'CA');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO tblUsers (firstname,lastname,age,state) 
VALUES ('Tina','Oak',42,'NC');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO tblUsers (firstname,lastname,age,state) 
VALUES ('Bob','Builder',51,'MO');
Query OK, 1 row affected (0.01 sec)
```

Now, `tblUsers` should contain the information of the 4 users added. To check
this, use `SELECT * FROM tblUsers;` to select *everything* from the `tblUsers`
table:

```SQL
mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
|  8 | Bob       | Builder  |   51 | MO    |
+----|-----------|----------|------|-------+
4 rows in set (0.00 sec)

```

#### INSERT INTO Another Table
The `INSERT INTO` command mixed with `SELECT FROM`, can insert contents of *one
table* into *another*. This technique can be quite useful, and is a simple way to
create quick backups.


```SQL
mysql> CREATE TABLE tblUsersBackup (id int PRIMARY KEY AUTO_INCREMENT, firstname varchar(50),lastname varchar(50), age INT,state varchar(2));
Query OK, 0 rows affected (0.02 sec)

mysql> SELECT * FROM tblUsersBackup;
Empty set (0.00 sec)

mysql> INSERT INTO tblUsersBackup SELECT * FROM tblUsers;
Query OK, 4 rows affected (0.00 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM tblUsersBackup;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
|  9 | Bob       | Builder  |   51 | MO    |
+----|-----------|----------|------|-------+
4 rows in set (0.00 sec)
```

#### Drop (delete) Table

To delete a table, the `DROP` command is used. For example, to delete the table
from above, issue `DROP TABLE tblUsersBackup;`:

```SQL
mysql> DROP TABLE tblUsersBackup;
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT * FROM tblUsersBackup;
ERROR 1146 (42S02): Table 'dbTest.tblUsersBackup' doesn't exist
```

**NOTE: Using `DROP` commands will delete the entire structure (including the
schema), even if there is data in it. Be Careful!**


#### SELECT

In addition to selecting *all* of the data in a table using `SELECT *`, The
`SELECT` command can be utilized to select all sorts of combinations of the
data. Here are a few examples:

-- Select specific columns from the table:

``` SQL
mysql> SELECT firstname,lastname FROM tblUsers;
+-----------|----------+
| firstname | lastname |
+-----------|----------+
| Joe       | Fry      |
| Emily     | Flanders |
| Tina      | Oak      |
| Bob       | Builder  |
+-----------|----------+
4 rows in set (0.00 sec)

```

-- Grab column(s), after matching in another:

``` SQL
mysql> SELECT firstname,lastname FROM tblUsers WHERE state="RI";
+-----------|----------+
| firstname | lastname |
+-----------|----------+
| Joe       | Fry      |
+-----------|----------+
1 row in set (0.00 sec)
```

In addition to searching using `=` (which only grabs exact matches), other
operators, such as `>`, `<`, `<=`, `>=`, `<>` (not equal), `BETWEEN` (between an
inclusive range), and `LIKE` (search for pattern) can be used with the `WHERE`
clause. For example:

```SQL
mysql> SELECT firstname,lastname FROM tblUsers WHERE age>=25;
+-----------|----------+
| firstname | lastname |
+-----------|----------+
| Joe       | Fry      |
| Tina      | Oak      |
| Bob       | Builder  |
+-----------|----------+
3 rows in set (0.00 sec)

```

```SQL
mysql> SELECT firstname,lastname FROM tblUsers WHERE age BETWEEN 30 AND 50;
+-----------|----------+
| firstname | lastname |
+-----------|----------+
| Joe       | Fry      |
| Tina      | Oak      |
+-----------|----------+
2 rows in set (0.00 sec)

```


#### ALTER

To change the table schema (add, drop or modify columns), the `ALTER` command
can be used along with `ADD`, `DROP COLUMN`, or `MODIFY COLUMN` (respectively)
after the tablename. For example:

-- Add a `born` column to the table

```SQL
mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
|  9 | Bob       | Builder  |   51 | MO    |
+----|-----------|----------|------|-------+
4 rows in set (0.00 sec)

mysql> ALTER TABLE tblUsers ADD born year;
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------|------+
| id | firstname | lastname | age  | state | born |
+----|-----------|----------|------|-------|------+
|  5 | Joe       | Fry      |   32 | RI    | NULL |
|  6 | Emily     | Flanders |   22 | CA    | NULL |
|  7 | Tina      | Oak      |   42 | NC    | NULL |
|  9 | Bob       | Builder  |   51 | MO    | NULL |
+----|-----------|----------|------|-------|------+
4 rows in set (0.00 sec)

```

-- Change `born` column from a `year` data type to a `date`

```SQL
mysql> ALTER TABLE tblUsers MODIFY COLUMN born date;
Query OK, 4 rows affected (0.03 sec)
Records: 4  Duplicates: 0  Warnings: 0
```

-- Drop the `born` column from the table

```SQL
mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------|------+
| id | firstname | lastname | age  | state | born |
+----|-----------|----------|------|-------|------+
|  5 | Joe       | Fry      |   32 | RI    | NULL |
|  6 | Emily     | Flanders |   22 | CA    | NULL |
|  7 | Tina      | Oak      |   42 | NC    | NULL |
|  9 | Bob       | Builder  |   51 | MO    | NULL |
+----|-----------|----------|------|-------|------+
4 rows in set (0.00 sec)

mysql> ALTER TABLE tblUsers DROP COLUMN born;
Query OK, 0 rows affected (0.04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
|  9 | Bob       | Builder  |   51 | MO    |
+----|-----------|----------|------|-------+
4 rows in set (0.00 sec)
```

NOTE: Depending on the type of SQL database being used, the `MODIFY` command may
be `ALTER`.


#### Delete

First, we can delete all the *data* in a table with `DELETE * FROM tblName`,
*without* deleting the table schema. However, this is almost never used because
there are better commands to do that.


Specific items from the table can be removed using more specific `DELETE FROM`
commands:

``` SQL
mysql> SELECT * FROM tblUsersBackup;                                                                    
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
|  9 | Bob       | Builder  |   51 | MO    |
+----|-----------|----------|------|-------+
4 rows in set (0.00 sec)

mysql> DELETE FROM tblUsersBackup WHERE age>35;
Query OK, 2 rows affected (0.01 sec)

mysql> SELECT * FROM tblUsersBackup;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
+----|-----------|----------|------|-------+
2 rows in set (0.00 sec)
```

You can also use multiple criteria:

``` SQL
mysql> SELECT * FROM tblUsersBackup;                                                                    
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
|  9 | Bob       | Builder  |   51 | MO    |
+----|-----------|----------|------|-------+

mysql> DELETE FROM tblUsersBackup WHERE age>50 OR state="RI";
Query OK, 2 rows affected (0.00 sec)

mysql> SELECT * FROM tblUsersBackup;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
+----|-----------|----------|------|-------+
2 rows in set (0.00 sec)
```


#### Indexes

Speeds up access to getting values in a table. However, comes at a speed cost
for updating the table. Want to index columns or tables that are frequently
searched on. Want to have unique values as often as possible.

Use with `CREATE INDEX`. Again though, different dbs may have different
commands.

``` SQL
mysql> SHOW FIELDS FROM tblUsers;
+-----------|-------------|------|-----|---------|----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------|-------------|------|-----|---------|----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| firstname | varchar(50) | YES  |     | NULL    |                |
| lastname  | varchar(50) | YES  |     | NULL    |                |
| age       | int(11)     | YES  |     | NULL    |                |
| state     | varchar(2)  | YES  |     | NULL    |                |
+-----------|-------------|------|-----|---------|----------------+
5 rows in set (0.00 sec)

mysql> CREATE INDEX indexTblUsers ON tblUsers (id);
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

#### Drop Table


As we already know, you can drop the whole table:

However, like many things, `DROP` can be used with other specifications...

Some versions will use `ALTERTABLE tblCustomerIDInfo DROP INDEX
indexCustInfoID;`, while others may have a different command:

``` SQL 
mysql> ALTER TABLE tblUsers DROP INDEX indexTblUsers;
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
```
 
 
#### Truncate

The `truncate` command will delete the data, but leave table with names of
columns all the same... again, still be careful because it *will* delete all the
data in the table.

``` SQL
mysql> SELECT * FROM tblUsersBackup;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
+----|-----------|----------|------|-------+
2 rows in set (0.00 sec)

mysql> TRUNCATE TABLE tblUsersBackup;
Query OK, 0 rows affected (0.03 sec)

mysql> SELECT * FROM tblUsersBackup;
Empty set (0.00 sec)
```

#### Auto Increment

An Integer value, that once assigned, auto increments by 1 everytime the table
is updated.

You can auto increment a key. Very useful for IDs in a table.

``` SQL
mysql> SHOW FIELDS FROM tblPeople;
+-----------|-------------|------|-----|---------|----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------|-------------|------|-----|---------|----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| firstname | varchar(50) | YES  |     | NULL    |                |
| lastname  | varchar(50) | YES  |     | NULL    |                |
| age       | int(11)     | YES  |     | NULL    |                |
| state     | varchar(2)  | YES  |     | NULL    |                |
+-----------|-------------|------|-----|---------|----------------+
5 rows in set (0.00 sec)

mysql> INSERT INTO tblPeople (firstname, lastname, age, state) 
VALUES ('Josh', 'Rivers', 19, "PA");
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO tblPeople (firstname, lastname, age, state) 
VALUES ('Kim', 'Medows', 32, "CO");
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM  tblPeople;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  1 | Josh      | Rivers   |   19 | PA    |
|  2 | Kim       | Medows   |   32 | CO    |
+----|-----------|----------|------|-------+
2 rows in set (0.00 sec)

```

You can also set the auto increment value:

``` SQL
mysql> INSERT INTO tblPeople (firstname, lastname, age, state) 
VALUES ('Dan', 'Valley', 40, "NH");
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM  tblPeople;
+------|-----------|----------|------|-------+
| id   | firstname | lastname | age  | state |
+------|-----------|----------|------|-------+
|    1 | Josh      | Rivers   |   19 | PA    |
|    2 | Kim       | Medows   |   32 | CO    |
| 1000 | Dan       | Valley   |   40 | NH    |
+------|-----------|----------|------|-------+
3 rows in set (0.00 sec)
```

Just be careful when setting the auto increment value that it isn't set to
something that could eventually overwrite a value in a table that has to be
unique, or it will error.

### SQL Functions

SQL *functions*, are SQL statements that don't directly manipulate data, but can
be use to extract other useful information from the database and tables. They
are often used with the `SELECT`. There are a bunch base of SQL functions that
can used. Here are examples of a few:

#### COUNT

Shows us the result of a function was ask it to do. In this case, the count of
items fitting that criteria.

``` SQL
mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
|  9 | Bob       | Builder  |   51 | MO    |
+----|-----------|----------|------|-------+
4 rows in set (0.00 sec)

mysql> SELECT COUNT(*) FROM tblUsers;
+----------+
| COUNT(*) |
+----------+
|        4 |
+----------+
1 row in set (0.00 sec)

mysql> SELECT COUNT(*) FROM tblUsers WHERE age>35;
+----------+
| COUNT(*) |
+----------+
|        2 |
+----------+
1 row in set (0.00 sec)
```


#### Average and Sum Functions

To get an average of the numbers in a column, use the `AVG` function:

``` SQL
mysql> SELECT AVG(age) from tblUsers;
+----------+
| AVG(age) |
+----------+
|  36.7500 |
+----------+
1 row in set (0.00 sec)
```

To get a total, use the `SUM` function:

``` SQL
mysql> SELECT SUM(age) from tblUsers;
+----------+
| SUM(age) |
+----------+
|      147 |
+----------+
1 row in set (0.00 sec)
```

Note, that statements can  still be combined:

``` SQL
mysql> SELECT COUNT(*),AVG(age) from tblUsers;
+----------|----------+
| COUNT(*) | AVG(age) |
+----------|----------+
|        4 |  36.7500 |
+----------|----------+
1 row in set (0.00 sec)
```

### The Like Operator

The `LIKE` operator can be used for matching, with wildcards, `%`. For
example in the following searches, `%S` and `S%` yield different results because
the first looks for last names which *end* in an "s", and the second grabs last
names which *start* with "s".

Note, `LIKE` uses higher CPU usage. With larger data sets, try to use it on
columns which are indexed if possible.

``` SQL
mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
|  9 | Bob       | Builder  |   51 | MO    |
| 10 | Zach      | Scout    |   27 | NV    |
+----|-----------|----------|------|-------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM tblUsers WHERE lastname LIKE '%S';
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  6 | Emily     | Flanders |   22 | CA    |
+----|-----------|----------|------|-------+
1 row in set (0.00 sec)

mysql> SELECT * FROM tblUsers WHERE lastname LIKE 'S%';
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
| 10 | Zach      | Scout    |   27 | NV    |
+----|-----------|----------|------|-------+
1 row in set (0.00 sec)

mysql> SELECT * FROM tblUsers WHERE lastname LIKE '%er%';
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  6 | Emily     | Flanders |   22 | CA    |
|  9 | Bob       | Builder  |   51 | MO    |
+----|-----------|----------|------|-------+
2 rows in set (0.00 sec)
```


### Views

Views let you create a custom filter, and display set of the data. This can be
useful in difference scenarios. For example, a view can saved, and then just
*updated*, instead of *recalculated*, when querying for dash boards, or reports.

``` SQL 
mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
|  9 | Bob       | Builder  |   51 | MO    |
| 10 | Zach      | Scout    |   27 | NV    |
+----|-----------|----------|------|-------+
5 rows in set (0.00 sec)

mysql> CREATE VIEW myView AS SELECT COUNT(*), AVG(age), SUM(age) FROM tblUsers;
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT * FROM myView;
+----------|----------|----------+
| COUNT(*) | AVG(age) | SUM(age) |
+----------|----------|----------+
|        5 |  34.8000 |      174 |
+----------|----------|----------+
1 row in set (0.00 sec)

mysql> DELETE FROM tblUsers WHERE firstname='Bob';
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM myView;
+----------|----------|----------+
| COUNT(*) | AVG(age) | SUM(age) |
+----------|----------|----------+
|        4 |  30.7500 |      123 |
+----------|----------|----------+
1 row in set (0.00 sec)

```

### Joins

#### Inner Join

An Inner join will return the selected rows from multiple tables, when there is
at least one match in each table. For example:

``` SQL
mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
| 10 | Zach      | Scout    |   27 | NV    |
+----|-----------|----------|------|-------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM tblUsersPts;
+----|-----------|----------|-------|--------+
| id | firstname | lastname | team  | points |
+----|-----------|----------|-------|--------+
|  1 | Joe       | Fry      | Red   |  20000 |
|  2 | Emily     | Flanders | Blue  |  17000 |
|  3 | Tina      | Oak      | Red   |  32800 |
|  4 | Bob       | Builder  | Green |  40100 |
+----|-----------|----------|-------|--------+
4 rows in set (0.00 sec)

mysql> SELECT tblUsersPts.firstname, tblUsersPts.lastname, tblUsersPts.points
    -> FROM tblUsersPts INNER JOIN tblUsers
    -> ON tblUsers.lastname=tblUsersPts.lastname 
    -> AND tblUsers.firstname=tblUsersPts.firstname;
+-----------|----------|--------+
| firstname | lastname | points |
+-----------|----------|--------+
| Joe       | Fry      |  20000 |
| Emily     | Flanders |  17000 |
| Tina      | Oak      |  32800 |
+-----------|----------|--------+
3 rows in set (0.00 sec)
```

#### Right Join

A *right* join will give *everything* in the right table, and any existing/matched
items on the left, but will display as null for non matching data.

``` SQL
mysql> SELECT * FROM tblUsers;
+----|-----------|----------|------|-------+
| id | firstname | lastname | age  | state |
+----|-----------|----------|------|-------+
|  5 | Joe       | Fry      |   32 | RI    |
|  6 | Emily     | Flanders |   22 | CA    |
|  7 | Tina      | Oak      |   42 | NC    |
| 10 | Zach      | Scout    |   27 | NV    |
+----|-----------|----------|------|-------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM tblUsersPts;
+----|-----------|----------|-------|--------+
| id | firstname | lastname | team  | points |
+----|-----------|----------|-------|--------+
|  1 | Joe       | Fry      | Red   |  20000 |
|  2 | Emily     | Flanders | Blue  |  17000 |
|  3 | Tina      | Oak      | Red   |  32800 |
|  4 | Bob       | Builder  | Green |  40100 |
+----|-----------|----------|-------|--------+
4 rows in set (0.00 sec)

mysql> SELECT firstname, lastname, points FROM tblUsersPts 
-> RIGHT JOIN tblUsers ON tblUsers.lastname=tblUsersPts.lastname 
-> AND tblUsers.firstname=tblUsersPts.firstname;
+-----------|----------|--------+
| firstname | lastname | points |
+-----------|----------|--------+
| Joe       | Fry      |  20000 |
| Emily     | Flanders |  17000 |
| Tina      | Oak      |  32800 |
| NULL      | NULL     |   NULL |
+-----------|----------|--------+
4 rows in set (0.00 sec)
```

#### Left Join

Basically the same as a `RIGHT` join, but with the left table items all joining.


#### Full Join
A full join shows *all* records from both the right and left table, regardless
of matching the relation records of either.

NOTE: Full outer joins do not work on mysql, but would on postresql. It is
recommended to use Unions to emulate it.

### Unions

Unions are used to combine and concatenate `SELECT` statements from multiple
tables. 

This example doesn't work well because it doesn't make much sense (`age` isn't
the a `point`), at least it displays what is happening during the `UNION`.

``` SQL
mysql> SELECT firstname, lastname, points FROM tblUsersPts 
UNION SELECT firstname, lastname, age FROM tblUsers;
+-----------|----------|--------+
| firstname | lastname | points |
+-----------|----------|--------+
| Joe       | Fry      |  20000 |
| Emily     | Flanders |  17000 |
| Tina      | Oak      |  32800 |
| Bob       | Builder  |  40100 |
| Joe       | Fry      |     32 |
| Emily     | Flanders |     22 |
| Tina      | Oak      |     42 |
| Zach      | Scout    |     27 |
+-----------|----------|--------+
8 rows in set (0.00 sec)
```


### Sorting Records

Records can be sorted in the ascending or descending order of a column by using
the `ODER` command and either `ASC` for "ascending" or `DESC` for "descending".
Like always, the results can be limited or trimmed with a statement, like `LIMIT
1`.

``` SQL
mysql> SELECT * FROM tblUsersPts;
+----|-----------|----------|-------|--------+
| id | firstname | lastname | team  | points |
+----|-----------|----------|-------|--------+
|  1 | Joe       | Fry      | Red   |  20000 |
|  2 | Emily     | Flanders | Blue  |  17000 |
|  3 | Tina      | Oak      | Red   |  32800 |
|  4 | Bob       | Builder  | Green |  40100 |
+----|-----------|----------|-------|--------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM tblUsersPts ORDER BY points DESC LIMIT 3;
+----|-----------|----------|-------|--------+
| id | firstname | lastname | team  | points |
+----|-----------|----------|-------|--------+
|  4 | Bob       | Builder  | Green |  40100 |
|  3 | Tina      | Oak      | Red   |  32800 |
|  1 | Joe       | Fry      | Red   |  20000 |
+----|-----------|----------|-------|--------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM tblUsersPts ORDER BY team,lastname ASC;
+----|-----------|----------|-------|--------+
| id | firstname | lastname | team  | points |
+----|-----------|----------|-------|--------+
|  2 | Emily     | Flanders | Blue  |  17000 |
|  4 | Bob       | Builder  | Green |  40100 |
|  1 | Joe       | Fry      | Red   |  20000 |
|  3 | Tina      | Oak      | Red   |  32800 |
+----|-----------|----------|-------|--------+
4 rows in set (0.00 sec)
```

### Minimum and Maximum Values

Similar to `ORDER`, the minimum and maximum values in a particular column of the
table can be returned using the `MIN` and `MAX` commands:

```SQL
mysql> SELECT * FROM tblUsersPts ORDER BY team,lastname ASC;
+----|-----------|----------|-------|--------+
| id | firstname | lastname | team  | points |
+----|-----------|----------|-------|--------+
|  2 | Emily     | Flanders | Blue  |  17000 |
|  4 | Bob       | Builder  | Green |  40100 |
|  1 | Joe       | Fry      | Red   |  20000 |
|  3 | Tina      | Oak      | Red   |  32800 |
+----|-----------|----------|-------|--------+
4 rows in set (0.00 sec)

mysql> SELECT MIN(points),MAX(points)  FROM tblUsersPts;
+-------------|-------------+
| MIN(points) | MAX(points) |
+-------------|-------------+
|       17000 |       40100 |
+-------------|-------------+
1 row in set (0.00 sec)
```

To return other fields with the min/max item, a sub-query (another query inside
parenthesis) may have to be used:

```SQL
mysql> SELECT firstname,lastname,points FROM tblUsersPts 
-> WHERE points=(SELECT MAX(points) FROM tblUsersPts);
+-----------|----------|--------+
| firstname | lastname | points |
+-----------|----------|--------+
| Bob       | Builder  |  40100 |
+-----------|----------|--------+
1 row in set (0.00 sec)
```

### Upper and Lower Case Conversions

Strings (such as names), and be easily altered using functions like `UCASE` and
`LCASE`. These two functions change the *displayed* text (the data is not
altered) to be upper or lower case, respectively. Note: if staying compliant to
the SQL standard, there is SQL function to *alter* the actual *data* to upper or
lower case.

```SQL
mysql> SELECT * FROM tblUsersPts;
+----|-----------|----------|-------|--------+
| id | firstname | lastname | team  | points |
+----|-----------|----------|-------|--------+
|  1 | Joe       | Fry      | Red   |  20000 |
|  2 | Emily     | Flanders | Blue  |  17000 |
|  3 | Tina      | Oak      | Red   |  32800 |
|  4 | Bob       | Builder  | Green |  40100 |
+----|-----------|----------|-------|--------+
4 rows in set (0.01 sec)

mysql> SELECT UCASE(lastname),LCASE(firstname) FROM tblUsersPts;
+-----------------|------------------+
| UCASE(lastname) | LCASE(firstname) |
+-----------------|------------------+
| FRY             | joe              |
| FLANDERS        | emily            |
| OAK             | tina             |
| BUILDER         | bob              |
+-----------------|------------------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM tblUsersPts;
+----|-----------|----------|-------|--------+
| id | firstname | lastname | team  | points |
+----|-----------|----------|-------|--------+
|  1 | Joe       | Fry      | Red   |  20000 |
|  2 | Emily     | Flanders | Blue  |  17000 |
|  3 | Tina      | Oak      | Red   |  32800 |
|  4 | Bob       | Builder  | Green |  40100 |
+----|-----------|----------|-------|--------+
4 rows in set (0.00 sec)
```

### Now()

The `Now*()` function can create a new value, using the current date and time.
This can be appended when making a view, to mark when things happen over time.


```sql
mysql> SELECT id,firstname,lastname,team,points, Now() AS updated
    -> FROM tblUsersPts;
+----|-----------|----------|-------|--------|---------------------+
| id | firstname | lastname | team  | points | updated             |
+----|-----------|----------|-------|--------|---------------------+
|  1 | Joe       | Fry      | Red   |  20000 | 2018-04-17 10:56:53 |
|  2 | Emily     | Flanders | Blue  |  17000 | 2018-04-17 10:56:53 |
|  3 | Tina      | Oak      | Red   |  32800 | 2018-04-17 10:56:53 |
|  4 | Bob       | Builder  | Green |  40100 | 2018-04-17 10:56:53 |
+----|-----------|----------|-------|--------|---------------------+
4 rows in set (0.00 sec)
```
