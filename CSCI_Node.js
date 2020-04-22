

var mysql = require('mysql');
var express = require('express');
var app = express();
app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/'));
// DB credentials might have to change in the future
var con = mysql.createConnection({
	host: '127.0.0.1',
	port: '3306',
	user: 'root',
	password: '100acef123',
	database: 'FOODIE'

});
var dataVar = [];
function getValue(value){
	dataVar = value;
}
//DB connection
con.connect(function(err){
	if (err) throw err;
	console.log('Connected!');
	var query = 'SELECT * FROM Restaurant where rand() <= .3 limit 1';
	const data = [];
	con.query(query, function(err, result, fields){
		if(err) throw err;
		getValue(result);
	});

});
// random meal selector

app.get('/', function(req,res){
	res.send(dataVar);
});
app.listen(8000);