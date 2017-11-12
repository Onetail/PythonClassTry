
function dEtailimages()
{
    stringhtml = ""
    $.post("/classimage",(data)=>
    {
        for(let i = 6; i < data.length ; i++)
        {
            stringhtml += "<img class='classimage' src=/assets/images/"+data[i]+"></img>"
            stringhtml += "<br>"
        }
        $("table#maintable").html(stringhtml)
    })
}
function cLasssearch()
{
    $("#maintable").html("")    //..clean data
    ajaxdata = ""
    $.ajax(
        {
            url: "/data/Package",
            success: (data)=>
            {
               ajaxdata = data 
            },
            async:false
        })
        
    ajaxdata = ajaxdata.split(" ")
    for(let i in ajaxdata)
    {
        console.log(ajaxdata[i])
        let alldata = document.createElement("div")
        alldata.id = "alldata"+ajaxdata[i]
        alldata.className = "Btnstyle"
        $("#maintable").append(alldata)
        $("div#alldata"+ajaxdata[i]).text(ajaxdata[i])
        $("div#alldata"+ajaxdata[i]).css(
            {
                "color":"#aadd11",
                "background":"#112233",
                "width":"100%",
                "margin":"10px"
            })
        $("div#alldata"+ajaxdata[i]).click(()=> //..onclick Package data's filename
        {
            dArkscreen(ajaxdata[i])
        })
    }
}
function dArkscreen(detail)
{
    screendata = ""
    console.log(detail)
    var darkbackground = document.createElement("div")
    darkbackground.id = "darkbackground"+detail
    $.ajax(
        {
            url: "/data/"+detail.toString(),
            success: (data)=>
            {
                screendata = data 
            },
            async:false
        })
    console.log(screendata)
    $(darkbackground).html(screendata)
    $(darkbackground).css(
        {
            "position":"fixed",
            "z-index":"99",
            "top":"20%",
            "left":"30%",
            "width":"35vw",
            "height":"60%",
        })
    $("#maintable").append(darkbackground)
    $("div#bg").fadeIn(SPEEDTIME,()=>
    {
        $("div#bg").click(()=>
        {
            $(darkbackground).remove() 
            $("div#bg").fadeOut(SPEEDTIME)   
        })
    })
    
}