(()=>
{
    // preload
    var webimages = ["/assets/images/background.png","/assets/images/backgrounddark.png","/assets/images/close.png","/assets/images/login.png","/assets/images/searchbar.png"]
    for(let i = 0 ; i < webimages.length;i++)
    {
        webimages[i] = new Image()
        webimages[i].src = "http://localhost" + webimages[i]
    }
    
            
    
})()

$("img#loginicon").click(()=>
{
    console.log("push!")
    $("div#loginframe").fadeIn(SPEEDTIME)
    $("#bg").fadeIn(SPEEDTIME)

})
$("img#loginexit").click(()=>
{
    $("div#loginframe").fadeOut(SPEEDTIME)
    $("div#loginerror").fadeOut(SPEEDTIME)
    $("#bg").fadeOut(SPEEDTIME)

})
$("#logintracebutton").click((e)=>
{
    // console.log($("#loginaccount").val())
    if($("#loginaccount").val()=== "" || $("#loginpassword").val()=== "")
    {
        // e.preventDefault()
        $("div#loginerror").fadeOut(SPEEDTIME/2,()=>
        {
            $("div#loginerror").fadeIn(SPEEDTIME)
        })
    }else
    {
        $("#loginform").submit()
    }
})