Title: Execute linux command in background or Execute Commands After You Exit From a Shell Prompt
Date: 2013-12-25 17:22:13.000000000 +05:30
Modified: 
Tags: unix
Slug: execute-linux-command-in-background-or-execute-commands-after-you-exit-from-a-shell-prompt
Authors: 
Summary: 

Problem: After running a command on remote server some time you need to close your terminal or pc or the command takes too much time to process and you cant wait for completion. 

for such problems you would want to run the command in background to do so we have **nohup**.

From Man page it says 

	nohup - run a command immune to hangups, with output to a non-tty
    
You use nohup 

	nohup command-name &

Please note **&** it is required to run the command in background. 
Example 

	nohup tar -cvz file.tar.gz folder1 folder2 &
The above command will compress the folders in background and even if you close your local terminal the process will run in background. 
