(www.bsonspec.org)
// MongoDB drivers send & receive data as BSON
// MongoDB data is stored as BSON
//  BSON extends 'JSON supported value types' by adding intergers, doubles, dates, binary data, as well as JSON supported value types: strings, numbers, booleans, arrays, objects

# This is the same thing, one in JSON, the other in BSON:
// JSON
   { "hello" : "world" }
// BSON
"\x16\x00\x00\x00\x02hello\x00 
\x06\x00\x00\x00world\x00\x00"
Look at [BSONSpec.org] for element specs


