const app = require('express')();
const http = require('http').Server(app);
const fs = require("fs")
// const path = require("path")
// app.use(bodyparser());
FILEDATA = ""
SERVEROPENCLOSE = false

IMAGESARRAY = ["title.png","background.png"] //  圖片array

mAinrunning = new function()
{
    
    for(var i = 1 ; i <=25;i++)
    {
        IMAGESARRAY.push(i+".jpg")
    }

    fs.readFile("../../index.html",'utf8',(err,data)=>
    {
        if (err) throw err 
        FILEDATA = data
        console.log(FILEDATA)
        console.log(__dirname + '/../../data/data.txt')
        // res.sendFile("index.html" , {root:'../../'})
        fs.readFile("../../data/data.txt",'utf-8',(err,data)=>
        {
            FILEDATA += data
            fs.readFile("../../bottomlayout.html","utf-8",(err,data)=>
            {
                FILEDATA += data 
            })
        })
        
    })    
}

app.get('/', (req, res)=>
{
    res.setHeader('Content-Type', 'text/html');
    res.send(FILEDATA)
    res.end()
});
app.get("/assets/css/index.css",(req,res)=>
{
    res.sendFile("index.css",{root:'../../assets/css/'})
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