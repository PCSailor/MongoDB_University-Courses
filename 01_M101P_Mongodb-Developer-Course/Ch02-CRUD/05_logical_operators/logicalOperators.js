db.movieDetails.find({
    $or: [{ "tomato.meter": { $gt: 99 } },
        { "metacritic": { $gt: 95 } }
    ]
})


db.movieDetails.find({
        $and: [{ "metacritic": { $ne: 100 } },
            { "metacritic" { $exists: true } }
        ]
    }) // $and allows checking for different data on the same field


/*
# Logical
Name 	        Description
$or 	        Joins query clauses with a logical OR returns all documents that match the conditions of either clause.
$and 	        Joins query clauses with a logical AND returns all documents that match the conditions of both clauses.
$not 	        Inverts the effect of a query expression and returns documents that do not match the query expression.
$nor 	        Joins query clauses with a logical NOR returns all documents that fail to match both clauses.
*/