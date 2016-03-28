Title: Updating data in query with forEach
Date: 2015-11-04 17:36:12.000000000 +05:30
Slug: updating-data-in-query-with-forEach
Authors: Mukesh
Modified: 
Category: programming
Tags: mongodb
Status: 
Summary: 

        Updating data in query with forEach 

Since No-SQL does not have a structure or columns fixed when we store data into it, its very common or easy we insert unwanted keys into MongoDB. 
While developing some of the project I faced this issue as well. 

To resolve such situation we can manually update each document, if the task is very small we might just write one update query and remove the key or replace the value. The problem with this is if there is conditional update we might have to write separate query and update it. 

Since MongoDB uses V8 Javascript Engine we can use Javascript Language to write conditional queries. 


	db.product.find().forEach(function (unit){
	    if (unit.expiry_date <= new Date())
	    	unit.expired = true
	    db.listings.save(unit)
	})

The above code is self explanatory. Bottom line is if we want to edit in forEach we should create complete document and save it. 