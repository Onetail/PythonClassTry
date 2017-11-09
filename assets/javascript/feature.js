
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
    var searchbar =  document.createElement("div")
    searchbar.id = "searchbar"
    // document.getElementById("centerframe").appendChild(searchbar)
    document.getElementById("searchbar").innerHTML = "<span id='searchtxt'><input type='text'></div>"
    $("table#maintable").hide(SPEEDTIME,()=>
    {
        $("div#searchbar").css("text-align","center")

    })
}