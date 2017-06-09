# Mongo Crud operations
# C reating Documents
    insertOne()
    insertMany()
    upsert - Update commands
# R ead Documents_Scaler Fields, Embedded Documents-Fields containing nested documents, Arrays-Equality Matches (on entire array, on any element, a specific element, operator complex matches)
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
    Comparison Operators [see Ch02-CRUD\03_comparison_operators AND Website](https://docs.mongodb.com/manual/reference/operator/query/)
        db.sumCollection.find({ sumKey: { $gt: sumValue } }).count() // find greater than sumvalue
        db.sumCollection.find({ sumKey: { $gt: sumValue01, $lt: sumValue02 } }).count() // find range between sumValue01 & sumValue02 
        db.sumCollection.find({ "sumKey.sumSubKey": { $gte: sumValue01 }, sumKey02: { $gt: sumValue02, _id: 0 } }) // find documents having a value for sumKey.sumSubKey matching sumValue01 or greater AND also having a value for sumKey02 matching values greater than sumValue02 AND not printing the object_ID number
        db.sumCollection.find({ sumKey: { $ne: "sumValue" } }).count() // 
        db.sumCollection.find({ sumKey: { $ne: "sumValue" } }, {sumKey01: 1, sumKey02: 1, _id: 0}).count() // 
        db.sumCollection.find({ sumKey: { $in: ["sumValue01", "sumValue02"] } }).pretty() // find documents that have a value for sumKey matching any one of the values within the $in array // The values of $in must be an array


# D elete

    To delete a database:
        1) use sumDatabaseName
        2) db.dropDatabase();