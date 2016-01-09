Title: XAMPP mod_rewrite , clean Url .htaccess 
Date: 2009-06-09 20:10
Author: Mukesh
Category: Apache, php, Xampp
Tags: .htaccess, Apache, Xampp
Slug: xampp-mod_rewrite-clean-url-htaccess
Status: published

Today every sites requirement is to have a user friendly URLs which can
be archived by .htaccess and apache. Since I'm running PHP I used XAMPP
. A default Xampp installation is lacking the mod\_rewrite
functionality. So to make the mod\_rewrite module working, we need to do
some tweak in Apache's httpd.conf file.

Since by default mod\_rewrite module is not enabled by default so I did
the following steps.

To enable mod\_rewrite in xampp first go to the directory of
installation \\apache\\conf and edit httpd.conf. Find the line which
contains  
\#LoadModule rewrite\_module modules/mod\_rewrite.so  
uncomment this(just remove \#, should be):

LoadModule rewrite\_module modules/mod\_rewrite.so

Also find AllowOverride None

Should be:

AllowOverride All

I really think it appears 2 or 3 times on the configuration file.

This setting is also required to get the clean\_url module to function
in drupal.

now restart the server and you are done.

Happy xampping!
