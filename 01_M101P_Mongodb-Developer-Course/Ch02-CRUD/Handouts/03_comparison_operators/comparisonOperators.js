db.movieDetails.find({ runtime: { $gt: 90 } }).count() // find greater than given value

db.movieDetails.find({ runtime: { $gt: 90, $lt: 120 } }).count() // find range 

db.movieDetails.find({ "tomato.meter": { $gte: 95 }, runtime: { $gt: 180 } })

db.movieDetails.find({ rated: { $ne: "UNRATED" } }).count()

db.movieDetails.find({ rated: { $in: ["G", "PG"] } }).pretty()