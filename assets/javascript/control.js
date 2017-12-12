function pOinterbackgroundmenutype(element,menu){}
pOinterbackgroundmenutype.prototype.bAckpointer = (element,menu)=>
{
    $("#centerframe").click(()=>
    {
      MENUTYPE = 0 
      $(element).css("opacity","0.5")
      $(menu).hide(SPEEDTIME)  
    })
}
pOinterbackgroundmenutype.prototype.hIde = (element,menu)=>
{
    MENUTYPE = 0
    $(element).css("opacity","0.5")
    $(menu).hide(SPEEDTIME)
}
pOinterbackgroundmenutype.prototype.sHow = (element,menu,number)=>
{
    $(menu).show(SPEEDTIME)
    $(element).css("opacity","1")   
    MENUTYPE = number
}
pOinterbackgroundmenutype.prototype.iNit = ()=>
{
    $("div.menudata").hide(SPEEDTIME)
    $("div.menuclass").hide(SPEEDTIME)
    $("div.menuthree").hide(SPEEDTIME)
    $('div#detailbtn').css("opacity","0.5")
    $('div#classbtn').css("opacity","0.5")
    $('div#anybtn').css("opacity","0.5")
}