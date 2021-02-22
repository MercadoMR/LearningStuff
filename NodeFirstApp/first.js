const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const fun_servidor = function (request,response){
	response.statusCode = 200;
	response.setHeader('Content-Type','text/plain');
	response.end('Hola mundo');
};

const servidor = http.createServer(fun_servidor);

servidor.listen(port,hostname, () => {
console.log(`Servidor corriendo en http://${hostname}:${port}/`);
});