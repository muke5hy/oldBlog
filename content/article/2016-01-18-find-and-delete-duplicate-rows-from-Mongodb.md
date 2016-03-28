Title: Find and delete duplicate rows from Mongodb
Date: 2016-01-18 13:36:12.000000000 +05:30
Slug: find-and-delete-duplicate-rows-from-Mongodb
Authors: Mukesh
Modified: 
Category: programming
Tags: MongoDb 
Status: draft
Summary: 
	Finding and deleting duplicates documents from mongo collections using aggregation. 


Getting all the data
db.duplicate.drop();
db.scrip_data.aggregate([
  { $group: { 
    _id: { time: "$time", code: "$code", ltp:"$ltp" }, 
    uniqueIds: { $addToSet: "$_id" },
    count: { $sum: 1 } 
  }}, 
  
  { $match: { 
    count: { $gt: 1 } 
  }},
  {"$out": "duplicate"}
],{allowDiskUse:true});


db.duplicate.find({}).sort({count:-1}).forEach( function(data){
    if (data.uniqueIds.length > 1){
        data.uniqueIds.shift();
        print(data.uniqueIds.length);
        db.scrip_data.remove({"_id":{$in:data.uniqueIds}});
    }
    })