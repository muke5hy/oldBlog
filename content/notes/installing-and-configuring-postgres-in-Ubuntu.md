Title: Installing and configuring postgress in ubuntu
Date: 2015-2-23 00:22:12.000000000 +05:30
Slug: installing-and-configuring-postgres-in-Ubuntu
Authors: Mukesh
Summary: 
Status: draft

sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

sudo -i -u postgres

You can get a Postgres prompt immediately by typing:

psql

Exit out of the PostgreSQL prompt by typing:

\q


We can create a new role (user_test) by typing:
createuser --interactive


You can create the appropriate database by simply calling this command as the postgres user:

createdb db_test


sudo -i -u user_test



create role myapp with createdb login password 'password';
