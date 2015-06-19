Title: mongo.php not Found (cli)
Date: 2013-11-05 13:45:28.000000000 +05:30
Slug: mongo-php-not-found-cli

Its common to get an error stating mongo.php not Found after installing mongo driver for php.   
To get rid of the error add 

	extension=mongo.so 

in your php.ini file 

If you are running mongodb via cron or cli you need to also add into 

	/etc/php5/cli/php.ini
