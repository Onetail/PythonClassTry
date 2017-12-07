const app = require('express')();
// const https = require('https')
const http = require("http").createServer(app)
const fs = require("fs")
const url = require("./htmlcomposing")

FILEDATA = ""   //..python string
HTMLDATA = ""  //..web string  

IMAGESARRAY = ["title.png","background.png","backgrounddark.png","login.png","close.png","searchbar.png"] //  圖片array
FILEARRAY = []   // to get 'Package' for know how many file to save

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
    gEtfiledata()
    console.log(FILEARRAY)
    hTmlurlset()
}
function gEtfiledata()
{
    FILEARRAY = []  // init
    fs.readFile("../../data/Package","utf-8",(err,data)=>
    {
        if(err) throw err 
        data = data.split(" ")
        for(var i = 0,max = data.length-1 ; i<max;i++){FILEARRAY.push(data[i])}
        fIleurlset()
    })
    url.cOmposing()
}
function hTmlurlset()
{
    //  put html , css , js file 
    app.get('/', (req, res)=>
    {
        
        gEtfiledata()
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
    //  import rwd
    app.get("/assets/css/index.css",(req,res)=>
    {
        res.sendFile("index.css",{root:'../../assets/css/'})
    })
    app.get("/assets/css/indexsmall.css",(req,res)=>
    {
        res.sendFile("indexsmall.css",{root:"../../assets/css/"})
    })
    app.get("/assets/javascript/feature.js",(req,res)=>
    {
        res.sendFile(__dirname+"/feature.js")
    })
    
    for(let i = 0,max=IMAGESARRAY.length;i<max;i++)
    {
        app.get("/assets/images/"+IMAGESARRAY[i],(req,res)=>
        {
            res.sendFile(IMAGESARRAY[i],{root:'../../assets/images'})
        })
    }
    
}
function fIleurlset()
{
    // sync
    app.get("/data/Package",(req,res)=>
    {
        fs.readFile("../../data/Package","utf-8",(err,data)=>
        {
            if(err) throw err
            FILEARRAY.length = 0
            datasplit = data.split(" ")
            for(var i = 0,max = datasplit.length-1 ; i<max;i++)
            {
                FILEARRAY.push(datasplit[i])
                console.log("[+加入陣列 ] "+ datasplit[i])
            }                
            console.log("[+] 陣列內容" + FILEARRAY)
            data = data.substring(0,data.length-1)
            //  put save data to post
            for(let i =0,max = FILEARRAY.length;i<max;i++)
            {
              // fs.readFile("../../data/"+FILEARRAY[i],"utf-8",(err,data)=>
             // {
                //     if(err) throw err
                //     app.post("/data/"+encodeURIComponent(FILEARRAY[i]),(req,res)=>
                //     {
                //         res.send(data)
                //     })
                // })
        
                // sync   
                app.get("/data/"+encodeURIComponent(FILEARRAY[i]),(reqq,ress)=>
                {
                    fs.readFile("../../data/"+FILEARRAY[i],"utf-8",(err,filedata)=>
                    {
                        ress.send(filedata)
                        console.log(filedata)
                    })
                })
            }
            res.send(data)
        })
    
    })
    

    // fs.readFile("../../data/Package","utf-8",(err,data)=>
    // {
    //     if(err) throw err 
    //     data = data.substring(0,data.length-1)
    //     app.post("/data/Package",(req,res)=>
    //     {
    //         res.send(data)
    //     })

    // })
}
//指定port
// var server = https.createServer(options, App).listen(3000,function()
// {
// 	console.log("listening on 3000....");
// });
http.listen(process.env.PORT || 3000, function(){
	console.log('listening on *:3000' );
});