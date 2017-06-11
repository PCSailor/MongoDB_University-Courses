# Mongo Crud operations
# ------------------------------------------------------------------------------
# C reating
    insertOne()
    insertMany()
    upsert - Update commands
# ------------------------------------------------------------------------------
# R ead 
[Query & Projection Operators](https://docs.mongodb.com/manual/reference/operator/query/)
    // Documents_Scaler Fields, Embedded Documents-Fields containing nested documents, Arrays-Equality Matches (on entire array, on any element, a specific element, operator complex matches)
    db.sumCollection.find({ sumKey : "sumValue" }).pretty() # on entire array # finds all values
    
    db.sumCollection.find({ sumKey : "sumValue" }).count() # gives count of all values
    
    db.sumCollection.find({ sumKey01 : "sumValue01", sumKey02 : "sumValue02" }).count() # gives count matching all values
    
    db.sumCollection.find({ "sumKey.sumSub-Key" : "sumSub-Value" }).count() # using dot-notation to find a field of a document nested within fields within an array # dot-notaition works with fields in any level. # Must enclose the key in quotes
    
    db.sumCollection.find({ "sumKey" : ["sumValue01", "sumValue02"] }).pretty() # exact match within array of both values in this exact order  
    
    db.sumCollection.find({ "sumKey" : "sumValue" }).pretty() # on any element # finds sumValue located anywhere in all field values # NOTE: It is not necessary to use square brackets unless want to find an exact match within an array field.
    
    db.sumCollection.find({ "sumKey.0" : "sumValue" }).pretty() # a specific element, # finds sumValue located in a particular position within field values
   
    Cursor - Find method returns a cursor # to access documents, must iterate through the cursor # In the Mongo shell, if find return value is not assigned to a variable using var keyword, the cursor is automatically iterated up to 20 times to print an initial set of search results # MongoDB server returns query search results in batches with batch size not exceeding maximum BSON document size # For most querys, the first batch returns 101 documents or approximately 1MB # Subsequent batches will return 4MB # As iterate through cursor and reach end of return batch, if there are more results, 'cursor.next' preforms a get-more operation retrieving the next batch.
            
            var c = db.sumCollection.find(); # Assign the cursor to a variable
            var doc = function() { return c.hasNext() ? c.next() : null; } # function that uses cursor checking first for anymore results & if so getting the next ones, otherwise returning null
            c.objsLeftInBatch(); # use this method on the cursor object to check how many objects are left in the batch
            doc() # uses this to iterate through the batch
    
    Projection - used to limit fields returned by a query # to reduce the size of data returned for any query
        
        db.sumCollection.find({ sumKey01 : "sumValue01" }, { sumKey02 : 1 }).pretty() # will contain only documents with sumKey02
        
        db.sumCollection.find({ sumKey01 : "sumValue01" }, { sumKey02 : 1, _id: 0 }).pretty() # # will contain only documents with sumKey02 AND will omit objectID values (=much cleaner results)
        
        # With the key, in the value, use a 1 to include or 0 to exclude from the query results
    NOTE: Text from 'Mongo_Query-Operators_Notes.md' should go here adding Query Operators into the Read section of CRUD.
# ------------------------------------------------------------------------------
# U pdate (see saved video_'MongoDB_Updating Documents.mp4')
[Field Update Operators](https://docs.mongodb.com/manual/reference/operator/update-field/)
    // Update needs an Update Operator

    db.sumCollection.updateOne({sumKey01: "sumValue01"}, { $set: {sumKey02: "sumValue02"} }) // Identifies the collection AND the document and then specifiy how to update ($set: is update operator)
    db.sumCollection.updateOne({sumKey01: "sumValue01"}, { $inc: { "sumKey.sumSub-Key01": 3, "sumKey.sumSub-Key02": 25 } }) // increments two values by 3 and 25
#   Push Operator - If the 'sumKey'field does not exist, Mongo will create it as an array field.
    db.sumCollection.updateOne({ sumKey01: "sumValue01" }, {
        $push: {
            sumKey: {
                sumSub-Key01: sumSub-Value01, // 4.3 //  for example: number
                sumSub-Key02: sumSub-Value02 // ISODate("2016-01-12T09:00:00Z"), // for example: date
                sumSub-Key03: "sumSub-Value03",
                sumSub-Key04: "sumSub-Value04"
            }
        }
    })  
#   $each - When pushing onto an existing field (Question: does it create also?) using the $each modifier instructs to push on each one of these documents as an individual element of the 'sumKey' array.  If not used, the entire array here will be pushed on as a single element.
    db.sumCollection.updateOne({ sumKey01: "sumValue01" }, {
        $push: {
            sumKey: {
                $each: [{
                    sumSub-Key01: sumSub-Value01, // 4.3 //  for example: number
                    sumSub-Key02: sumSub-Value02 // ISODate("2016-01-12T09:00:00Z"), // for example: date
                    sumSub-Key03: "sumSub-Value03",
                    sumSub-Key04: "sumSub-Value04"
                    },
                    {
                    sumSub-Key05: sumSub-Value05, // 4.3 //  for example: number
                    sumSub-Key06: sumSub-Value06 // ISODate("2016-01-12T09:00:00Z"), // for example: date
                    sumSub-Key07: "sumSub-Value07",
                    sumSub-Key08: "sumSub-Value08"
                    }
                ]
            }
        }
    })

#   Slice Operator - same operation as $each above but adding slice operator to keep only 5 sumKeys.  Using a positive or negative number with slice indicates to keep the most recent or last sumKeys.
#   Position Operaptor - Instructs added values to go onto the front of the array
    db.sumCollection.updateOne({ sumKey01: "sumValue01" }, {
        $push: {
            sumKey: {
                $each: [{
                    sumSub-Key01: sumSub-Value01, // 4.3 //  for example: number
                    sumSub-Key02: sumSub-Value02 // ISODate("2016-01-12T09:00:00Z"), // for example: date
                    sumSub-Key03: "sumSub-Value03",
                    sumSub-Key04: "sumSub-Value04"
                    }],
                $position: 0,
                $slice: 5
            }
        }
    })

#   updateMany - Same formats as above work but will modify all documents matching the filter
    db.sumCollection.updateMany({ sumKey01: null }, { $unset: { sumKey01: "" } }) // removes all matching elements // Value given doesn't matter, just use empty string (Questions: Why use anything? "")

#   upserts -  Operations where if no document is found matching the filter, the document is inserted.
    db.sumCollection.updateOne({ "sumKey01.id": sumVar01.sumKey01.id }, { $set: sumVar01 }, { upsert: true }); // Prevents adding in a duplicate document with a different _id // update any document having the sumKey01.id value equal to the sumKey01.id value in the variable sumVar01 document. // 'sumVar01' is a created variable of the object that represents the document in the collection // Upsert adds the document if it does not exist

#   replaceOne
    db.movies.replaceOne({ "sumKey01": sumVar01.sumKey01.id }, sumVar01); // replace one document with a document from a created variable

# ------------------------------------------------------------------------------
# D elete

    To delete a database:
        1) use sumDatabaseName
        2) db.dropDatabase();
# --END-------------------------------------------------------------------------