const mongoose = require('mongoose');
const Sandwich = require('./models/Sandwich');

mongoose.connect('mongodb://localhost/Sandwich_World', {useNewUrlParser: true, useUnifiedTopology: true});

Sandwich.create({
	nombre:"Sandwich de frijoles",
	pan:"Blanco normal",
	untable:"Frijoles",
	descripcion:"Un clásico sandwich mexicano. Pan blanco con frijoles untados."
},(error,sandwich) => {
	console.log(error,sandwich);
});