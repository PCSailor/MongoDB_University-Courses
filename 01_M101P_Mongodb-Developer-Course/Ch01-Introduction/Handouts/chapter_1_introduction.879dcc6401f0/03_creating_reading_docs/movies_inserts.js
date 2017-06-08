use video;
db.movies.insertOne({ "title": "Jaws", "year": 1975, "imdb": "tt0073195" });
db.movies.insertOne({ "title": "Mad Max 2: The Road Warrior", "year": 1981, "imdb": "tt0082694" })
db.movies.insertOne({ "title": "Raiders of the Lost Ark", "year": 1981, "imdb": "tt0082971" })

// Results:
/*
>db.movies.find().pretty() {
    "_id": ObjectId("5932cf7e8fb9f9438281e0b7"),
    "title": "Jaws",
    "year": 1975,
    "imdb": "tt0073195"
}
{
    "_id": ObjectId("5932d11f8fb9f9438281e0b8"),
    "title": "Mad Max 2: The Road Warrior",
    "year": 1981,
    "imdb": "tt0082694"
}
{
    "_id": ObjectId("5932d12a8fb9f9438281e0b9"),
    "title": "Raiders of the Lost Ark",
    "year": 1981,
    "imdb": "tt0082971"
}
*/