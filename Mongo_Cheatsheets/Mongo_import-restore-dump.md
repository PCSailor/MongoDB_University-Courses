 mongoimport is used to import a json or csv file that has been exported from mongodb. https://docs.mongodb.com/v3.2/reference/program/mongoimport/#synopsis

mongorestore "writes data from a binary database dump created by mongodump to a MongoDB instance." https://docs.mongodb.com/v3.2/reference/program/mongorestore/#synopsis

Try using mongorestore --db movies --collection movieDetails movieDetails.bson

Make sure to navigate into the folder that contains this file first.