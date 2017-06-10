# Query Operators [see folders within Ch02-CRUD\Handouts for detailed notes and examples](https://docs.mongodb.com/manual/reference/operator/query/)
# Comparison Operators
    db.sumCollection.find({ sumKey: { $gt: sumValue } }).count() // find greater than sumvalue
    db.sumCollection.find({ sumKey: { $gt: sumValue01, $lt: sumValue02 } }).count() // find range between sumValue01 & sumValue02 
    db.sumCollection.find({ "sumKey.sumSubKey": { $gte: sumValue01 }, sumKey02: { $gt: sumValue02, _id: 0 } }) // find documents having a value for sumKey.sumSubKey matching sumValue01 or greater AND also having a value for sumKey02 matching values greater than sumValue02 AND not printing the object_ID number
    db.sumCollection.find({ sumKey: { $ne: "sumValue" } }).count() // 
    db.sumCollection.find({ sumKey: { $ne: "sumValue" } }, {sumKey01: 1, sumKey02: 1, _id: 0}).count() // 
    db.sumCollection.find({ sumKey: { $in: ["sumValue01", "sumValue02"] } }).pretty() // find documents that have a value for sumKey matching any one of the values within the $in array // The values of $in must be an array
# Element Operators
    db.sumCollection.find({ "sumKey.sumSubKey": { $exists: true } }) // test for field existance of sumKey.sumSubKey
    db.sumCollections.find({ "sumKey.sumSubKey": { $exists: false } }) // test for non-existance of sumKey.sumSubKey field
    db.sumCollection.find({ _id: { $type: "string" } }) // searches for all documents with an id field and a typeof string // Value of $type may be either a BSON type number or the string alias
# Logical Operators
    db.sumCollection.find({ $or: [{ "sumKey01.sumSubKey": { $gt: 99 } }, { "sumKey02": { $gt: 95 } } ]})
    db.sumCollection.find({ $and: [{ "sumKey01": { $ne: 100 } }, { "same-sumKey01" { $exists: true } } ] }) // $and allows checking for different data on the same field
# Regex Operators (see '06_regex_operators' for notes)
    db.sumCollection.find({ "sumKey01.sumSubKey": { $regex: /^sumValue\s.*/ } }, { sumKey02: 1, "sumKey01": 1, _id: 0 }).pretty()
# Array Operators
    db.sumCollection.find({ sumKey: { $all: ["sumValue01", "sumValue02", "sumValue03"] } }).pretty() // must match ALL elements listed in the array
    db.sumCollection.find({ sumKey: { $size: 1 } }).pretty() // match documents based on the length of the array
    db.sumCollection.find({ sumKey-withArrayValue: { $elemMatch: { sumArrayKey01: "sumArrayValue01", sumArrayKey02: { $gt: 15 } } } }) // $elemMatch requires that all criteria match within a single element of an array field