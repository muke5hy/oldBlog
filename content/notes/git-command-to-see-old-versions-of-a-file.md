Title: Git command to see old versions of a file. 
Slug: git-command-to-see-old-versions-of-a-file
Date: 2016-03-16 12:37:35
Tags: git, tip
Category: Git 
Author: Mukesh
Lang: 
Summary: 

Often we require to check the versions of the file changes git. There are method in git to do that, but there is other better way to do that.   


To view a file of a specific version, below command will show you 5th last commit of model.py
`
git show HEAD~5:auth/model.py
` 

To get the history of changes 
`
git log -p auth/model.py

# If you want to follow all the changes inclusing file name change you can give --follow option
git log -p --follow  auth/model.py
` 

If you not comforatble with terminal out put, you can use `gitk` or `gitg`

`
gitg auth/model.py

# or with follow 
gitg --follow  auth/model.py
` 
or 
`
gitk --follow auth/model.py
` 
