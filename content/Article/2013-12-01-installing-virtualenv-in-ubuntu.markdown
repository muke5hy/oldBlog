Title: Installing virtualenv in ubuntu
Date: 2013-12-01 14:04:12.000000000 +05:30
Modified: 
Category: 
Tags: python
Slug: installing-virtualenv-in-ubuntu
Authors: 
Summary: 

Virtualenv is a tool to create isolated Python environments.

There is multiple ways to install virtualenv I'm gonna use one of the esiest way to install it. 

**Installing via pip :**

To install via pip you have to install pip 

	sudo apt-get install python-pip

check installed pip 

	which pip

Then install virtualenv 

	pip install virtualenv
    
Now check where virtualenv got isntalled

	which virtualenv
    
to create a enviroment run following line

	virtualenv ~/env/project --no-site-packages

env/project is a path where environment will get created. 

To activate environment 

	source ~/env/tweepy/bin/activate


  
