Title: Install latest Redis (3.0.2) in ubuntu 
Date: 2015-07-03 21:42:13.000000000 +05:30
Modified: 
Category: redis
Tags: ubuntu, redis
Slug: Install-latest-Redis-3.0.2-in-ubuntu 
Authors: mukesh
Summary: 

        Installing Redis





With all of the prerequisites and dependencies downloaded to the server, we can go ahead and begin to install redis from source:

Download the latest stable release tarball from Redis.io.

wget http://download.redis.io/releases/redis-stable.tar.gz

Untar it and switch into that directory:

tar xzf redis-stable.tar.gz

cd redis-stable

Proceed to with the make command:

make

Run the recommended make test:

make test

Finish up by running make install, which installs the program system-wide.

sudo make install

Once the program has been installed, Redis comes with a built in script that sets up Redis to run as a background daemon.

To access the script move into the utils directory:

cd utils

From there, run the Ubuntu/Debian install script:

sudo ./install_server.sh

As the script runs, you can choose the default options by pressing enter. Once the script completes, the redis-server will be running in the background.

You can start and stop redis with these commands (the number depends on the port you set during the installation. 6379 is the default port setting):

sudo service redis_6379 start
sudo service redis_6379 stop

You can then access the redis database by typing the following command:

redis-cli

You now have Redis installed and running. The prompt will look like this:

redis 127.0.0.1:6379> 

