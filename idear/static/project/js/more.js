 //加载更多
$(function() {
    $(".project_top").slice(0,1000).show();
    if ($(".project_top").length <= 1000) {
        $(".project_more").hide();
    }
    $(".project_more").on('click',function(e) {
        e.preventDefault();
        $(".project_top:hidden").slice(0, 2).slideDown();
        if ($(".project_top:hidden").length == 0) {
            $(".project_more").fadeOut('slow');
        }


        if ($(".project_top:hidden").length == 0) {
            $(".project_more").fadeOut('slow');
        }
    });
});

$(function () {

$.cookie("user",3)

userId = $.cookie("user")

$(".follow").click(function(){

   Id = $(this).attr("creation")
   follow = $(this)
   $.post("attend",{userId:userId,attendType:"1",Id:Id},function(data){
    if(data == 1)
        {
          follow.children().attr("src","../static/creation/imgs/collections.png")
          follow.children(".followspan").html(parseInt(follow.children(".followspan").html())+1)
      }
    else if(data == 0)
        alert("操作失败")
    else
      {
        follow.children().attr("src","../static/creation/imgs/collection1.png")
        follow.children(".followspan").html(parseInt(follow.children(".followspan").html())-1)
      }

})

})


$(".like").click(function(){
   Id = $(this).attr("creation")
   $.post("star",{userId:userId,starType:"1",Id:Id},function(data){
    if(data == 1)
    	alert("感谢您的点赞")
    else if(data == 0)
    	alert("操作失败")
    else
      alert("取消点赞")
    location.reload()
})

})

})


$(function(){
		$("#praise").click(function(){
			var praise_img = $("#praise-img");
			var praise_txt = $("#praise-txt");
			var num=parseInt(praise_txt.text());
			if(praise_img.attr("src") == ("../static/creation/imgs/likes.png")){
				$(this).html("<img src='../static/creation/imgs/like1.png' id='praise-img' class='animation' />");
				praise_txt.removeClass("hover");
				num -=1;
				praise_txt.text(num)
			}else{
				$(this).html("<img src='../static/creation/imgs/likes.png' id='praise-img' class='animation' />");
				praise_txt.addClass("hover");
				num +=1;
				praise_txt.text(num)
			}
		});
	})
