db.test.find();
// --
// This reassigns the property value of q001 :
db.test.update({ _id: ObjectId("58e80637cc283671ce64bff5") }, { $set: { q001: "001" } });
// --
// Add a new object within the collection with the property keys and values specified :
db.test.insert({ q003: "003", q004: "004" });
// --
// Updates an existing object by adding property keys & values within that object :
db.test.update({ _id: ObjectId("58e80637cc283671ce64bff5") }, { $set: { q003: "003", q004: "004" } });
// --
// Updates an existing object by adding one property key with an array of values within that object :
db.test.update({ _id: ObjectId("58e80637cc283671ce64bff5") }, { $set: { q006: ["006a", "006b", "006c", "006d"] } });
// --
// Updates an existing object by adding one property value within an existing property key within that object :
db.test.update({ _id: ObjectId("58e80637cc283671ce64bff5") }, { $push: { q006: "006f" } });
// --
// removes identified object
db.test.remove({ _id: ObjectId("58e81481cc283671ce64bff7") });
// --
// Updates an existing object by removing one property value within an existing property key within that object
db.test.update({ _id: ObjectId("58e80637cc283671ce64bff5") }, { $pull: { q006: "006g" } });
// --
// Mondo Shell Command: db.resume.save
// shows this JavaScript function within Mongo
function(obj, opts) {
    if (obj == null)
        throw Error("can't save a null");

    if (typeof(obj) == "number" || typeof(obj) == "string")
        throw Error("can't save a number or string");

    if (typeof(obj._id) == "undefined") { // checks if there is an object ID associated and if there is not one, Mongo assigns one and does an insert
        obj._id = new ObjectId();
        return this.insert(obj, opts);
    } else {
        return this.update({ _id: obj._id }, obj, Object.merge({ upsert: true }, opts)); // checks if there is an object ID associated and if there is one, Mongo does an update
    }
}
// --