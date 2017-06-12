db.movieDetails.find({ "awards.text": { $regex: /^Won\s.*/ } }).pretty()

db.movieDetails.find({ "awards.text": { $regex: /^Won\s.*/ } }, { title: 1, "awards": 1, _id: 0 }).pretty()
    // Allows using regular expressions to match fields with string values.
    // Must have a good understanding of regular expressions

// /^Won\s.*/ - See Below for explaination
// '/' and '/' Slashes delimit the regular expression
// '^' start at the beginning of value matching against (awards.text) and match exactly to 'Won' (case matters)
// '.' - Dot is a wildcard character indicating match any character any number of times.
// \s space character

// Basically saying give me all documents with the awards.text field where the value begins with the word 'Won'