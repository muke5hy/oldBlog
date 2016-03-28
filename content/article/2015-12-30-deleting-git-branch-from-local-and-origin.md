Title: Deleting git branch from local and origin 
Date: 2015-11-20 13:36:12.000000000 +05:30
Slug: deleting-git-branch-from-local-and-origin 
Authors: Mukesh
Modified: 
Category: programming
Tags: git
Status: 
Summary: 
	Deleting branches from local and remote. 

## How to delete git branch from local and remote

for long running projects and projects which has continuous changes gets many unused branch over the period of time, 
and if you do not clean up your branches they keep on increasing some time more than 50+ or may be 100+

When you checkout a branch from remote (origin), it makes a copy locally and points it to the remote Branch. When you want to delete a branch it becomes necessary to remove it from both places as well as from other machine too. 



If you want to delete a branch quickfix, first checkout to the branch other than the branch to be deleted.

	git checkout other_than_branch_to_be_deleted 

Deleting the local branch:

	git branch -D quickfix

Deleting the remote branch:

	git push origin --delete quickfix

at this stage you have deleted branch from your local as well from remote. If you repository is being used on other machine you need to update their too.

	git remote prune <remote_name>

If your <remote_name> is origin then 

	git remote prune origin