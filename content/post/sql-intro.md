+++
title   = "SQL Intro"
date    = "2018-04-24"
author  = "Ryan Himmelwright"
image   = "img/header-images/container-building-umich.jpg"
caption = "Ross School of Business - University of Michigan, Ann Arbor, MI"
tags   = ["Linux", "Programming", "Dev", "Database", "SQL",]
+++

SQL is one of those technologies that which to be everywhere, but yet... I
somehow haven't *had* to use it for anything in school or at work. I know, I
know... it's quite a feat. Still, the pervasiveness of SQL-like databases argues
that I really *should* learn it. So I am.

<!--more-->

The main purpose of this website is to document some of the tech stuff I do in
my free time. This serves three purposes: 1) Organizing my thoughts into a post
enhances my learning, 2) I can easily refer back to the post to refresh my
memory in the future, 3) It's a good medium to share what I've learned with
others. 

This post is a prime example, as it didn't start out as a *post*, but a file of
the *notes* I took as I learned SQL basics. As I progressed, I realized all of
the accumulating information should be cleaned up and posted. So here we are.
I've redone the examples, and turned my shorthand blurbs into sentences, but if
this post still seems a bit different than previous ones (no images, more code
snippets than words)... that's because it's my learning notes with makeup
heavily applied. Enjoy.

## Install Setup

