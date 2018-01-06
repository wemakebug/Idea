
$(function(){
	$(window).scroll(function(){
		var scrollt = document.documentElement.scrollTop + document.body.scrollTop;
		if( scrollt >300 ){
			$("#gotop").fadeIn(400);
		}else{
			$("#gotop").stop().fadeOut(400);
		}
	});
	$("#gotop").click(function(){
			$("html,body").animate({scrollTop:"0px"},200);
	});
});






