db.movieDetails.find({ genres: { $all: ["Comedy", "Crime", "Drama"] } }).pretty() // must match ALL elements listed in the array

db.movieDetails.find({ countries: { $size: 1 } }).pretty() // match documents based on the length of the array

// $elemMatch Explained
boxOffice: [{ "country": "USA", "revenue": 41.3 },
    { "country": "Australia", "revenue": 2.9 },
    { "country": "UK", "revenue": 10.1 },
    { "country": "Germany", "revenue": 4.3 },
    { "country": "France", "revenue": 3.5 }
]

// Say for example you wanted to find all documents where the revenue for the UK was greater than 15 million.  The above 'boxOffice document with it's associated array would NOT match this search.
db.movieDetails.find({ boxOffice: { country: "UK", revenue: { $gt: 15 } } }) // This query would not work because Mongo is looking for a 'boxOffice' value that satisfies these two selectors.  So even though this document is not what we are looking for, Mongo would return this document because within this array it finds "UK" and 41.3 (which is greater than 15)

db.movieDetails.find({ boxOffice: { $elemMatch: { country: "UK", revenue: { $gt: 15 } } } }) // $elemMatch requires that all criteria match within a single element of an array field







/*
# Array
Name 	        Description
$all 	        Matches arrays that contain all elements specified in the query.
$elemMatch 	    Selects documents if element in the array field matches all the specified $elemMatch conditions.
$size 	Selects documents if the array field is a specified size.
*/