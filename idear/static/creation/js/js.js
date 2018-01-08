 //加载更多
$(function() {
    $("#block").slice(0, 9).show();
    if ($("#block").length <= 9) {
        $("#more").hide();
    }
    $("#more").on('click',function(e) {
        e.preventDefault();
        $("#block:hidden").slice(0, 6).slideDown();
        if ($("#block:hidden").length == 0) {
            $("#more").fadeOut('slow');
        }
    });

    // var content_input = document.getElementById("comment-content1");
    // content_input.value = "";
});


$(function () {
$.cookie("user",3)

userId = $.cookie("user")

// 创意关注操作
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


//创意点赞操作
$(".like").click(function(){

   Id = $(this).attr("creation")
   like = $(this)
   $.post("star",{userId:userId,starType:"1",Id:Id},function(data){
    if(data == 1)    //点赞成功
        { 
          like.children().attr("src","../static/creation/imgs/likes.png")
          like.children(".likespan").html(parseInt(like.children(".likespan").html())+1)
      }
    else if(data == 0)
        alert(data)
    else    //取消点赞成功
      { 
        like.children().attr("src","../static/creation/imgs/like1.png")
        like.children(".likespan").html(parseInt(like.children(".likespan").html())-1)
      }

})

})

})


