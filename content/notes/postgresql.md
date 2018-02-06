Notes for Postgresql

## Install

Just installed from the repos at first... was in Solus.

### Pulling down for latest

Went to website and got commands to pull down latest in Fedora (I'm in an lxc
container).

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

*Note: I had to add a shell for the user

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
