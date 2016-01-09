Title: Another app is currently holding the yum lock; waiting for it to exit... 
Date: 2009-05-03 18:48
Author: Mukesh
Category: Linux
Tags: Linux, Unix
Slug: another-app-is-currently-holding-the-yum-lock-waiting-for-it-to-exit
Status: published

From last few days trying My hands on fedora. 10, I must say its a cool
distro. Recently I was trying to install some software through yum, but
I constantly getting

Another app is currently holding the yum lock; waiting for it to exit...

error though I was not using yum any where else, but this crap was
coming every time when I run the command, After googling a bit finally
got the solution that I this error was coming coz there was something in
the yum.pid.  
We can this issue by two means  
**First**  
one killing the pid by doing follwing command.

` # ps aux | grep yum `

this command will show all the process with process id which is running
by yum. so now you can kill the process. Say process Id 31542 is using
the yum so you can do

`# kill -9 31542 or # kill 31542`

**Second:**

If above method doesn't work for you. you can remove the yum process
from the machine. Now the question arise where you will get the process
file. yum process resides in /var/run folder so simply type the
following command and hit enter.  
` # rm -f /var/run/yum.pid `

N.B. To run the above command you need to be in a sudoers list or a
root.
