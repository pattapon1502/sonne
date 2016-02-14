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

var schema = mongoose.model('prototype', {sentence: String, doll_series: String, actor: String, date: { type: Date, default: Date.now }});

app.use('/home', function(req, res){
	
	
    res.writeHead(200, {"Content-Type":"text/html"});
    res.write("It's working");
    res.end();

});

app.use('/home2', function(req, res) {

    res.writeHead(200, {"Content-Type": "application/json"});
    var json2 = JSON.stringify({"text": "it's working"});
    res.write(json2);
    res.end()

});

app.get('/getdata', function(req, res) {

    schema.find({actor: "kid", sentence: "สวัสดี"}, function (err, docs) {
        res.json(docs);
    });


});

app.get('/data/:user', function(req, res) {

    schema.find({actor: "kid", doll_series: req.params.user}, function (err, docs) {
        res.json(docs);
    });


});

app.use('/mongo', function(req, res) {

    var database = new schema({sentence: req.body.sentence, doll_series: req.body.doll_series, actor: "kid"});
    database.save(function (err) {
        if(err) {
            console.log('there is error');
        }
    });
    
    res.writeHead(200, {"Content-Type": "application/json"});
    res.write(JSON.stringify({"text": "success"}));
    res.end()
});

app.post('/lexto', function(req, res) {

    var output = lexto.word_segmentationSync(req.body.sentence);
    console.log(req.body.sentence);
    console.log(output);

    
    res.writeHead(200, {"Content-Type":"application/json"});
    var json = JSON.stringify({"sentence": output});
    
    res.write(json);
    res.end();

});

app.post('/project', function(req, res) {

    //{"sentence":"", "mode":"", "doll series":"", }
    var database = new schema({sentence: req.body.sentence, doll_series: req.body.doll_series, actor: "kid"});
    database.save(function (err) {
        if(err) {
            console.log('there is error');
        }
    });

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
        var json = JSON.stringify({"sentence": results[0], "context": results[1], "doll_series": req.body.doll_series, "action": results[2], "sound": results[3]});
        console.log(results);
        res.write(json);
        res.end();

        var database2 = new schema({sentence: results[0], doll_series: req.body.doll_series, actor: "doll", action: results[2], sound: results[3]});
        database2.save(function (err) {
            if(err) {
                console.log('there is error');
            }
        });


    });
    


});


app.listen(3000, function(err) {
    if(!err) {
        console.log("API  is running on port 3000");
    }

});

