//
//$(function () {
//
//$.cookie("user",3)
//
//userId = $.cookie("user")

/*cookie值转码*/
function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}


$("#rdreport").click(function(){
    var username = getCookie('username');
    if (username === null || username === '') {
        var conf = confirm("请先登录")
        if(conf==true)
        window.location.href="login"
        else
        window.location.reload()
    }
})


document.getElementById('submit-report').onclick = function(){
    var reason = $("#message-text").val()
    var creationId = $("#creationId").val()
    if(reason=="")
        alert("请填入举报理由")
    else
    $.post("crreport",{
        "reason":reason,
        "creationId":creationId
    },function(data){
        alert("提交成功")
        window.location.reload()
    })
}

$("#putcomment").click(function(){
  comment = $("#comment-content1").val() //获取评论中输入的内容
  var username = getCookie('username');
    if (username === null || username === '') {
        alert("请先登录")
        window.location.href="login"
    }
    if (comment=="")    //内容为空
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
  rcomment = $("#comment-content2").val()
  if (rcomment=="")
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

$('.rcreply').click(function(){
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
         like.children(".praise-txt").html(parseInt(like.children(".praise-txt").html())-1)
       }

 })

 })




//})
