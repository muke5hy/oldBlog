Title: not able to login in magento? 
Date: 2009-03-25 19:38
Author: Mukesh
Category: magento
Tags: magento, php
Slug: not-able-to-login-in-magento
Status: published

I have moved my blog to [makdotgnu.com](http://www.makdotgnu.com/ "makdotgnu")
------------------------------------------------------------------------------

 

**A simple tweak**  
This is a question I was asking every here and there on forums, from
last 2 days but finally got the solution.  
Magneto has a Good security.  
According to this some url are block for admin, so if you are using any
domain name or http://localhost/ then just use the IP address of that
server, in case of localhost just use 127.0.0.1 instead of localhost,
Now your Url will look like on Local  
http://127.0.0.1/magnetofolder/index.php/admin  
and on your server.  
http://server\_IP/index.php/admin
