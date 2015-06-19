
Changing Mysql data directory require change to AppArmor

After a bit of googling and hair-pulling, I realized that if I just changed the datadir directive in my.cnf will cause mysql start to fail on Ubuntu. The other thing is to add permissions to apparmor for mysql to access the new data directories.

Steps
1. sudo vi /etc/apparmor.d/usr.sbin.mysqld
2. Add
/newdir/ r,
/newdir/** rwk,
3. sudo /etc/init.d/apparmor restart
4. sudo /etc/init.d/mysql restart

If that still does not work, check the nix permissions to be sure mysql is owner and group for the new directory recursively.
chown -R mysql:mysql “new datadir path”

