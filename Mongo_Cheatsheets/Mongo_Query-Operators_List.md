[MongoDB-Reference-Queries](https://docs.mongodb.com/manual/reference/operator/query/)
Query Selectors
# Comparison
For comparison of different BSON type values, see the specified BSON comparison order.
Name 	        Description
$eq 	        Matches values that are equal to a specified value.
$gt 	        Matches values that are greater than a specified value.
$gte 	        Matches values that are greater than or equal to a specified value.
$lt 	        Matches values that are less than a specified value.
$lte 	        Matches values that are less than or equal to a specified value.
$ne 	        Matches all values that are not equal to a specified value.
$in 	        Matches any of the values specified in an array.
$nin 	        Matches none of the values specified in an array.
# Logical
Name 	        Description
$or 	        Joins query clauses with a logical OR returns all documents that match the conditions of either clause.
$and 	        Joins query clauses with a logical AND returns all documents that match the conditions of both clauses.
$not 	        Inverts the effect of a query expression and returns documents that do not match the query expression.
$nor 	        Joins query clauses with a logical NOR returns all documents that fail to match both clauses.
# Element
Name 	        Description
$exists 	    Matches documents that have the specified field.
$type           Selects documents if a field is of the specified type.
# Evaluation
Name 	        Description
$mod 	        Performs a modulo operation on the value of a field and selects documents with a specified result.
$regex 	        Selects documents where values match a specified regular expression.
$text 	        Performs text search.
$where 	        Matches documents that satisfy a JavaScript expression.
# Geospatial
Name 	        Description
$geoWithin 	    Selects geometries within a bounding GeoJSON geometry. The 2dsphere and 2d indexes support $geoWithin.
$geoIntersects 	Selects geometries that intersect with a GeoJSON geometry. The 2dsphere index supports $geoIntersects.
$near 	        Returns geospatial objects in proximity to a point. Requires a geospatial index. The 2dsphere and 2d indexes support $near.
$nearSphere 	Returns geospatial objects in proximity to a point on a sphere. Requires a geospatial index. The 2dsphere and 2d indexes support $nearSphere.
# Array
Name 	        Description
$all 	        Matches arrays that contain all elements specified in the query.
$elemMatch 	    Selects documents if element in the array field matches all the specified $elemMatch conditions.
$size 	Selects documents if the array field is a specified size.
# Bitwise
Name 	        Description
$bitsAllSet 	Matches numeric or binary values in which a set of bit positions all have a value of 1.
$bitsAnySet 	Matches numeric or binary values in which any bit from a set of bit positions has a value of 1.
$bitsAllClear 	Matches numeric or binary values in which a set of bit positions all have a value of 0.
$bitsAnyClear 	Matches numeric or binary values in which any bit from a set of bit positions has a value of 0.
# Comments
Name 	        Description
$comment 	    Adds a comment to a query predicate.
## Projection Operators
Name 	        Description
$ 	            Projects the first element in an array that matches the query condition.
$elemMatch 	    Projects the first element in an array that matches the specified $elemMatch condition.
$meta 	        Projects the document’s score assigned during $text operation.
$slice 	        Limits the number of elements projected from an array. Supports skip and limit slices.

# Update
[Field Update Operators](https://docs.mongodb.com/manual/reference/operator/update-field/)
Field Update Operators:
Name 	        Description
$inc 	        Increments the value of the field by the specified amount.
$mul 	        Multiplies the value of the field by the specified amount.
$rename 	    Renames a field.
$setOnInsert 	Sets the value of a field if an update results in an insert of a document.
                Has no effect on update operations that modify existing documents.
$set 	        Sets the value of a field in a document.
$unset 	        Removes the specified field from a document.
$min 	        Only updates the field if the specified value is less than the existing field value.
$max 	        Only updates the field if the specified value is greater than the existing field value.
$currentDate 	Sets the value of a field to current date, either as a Date or a Timestamp.
[Array Update Operators](https://docs.mongodb.com/manual/reference/operator/update-array/)
# Array Update Operators:
Name 	    Description
$ 	        Acts as a placeholder to update the first element that matches the query condition in an update.
$addToSet 	Adds elements to an array only if they do not already exist in the set.
$pop 	    Removes the first or last item of an array.
$pullAll 	Removes all matching values from an array.
$pull 	    Removes all array elements that match a specified query.
$pushAll 	Deprecated. Adds several items to an array.
$push 	    Adds an item to an array.
# Array Update Operator Modifiers:
Name 	    Description
$each 	    Modifies the $push and $addToSet operators to append multiple items for array updates.
$slice      Modifies the $push operator to limit the size of updated arrays.
$sort 	    Modifies the $push operator to reorder documents stored in an array.
$position 	Modifies the $push operator to specify the position in the array to add elements.