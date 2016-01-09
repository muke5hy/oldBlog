Title: How to install Django on ubuntu with apache and php?
Date: 2010-04-23 18:35
Author: Mukesh
Category: Uncategorized
Slug: how-to-install-django-on-ubuntu-with-apache-and-php
Status: published

Was just going through python in morning and thought lets try out Django
Framework. Django is very popular web framework for python, Its MVC
pattern. So just wanted to give a try to django. I have lappy I have
ubuntu 9.04 installed and as I'm PHP developer I have already installed
apache and php.

To install on Django on your current apache2 just follow the following
commands.

    sudo apt-get install libapache2-mod-python python-django python-django-doc

Now open this file in vim or gedit

    sudo vim /etc/apache2/sites-available/django-example

and add these lines

    <Location "/">
        SetHandler python-program
        PythonHandler django.core.handlers.modpython
        PythonDebug On
        PythonPath "['/usr/share/doc/python-django-doc'] + sys.path"
        SetEnv DJANGO_SETTINGS_MODULE examples.settings
    </Location>

Now disable your default setting

    sudo a2dissite default

Now enable Django example  and then reload the apcahe2

    sudo a2ensite django-example
    sudo /etc/init.d/apache2 reload

You can toggle between PHP and Django Now to use php again

    sudo a2dissite django-example
    sudo a2ensite default
