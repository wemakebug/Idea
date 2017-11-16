
$(function () {

$.cookie("user",3)

userId = $.cookie("user")



$("#putcomment").click(function(){
  comment = $("#comment-content1").val()
  if (comment=="")
    alert("您的输入为空")
  else
  $.post("comment",{content:$("#comment-content1").val(),creationId:$("#creationId").val()},function(data){
      if (data == 1)
        location.reload()
      else 
        alert("Sorry, 出现了一些问题")
})

})


    $("#putcomments").click(function(){
    comment = $("#comment-content2").val()
    if (comment=="")
        alert("您的输入为空")
    else
    $.post("comment",{content:$("#comment-content2").val(),creationId:$("#creationId").val()},function(data){
        if (data == 1)
            location.reload()
        else
            alert("Sorry, 出现了一些问题")
    })

})

$('.creply').click(function(){
    var ele = this;
    var parent_div = ele.parentNode.parentNode.parentNode;
    var reply = parent_div.lastChild;
    if(reply.tagName === undefined){
        reply = parent_div.childNodes[parent_div.childNodes.length-2];
    }else {
        reply = parent_div.lastChild;
    }
    reply = $(reply);
    reply.slideToggle("slow");
 });



//创意关注操作
$(".home-b-collection").click(function(){
    Id = $(this).attr("creation")
    follow = $(this)
    $.post("/idear/attend",{userId:userId,attendType:"1",Id:Id},function(data){
     if(data == 1)
         {
           follow.children().attr("src","../static/creation/imgs/collections.png")
           follow.children(".followspan").html(parseInt(follow.children(".followspan").html())+1)
       }
     else if(data == 0)
         alert(data)
     else
       {
         follow.children().attr("src","../static/creation/imgs/collection0.png")
         follow.children(".followspan").html(parseInt(follow.children(".followspan").html())-1)
       }
    })

})

//创意点赞操作
 $(".praise").click(function(){

    Id = $(this).attr("creation")
    like = $(this)
    $.post("/idear/star",{userId:userId,starType:"1",Id:Id},function(data){
     if(data == 1)    //点赞成功
         {
           like.children().attr("src","../static/creation/imgs/likes.png")
           like.children(".praise-txt").html(parseInt(like.children(".praise-txt").html())+1)
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
