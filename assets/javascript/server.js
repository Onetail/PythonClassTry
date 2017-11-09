const app = require('express')();
// const https = require('https')
const http = require("http").createServer(app)
const fs = require("fs")

// const path = require("path")
// app.use(bodyparser());
FILEDATA = ""   
HTMLDATA = ""  
SERVEROPENCLOSE = false

IMAGESARRAY = ["title.png","background.png","backgrounddark.png","login.png","close.png","searchbar.png"] //  圖片array

mAinrunning = new function()    // init fs and array
{
    // var keyPath = __dirname + '/.ssl/private.key';
    // var certPath = __dirname + '/.ssl/certificate.crt';
    
    // var hskey = fs.readFileSync(keyPath);
    // var hscert = fs.readFileSync(certPath);
    
    // var options = {
    //     key: hskey,
    //     cert: hscert
    // };
    
    for(var i = 1 ; i <=25;i++)
    {
        IMAGESARRAY.push(i+".jpg")
    }

    fs.readFile("../../index.html",'utf8',(err,data)=>
    {
        if (err) throw err 
        HTMLDATA = data
        console.log(FILEDATA)
        console.log(__dirname + '/../../data/data.txt')
        // res.sendFile("index.html" , {root:'../../'})
        fs.readFile("../../data/data.txt",'utf-8',(err,data)=>
        {
            FILEDATA = data
            HTMLDATA += data
            fs.readFile("../../bottomlayout.html","utf-8",(err,data)=>
            {
                HTMLDATA += data 
            })
        })
        
    })    
}

app.get('/', (req, res)=>
{

    res.setHeader('Content-Type', 'text/html');
    res.send(HTMLDATA)
    res.end()
       
});
app.post("/pydata",(req,res)=>
{
    res.send(FILEDATA)
})
app.post("/classimage",(req,res)=>
{
    res.send(IMAGESARRAY)   
})
app.get("/assets/css/index.css",(req,res)=>
{
    res.sendFile("index.css",{root:'../../assets/css/'})
})
app.get("/assets/javascript/feature.js",(req,res)=>
{
    res.sendFile(__dirname+"/feature.js")
})


for(let i = 0;i<IMAGESARRAY.length;i++)
{
    app.get("/assets/images/"+IMAGESARRAY[i],(req,res)=>
    {
        res.sendFile(IMAGESARRAY[i],{root:'../../assets/images'})
    })
}

//指定port
// var server = https.createServer(options, App).listen(3000,function()
// {
// 	console.log("listening on 3000....");
// });
http.listen(process.env.PORT || 3000, function(){
	console.log('listening on *:3000' );
});