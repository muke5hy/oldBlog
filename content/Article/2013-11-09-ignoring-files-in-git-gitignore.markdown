Title: Ignoring files in git (.gitignore)
Date: 2013-11-09 12:32:10.000000000 +05:30
Modified: 
Category: 
Tags: git
Slug: ignoring-files-in-git-gitignore
Authors: 
Summary: 

**Problem**: You want to ignore few folders or files from your git repository

**Solution**: Add a .gitignore file in your root project folder(even you can add this to your spesific folder too).

To ignore .htaccess in your repository, add .htaccess in your **.gitignore** file.

	.htaccess

To ignore all uploaded files from upload folder but not the upload folder add
	
	uploads/*

Suppose you have images folder in your upload directory and you want to add this to revision. your .gitignore file will look like 

	!uploads/images
    uploads/images/*
Second line in above code will ignore all the images file in images folder. 

To exclude index.html and .htaccess add folowing line 

	!uploads/images/index.html
    !uploads/images/.htaccess


Now your .gitignore file will look like 


	.htaccess
    uploads/*
    !uploads/images
	uploads/images/*
    !uploads/images/index.html
	!uploads/images/.htaccess
    
    
**NOTE:** If your file or folder is already indexes you have to remove them first 

	git rm -r --cached config/config.js # this this remove config file form git 
    git rm -r --cached . # this will remove all the index files and folder 
