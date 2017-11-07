const app = require('express')();
const http = require('http').Server(app);
const fs = require("fs")
// const path = require("path")
// app.use(bodyparser());
FILEDATA = ""   
HTMLDATA = ""  
SERVEROPENCLOSE = false

IMAGESARRAY = ["title.png","background.png"] //  圖片array

mAinrunning = new function()    // init fs and array
{
    
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
http.listen(process.env.PORT || 80, function(){
	console.log('listening on *:80' );
});