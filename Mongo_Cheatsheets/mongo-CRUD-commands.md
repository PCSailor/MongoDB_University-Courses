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
    Cursor - Find method returns a cursor, to access documents, must iterate through the cursor
    Projection - used to limit fields returned by a query
    Tester


