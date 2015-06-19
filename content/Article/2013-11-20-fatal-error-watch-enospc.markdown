Title: ! 'Fatal error : watch ENOSPC'
Date: 2013-11-20 01:26:19.000000000 +05:30
Modified: 
Category: 
Tags: unix
Slug: fatal-error-watch-enospc
Authors: 
Summary: 

Recently while running nodemon for the first time  I got an error which states :- 

	Error: watch ENOSPC
    at errnoException (fs.js:1019:11)
    at FSWatcher.start (fs.js:1051:11)
    at Object.fs.watch (fs.js:1076:11)
    at Object.watchFileChecker.check (/usr/lib/node_modules/nodemon/nodemon.js:160:6)
    at ready (/usr/lib/node_modules/nodemon/nodemon.js:49:22)
    at /usr/lib/node_modules/nodemon/nodemon.js:63:11
    at ChildProcess.exithandler (child_process.js:641:7)
    at ChildProcess.EventEmitter.emit (events.js:98:17)
    at maybeClose (child_process.js:735:16)
    at Socket.<anonymous> (child_process.js:948:11)

Since Nodemon keeps a monitoring of all the files in your project, to restart the server if there is any change in files. 

Since its low for my project files I changed it to 524298 
    
    echo fs.inotify.max_user_watches=524298 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p


