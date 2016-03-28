Title: "System program problem detected" on each startup Ubuntu  
Slug: system-program-problem-detected-on-each-startup-ubuntu
Date: 2016-03-24 11:43:17
Tags: Ubuntu
Category: ubuntu 
Author: Mukesh
Lang: 
Summary: "System program problem detected" on each startup Ubuntu    


After using ubuntu for a while, and if you keep on updating or upgrading your ubuntu. There are chances that you will face “System program problem detected” popup message on startup. 
 It’s very annoying to see the popups everytime you start your machine. Here is a solution to get rid of them.

### Finding out programmes which are responsible for popups 

Before getting rid of the problem its better to find out cause of the error. To check it you can do sudo ls -ltrh /var/crash/ , for me following are the issues.

    $ sudo ls -ltrh /var/crash/
    total 3.8M
    -rw-r----- 1 mongodb whoopsie 1.6M Mar 18 20:31 _usr_bin_mongod.120.crash
    -rw-r----- 1 root    whoopsie 469K Mar 19 21:34 susres.2016-03-19_21:34:39.781436.crash
    -rw-r----- 1 root    whoopsie 603K Mar 23 11:27 susres.2016-03-23_11:27:55.376655.crash
    -rw------- 1 root    whoopsie 209K Mar 23 11:40 mysql-server-5.6.0.crash
    -rw------- 1 root    whoopsie 275K Mar 23 12:03 mysql-server-5.5.0.crash
    -rw-r----- 1 root    whoopsie 634K Mar 24 11:34 susres.2016-03-24_11:34:14.141978.crash
    
As you can see in the result older crash files are also present. Hence they also poped up whenever system gets startup.

### Removing all the crash files, 

We can simply remove all the files and then good to go. And after removing you might get popup if new crash happens. 

    $ sudo rm /var/crash/*

If you want to remove all the popups in current session only with command you can do. 

    $ killall system-crash-notification

### Getting rid of popups forever, 

Apport system which does reporting for the crashes. Its not advisable to disable the Apport but even still you want to do it, here is how you can do.

    $ sudo vim /etc/default/apport

Change `enabled=1` to `enabled=0` , then save and exit.

    $ sudo restart apport

