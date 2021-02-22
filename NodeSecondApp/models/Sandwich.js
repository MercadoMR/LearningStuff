const mongoose = require('mongoose');

/* Definición del Schema */
const SandwichSchema = new mongoose.Schema({
	nombre:String,
	pan:String,
	untable:String
});

/* Compile model(file,CollectionSchema) */
const sandwich = mongoose.model('Sandwich',SandwichSchema);
module.exports = sandwich;



