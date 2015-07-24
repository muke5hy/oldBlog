Title: Mount disk permanently  in linux. (auto-mount disk)
Date: 2013-11-07 21:42:13.000000000 +05:30
Modified: 
Category: 
Tags: unix
Slug: mount-disk-permanently-in-linux-auto-mount-disk-2
Authors: 
Summary: 

To make the partition auto-mount.

1. Get your disk name 

        fdisk -l
 		
1. Find out the UUID of /dev/sda3 by doing:

		sudo blkid   
		sudo vim /etc/fstab
    
2. Now add add a line to the bottom of that file. It should look something like this (UUID will be different):

		UUID=03ec5dd3-45c0-4f95-a363-61ff321a09ff /works ext4 defaults  0      2

Now to check whether its working run 

		sudo mount -a
