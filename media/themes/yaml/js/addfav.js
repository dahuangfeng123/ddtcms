function addfav()
{
 if (document.all)
 {
window.external.addFavorite(window.location.href,'软件频道_快车网_中国领先的资源下载门户');
 }

else if (window.sidebar)
 {
 window.sidebar.addPanel('软件频道_快车网_中国领先的资源下载门户', 
window.location.href, "");
}
}
function scrollDoor(){
}
scrollDoor.prototype = {
	sd : function(menus,divs,openClass,closeClass){
		var _this = this;
		if(menus.length != divs.length)
		{
			alert("数据不正常!");
			return false;
		}				
		for(var i = 0 ; i < menus.length ; i++)
		{	
			_this.$(menus[i]).value = i;				
			_this.$(menus[i]).onmouseover = function(){
					
				for(var j = 0 ; j < menus.length ; j++)
				{						
					_this.$(menus[j]).className = closeClass;
					_this.$(divs[j]).style.display = "none";
				}
				_this.$(menus[this.value]).className = openClass;	
				_this.$(divs[this.value]).style.display = "block";	
				
				
							
			}
		}
		},
	$ : function(oid){
		if(typeof(oid) == "string")
		return document.getElementById(oid);
		return oid;
	}
}
window.onload = function(){
	var SDmodel = new scrollDoor();
        SDmodel.sd(["tjt01","tjt02","tjt03","tjt04","tjt05","tjt06","tjt07","tjt08"],["tjl01","tjl02","tjl03","tjl04","tjl05","tjl06","tjl07","tjl08"],"sd01 active","sd02");
		SDmodel.sd(["rjt01","rjt02","rjt03","rjt04","rjt05"],["rjb01","rjb02","rjb03","rjb04","rjb05"],"sd01 active","sd02");
        SDmodel.sd(["gamet01","gamet02","gamet03"],["gamel01","gamel02","gamel03"],"sd01 active","sd02");
        

}