I first installed mysql, by going to the [mySQL download
page](https://dev.mysql.com/downloads) and getting the appropriate the version
for my VM (centos 7). This may differ based on Distro/DB.

*I'm not going to cover any of the installation steps, as this post is more about
the SQL language, not setting up the DB. Besides, I did this in mysql, but in
the future I'll likely look at using MariaDB anyway...*

I do however want to note this issue I encountered, so I don't stumble over it
in the future. At first, I couldn't get the `/usr/bin/mysql_secure_installation`
command to run due to a permission denied error...

Eventually, I learned that the first time mysql runs, it creates a temp password
in the log, located at `/var/log/mysqld.log`. Using that password, I was able to
login.


## DBs and Commands:

Conventionally, SQL commands are typed in all CAPS, and statements end with a
terminating `;`. The rest of this post contains some SQL functions, with
examples of how they are used.

#### Show databases

To display all of the available databases, use the `SHOW DATABASES;` command.
Note, some of the DBs displayed are ones generated for the database system. For
example, in the output below, *I* only created `dbCustomerInfo` and `dbTest`:

```SQL
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| dbCustomerInfo     |
| dbTest             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)
```

#### Create database 

To create a new database, use the `CREATE DATABASE` command. Simple.

```SQL
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| dbCustomerInfo     |
| dbTest             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

mysql> CREATE DATABASE shotLivedDB;
Query OK, 1 row affected (0.00 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| dbCustomerInfo     |
| dbTest             |
| mysql              |
| performance_schema |
| shotLivedDB        |
| sys                |
+--------------------+
7 rows in set (0.00 sec)

```

#### Drop a database (delete): 

As easy as it was to *create* that database, deleting, or *dropping* it is just
as effortless with the `DROP DATABASE command, so be careful!

```SQL
mysql> DROP DATABASE shotLivedDB;
Query OK, 0 rows affected (0.00 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| dbCustomerInfo     |
| dbTest             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)
```

#### Select DB

To select which db to use inside the mysql shell use... `USE`. For this
tutorial, I created a database named `dbTest` and selected it with `USE dbTest`.

### Tables

*Note: make sure to first select a DB to work with: `USE dbTest;`...*

#### Show Tables

To show all of the tables in a database, use `SHOW TABLES;`. For example:

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
1) the name of the new table, and 2) a list of the table fields (with their
data types). For example, to create a user information table that contains a user's
first name, last name, age, and state, as well as an identification number, the
following SQL command can be used:

```SQL
mysql> CREATE TABLE tblUsers (id int PRIMARY KEY AUTO_INCREMENT, firstname varchar(50),lastname varchar(50), age INT,state varchar(2));
Query OK, 0 rows affected (0.01 sec)
```

The `first name`, `last name`, and `state` columns have a `varchar` data type,
which are strings of various sizes (50 and 2 characters in this case). The `id`
and `age` columns have an `int` data type. Notice that the `id` column
has some other junk defined after the `int` identifier....

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
`PRIMARY_KEY` is a combination of the `NOT NULL` and `UNIQUE` constraints,
meaning it ensures that all values in the column are unique and not `NULL`. The
`AUTO_INCREMENT` field generates an unique number that is automatically
incremented during each insert to the table.


#### INSERT INTO

To actually *add* data to the table, the `INSERT INTO` command is used. As an
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

The `tblUsers` table should now contain the information of the 4 users added. To check
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

The `INSERT INTO` command combined with `SELECT FROM`, can insert contents of *one
table* into *another*. This technique can be quite useful, providing a simple way to
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

To delete a table, the `DROP` command is used. For example, to delete the backup
table from above, issue `DROP TABLE tblUsersBackup;`:

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
is used along with `ADD`, `DROP COLUMN`, or `MODIFY COLUMN` (respectively)
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
be known as `ALTER`.


#### Delete

All the *data* in a table can be removed using `DELETE * FROM tblName`,
*without* deleting the table schema. However, this is almost never used because
there are better commands to do that.


*Specific* items from the table can be removed using `DELETE FROM`
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

Multiple criteria can also be used to specify what to delete:

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

An index speeds up the data retrieval time of a table. However, this comes at a
speed cost for *updating* the table. So, it is usually a good idea to only index
columns or tables that are frequently searched on.

To add an index, use `CREATE INDEX`. *(Again, may differ depending on database
technology being used)*

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


As we already know, you can drop a whole table with `DROP`. However, like many
of the other commands, `DROP` can be used with other items, like an index:


``` SQL 
mysql> ALTER TABLE tblUsers DROP INDEX indexTblUsers;
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0
```
 
#### Truncate

The `truncate` command will delete the data, but leave table schema the same...
again, still be careful because it *will* delete *all the data* in the table.

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

You can auto increment a key, which is very useful for IDs in a table (as we saw
earlier).all the data

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

Note: The auto increment value can be manually set.

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

When setting the auto increment value manually, just be careful that it isn't
set to one that will eventually overwrite another value in the table that *must*
be unique, or it will error.

### SQL Functions

SQL *functions*, are SQL statements that don't directly manipulate data, but can
be use to extract other useful information from the database and tables. They
are often used in conjunction with `SELECT`. There are a bunch of base SQL
functions to use. Here is a sampling of a few:

#### COUNT

Shows the number of matched results returned. In this example, the number of
rows in `tblUsers`, and then the number of users over the age of 35:

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

To get an average of the number values in a column, use the `AVG` function:

``` SQL
mysql> SELECT AVG(age) from tblUsers;
+----------+
| AVG(age) |
+----------+
|  36.7500 |
+----------+
1 row in set (0.00 sec)
```

To get a total of a column's number values, use the `SUM` function:

``` SQL
mysql> SELECT SUM(age) from tblUsers;
+----------+
| SUM(age) |
+----------+
|      147 |
+----------+
1 row in set (0.00 sec)
```

Note, that select statements using functions can still be combined:

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

The `LIKE` operator can be used for matching, with wildcards (`%`). For example
in the following searches, `%S` and `S%` yield different results because the
first looks for last names which *end* in an "s", and the second grabs last
names which *start* with "s". The last example returns names which have "er"
anywhere in the last name.

*Note, `LIKE` uses higher CPU usage. With larger data sets, try to use it on
columns which are indexed if possible.*

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

Views create a custom filter to display a set of the data. This can be useful
when defining several use cases of an application. For example, a view can
saved, and then just *updated*, instead of *recalculated*, when querying for
dash boards, and/or reports.

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

A *right* join will return *everything* in the right table, and any existing/matched
items on the left. Any non-matching data will display as null.

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
recommended to use Unions to emulate them if needed.

### Unions

Unions are used to combine and concatenate `SELECT` statements from multiple
tables. 

This example doesn't work well because it doesn't make much sense (`age` isn't
the same as a `point`), but at least it displays what is happening during the `UNION`.

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

Record rows can be sorted in the ascending or descending order of a column by using
the `ODER` command and either `ASC` for "ascending" or `DESC` for "descending".
The results can be limited or trimmed using another statement, like `LIMIT
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

To return other fields with the min/max item, a sub-query (another SQL query
inside parenthesis) may have to be used:

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
altered) to be upper or lower case.

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

The `Now*()` function creates a new value, using the current date and time. This
can be appended when creating a view, to mark when changes happen over time.


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

## Conclusion

I think that is enough to at least get started with SQL :) (it was for me
anyway). There's not much else to say other than hopefully this post server as
a good SQL quick-reference down the road :). Enjoy!
