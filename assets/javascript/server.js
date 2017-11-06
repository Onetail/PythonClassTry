const app = require('express')();
const http = require('http').Server(app);
const fs = require("fs")
// const path = require("path")
// app.use(bodyparser());
FILEDATA = ""
SERVEROPENCLOSE = false

imagesarray = ["title.png","background.png"] //  圖片array
mAinrunning = new function()
{
    
    for(var i = 1 ; i <=25;i++)
    {
        imagesarray.push(i+".jpg")
    }

    
}

app.get('/', function(req, res){
    fs.readFile("../../index.html",'utf8',(err,data)=>
    {
        if (err) throw err 
        FILEDATA = data

        res.setHeader('Content-Type', 'text/html');
        console.log(FILEDATA)
        console.log(__dirname + '/../../data/data.txt')
        // res.sendFile("index.html" , {root:'../../'})
        fs.readFile("../../data/data.txt",'utf-8',(err,data)=>
        {
            FILEDATA += data
            fs.readFile("../../bottomlayout.html","utf-8",(err,data)=>
            {
                FILEDATA += data 
                res.send(FILEDATA)
                res.end()
            })
        })
        
    })
    
});
app.get("/assets/css/index.css",(req,res)=>
{
    res.sendFile("index.css",{root:'../../assets/css/'})
})

for(let i = 0;i<imagesarray.length;i++)
{
    app.get("/assets/images/"+imagesarray[i],(req,res)=>
    {
        res.sendFile(imagesarray[i],{root:'../../assets/images'})
    })
}

//指定port
http.listen(process.env.PORT || 80, function(){
	console.log('listening on *:80' );
});