var express = require('express');
var app = express();

var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

var java = require('java');
java.classpath.push("");
var lexto = java.import('LongLexTo');

var pythonShell = require('python-shell');

var restful = require('node-restful');
var mongoose = restful.mongoose
mongoose.connect('mongodb://localhost:27017/boom_test');

app.use('/home', function(req, res){
	
	
    res.writeHead(200, {"Content-Type":"text/html"});
    res.write("It's working");
    res.end();

});

app.use('/mongo', function(req, res) {

    var resources = app.test = restful.model('test', mongoose.Schema({
        title: String,
        year: Number

    }))
    .methods(['get', 'post']);
    resources.register(app, '/test');
});

app.post('/lexto', function(req, res) {

    //{"sentence":"", "mode":"", "doll series":"", }
    var output = lexto.word_segmentationSync(req.body.sentence);	
    console.log(req.body.sentence);
    console.log(req.body.context);
    console.log(output);

    var outputs;
    options = {args: [output, req.body.context]}
    pythonShell.run('core.py', options, function(err, results) {
        if(err)
            throw new Error(err);
        console.log(results[0]);
        console.log(results[1]);

        res.writeHead(200, {"Content-Type":"application/json"});
        var json = JSON.stringify({"sentence": results[0], "context":results[1], "doll series": "prototype001"});
        console.log(results);
        res.write(json);
        res.end();

    });
});


app.listen(3000, function(err) {
    if(!err) {
        console.log("API  is running on port 3000");
    }

});

