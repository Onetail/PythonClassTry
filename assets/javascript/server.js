const app = require('express')();
const http = require('http').Server(app);
const fs = require("fs")
// const path = require("path")
// app.use(bodyparser());
FILEDATA = ""


app.get('/', function(req, res){
    fs.readFile("../../data/data.txt",'utf8',(err,data)=>
    {
        if (err) throw err 
        FILEDATA = data
        console.log(FILEDATA)
        console.log(__dirname + '/../../data/data.txt')
        // res.sendFile("index.html" , {root:'../../'})
        fs.readFile("../../index.html",(err,data)=>
        {
            FILEDATA += data
            res.send(FILEDATA);
        })
        
    })
    
});
// app.get("/assets/css/index.css",(req,res)=>
// {
//     res.sendFile(__dirname+"/index.css")
// })


//指定port
http.listen(process.env.PORT || 80, function(){
	console.log('listening on *:80' );
});