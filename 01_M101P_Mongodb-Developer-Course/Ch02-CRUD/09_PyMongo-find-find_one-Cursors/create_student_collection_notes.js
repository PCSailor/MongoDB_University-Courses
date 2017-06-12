// JavaScript code to be used in Mongo shell
use school // use school database
db.scores.drop(); // drops score collection
var types = ['exam', 'homework', 'quiz']
for (student_id = 0; student_id < 100; student_id++) {
    for (type = 0; type < 3; type++) {
        var r = { 'student_id': student_id, 'type': types[type], 'score': Math.random() * 100 };
        db.scores.insert(r); // inserts into database
    }
}
// for 100 students, puts in 1 document per student for each type.  So for each student there will be an exam, homework, and quiz with a score that has been randomized.