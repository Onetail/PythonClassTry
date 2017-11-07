
function cLassimages()
{
    stringhtml = ""
    $.post("/classimage",(data)=>
    {
        for(let i = 2; i < data.length ; i++)
        {
            stringhtml += "<img class='classimage' src=/assets/images/"+data[i]+"></img>"
            stringhtml += "<br>"
        }
        $("table#maintable").html(stringhtml)
    })
}
