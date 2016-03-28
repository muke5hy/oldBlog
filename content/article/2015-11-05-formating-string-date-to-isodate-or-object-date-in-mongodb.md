Title: Formating String date to ISOdate or Object Date in MongoDB
Date: 2015-11-05 13:36:12.000000000 +05:30
Slug: formating-string-date-to-isodate-or-object-date-in-mongodb
Authors: Mukesh
Modified: 
Category: programming
Tags: mongodb
Status: 
Summary: 
        Formating String date to ISOdate or Object Date in MongoDB

MongoDB stores the date in ISODate format which is nothing but a wrapper for the Date object of Javascript. If some how your database has stored to string date, you can convert them to ISO by running following query directly in mongo terminal

	db.collection.find({"date_updated":{$type:2}})	  
	    .forEach( function(item){

            if (typeof(item.date_updated) == "string"){
                item.date_updated = new ISODate(item.date_updated);
            	db.items.save(item)
            }
	    }
	        
	})

