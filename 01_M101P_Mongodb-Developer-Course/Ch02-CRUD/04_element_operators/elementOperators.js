db.moviesDetails.find({ "tomato.meter": { $exists: true } }) // test for field existance of tomato.meter review data

db.moviesDetails.find({ "tomato.meter": { $exists: false } }) // test for non-existance of tomato.meter field review data

// Value of $type may be either a BSON type number or the string alias
// See https://docs.mongodb.org/manual/reference/operator/query/type
db.moviesScratch.find({ _id: { $type: "string" } }) // searches for all documents with an id field and a typeof string

// # Element
// Name 	        Description
// $exists 	    Matches documents that have the specified field.
// $type           Selects documents if a field is of the specified type.