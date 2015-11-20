Title: Optimization of Mongo query, making cursor iteration fast.
Date: 2015-11-20 13:36:12.000000000 +05:30
Slug: optimization-of-mongo-query-making-ursor-iteration-fast
Authors: Mukesh
Modified: 
Category: optimization
Tags: MongoDB, Query Optimization 
Status: 
Summary: 
        

If you using a mongo, I'm sure you must have come across a situation where you want to do a iteration for .find() command in mongo. 
Querying a Mongo collection for few records will give you faster results, but if you data is more than than 20K-30K or millions and you want to do iteration over it its hell lot of time. 

Lets take an example say you have 1 Million records in your users collection and about 98% users a active, to get the result you will do 
  active_users = db.users.find({active:True})
Your above query will get the cursor, now here comes the problem. Mongo does not fetches records in above query it just gets the cursor. To get all the records you need iterate over it. 
	
	temp = []
	for user in active_users:
		if user.get('first_name'):
			temp.append(user.get('first_name'))

The above query will take about 12+ or around that to create temp list. 12 sec is too huge number for such an small task. (The seconds will differ depending on size of the documents you have in users collection)

Under the hood pymongo in this case is not getting all the records at once in fact it does not gets the results when you do .find() query. Once you start iterating it fetches data from Mongodb in batches. 

By default it has 4MB of document size, Maximum of 16MB data mongo can fetch from DB. 
                
to optimize our query we can do 

  active_users = db.users.find({active:True}).batch_size(2000)

Now again iterate over the active_users and see the magic happen. 