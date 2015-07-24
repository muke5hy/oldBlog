Title: Allowing ubuntu user to access www folder amazon aws
Date: 2013-12-11 23:53:39.000000000 +05:30
Modified: 
Category: 
Tags: aws
Slug: allowing-ubuntu-user-to-access-www-folder-amazon-aws
Authors: 
Summary: 

sudo apt-get install apache2

sudo a2enmod rewrite

sudo apt-get install libapache2-mod-php5



sudo /etc/init.d/apache2 restart

sudo adduser ubuntu www-data
sudo chown -R www-data:www-data /var/www
sudo chmod -R g+rw /var/www
