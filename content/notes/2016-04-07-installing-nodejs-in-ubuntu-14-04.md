Title: Installing nodejs in ubuntu 14.04
Slug: installing-nodejs-in-ubuntu-14-04
Date: 2016-04-07 12:35:55
Tags: nodejs, npm, installation
Category: notes
Author: mukesh
Lang: 
Summary: Installing nodejs and npm in ubuntu 14.04


There are few ways to install nodejs in Ubuntu, 
1. apt-get, 
2. compile it 
3. Use PPA 

I like the 3rd which is easy and it maintains latest version, I use NodeSource's PPA. To add PPA just execute the below line

```
    curl -sL https://deb.nodesource.com/setup | sudo bash -
```

After running the setup script from nodesource, you can install the Node.js package in the same way that we do in ubuntu

```
sudo apt-get install nodejs
```
