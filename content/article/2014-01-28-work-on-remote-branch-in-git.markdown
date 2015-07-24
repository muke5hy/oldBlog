Title: Work on remote branch in Git
Date: 2014-01-28 12:00:58.000000000 +05:30
Modified: 
Category: Git
Tags: Git, 
Slug: work-on-remote-branch-in-git
Authors: Mukesh
Summary: 

Branching is too helpfull for a development. If some of your coworker has pushed a his local branch to remote branch and you want to make some changes to it you can do it by checkout. 

To check out his/her branch on your local machine you need to follow these

1. Get the remote branch in your machine 

		git fetch origin	
        
 Where **origin** is a **remote** server. Now when you will do `git branch -r` you can see all the branches which has been pushed to remote. 

2. Since you can not work someone else branch you have to checkout his branch to your local and then do modification. To do so you have to checkout his branch in your local branch.

		git checkout -b test origin/test
Above command will checkout test branch from `origin` remote and will create test branch in your local branch. 

Now you can commit and push to the remote branch. 

Happy pushing
