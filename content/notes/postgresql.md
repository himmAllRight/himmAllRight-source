Notes for Postgresql

## Install

Just installed from the repos at first... was in Solus.

### Pulling down for latest

Went to [website](https://www.postgresql.org/download/linux/) and got commands
to pull down latest for Centos (I'm using an lxc container). The website has you
choose what system you are on, and customizes the commands for you, which is
nice :) .

#### Init DB

```
sudo /usr/pgsql-10/bin/postgresql-10-setup initdb
```

I wasn't sure how to do this on Solus, so I didn't...

#### Start/Enable service

```
sudo systemctl enable postgresql
sudo systemctl start postgresql
```

## Test out DB

#### Switch to postgres user

```
su - postgres
```

To quit: `\quit`

*Note: Might a shell for the user?

```
sudo usermod -s /bin/bash postgres
```

#### Connect to DB command lineup

```
psql
```

#### Change postgres password

```
\password postgres
```

#### Add admin pack for later

I couldn't get this to work... it might be not initializing my DB coming back to
haunt me...


Still can't get it to work...

```
postgres=# CREATE EXTENSION adminpack;
ERROR:  could not open extension control file "/usr/pgsql-10/share/extension/adminpack.control": No such file or directory
```

Figured it out!

Had to install `postgres-contrib`

## Creating DBs

in Bash:

```
createdb mytestdb
```

## Creating Tables


#### Create Table
```SQL
CREATE TABLE cities (
cityid varchar(5),
cityname varchar(80),
state varchar(20) );
```
#### Insert Values

```SQL
INSERT INTO citiies VALUES (
12345,
'Cincinnati',
'Ohio');
```
to see the table quickly:

```SQL
Select * FROM cities;
```

## Creating and Deleting Users

in BASH under postgres user:

create user
```bash
createuser mytestuser
```

create db with user name
```bash
createdb mytest
```

Set user password for authentication (in psql):

```SQL
ALTER USER mytestuser WITH PASSWORD 'password';
```

in Bash, set auth. Edit file `/var/lib/pgsql/10/data/pg_hba.conf`. Change the
Unix domain socket and IPv3 local connects to use the `password` method.

to apply setting, make sure to restart postgreql (from root/admin account, not
`postgres` user): `systemctl restart postgreql-10`.

Then, to log into with psql with the new user, `psql -U mytestuser`.

To remove user in bash, `dropuser mytestuser`. However, cannot delete user if it
owns tables/ other objects.
