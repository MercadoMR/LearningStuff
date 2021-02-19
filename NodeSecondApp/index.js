/**
 * http://usejsdoc.org/
 */

 const envi = require('dotenv')
 envi.config();
 console.log(`El puerto es ${process.env.PORT}`);
 const express = require('express');
 const app = express();

 /* Configurar motor de vistas */
 app.set('views','./vistas');
 app.set('view engine','pug');

 /* Funciones HTTP */
 app.get("/",function(req,res){
	res.render('base',{ titulo: 'Usando Pug', encabezado: 'Primera Vista!', texto: 'Mi primera vista generada' });
 });

 app.get("/sandwiches",function(req,res){
	 res.send("Todos los sandwiches");
 });


 app.listen(process.env.PORT);