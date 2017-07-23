
 $(function () {
            $(".block").slice(0, 12).show();
            $(".more").on('click', function (e) {
              
              if ($(".block:hidden").length == 0) {
               $(".more").css('display', 'none');
              }
                e.preventDefault();
                $(".block:hidden").slice(0, 4).slideDown();
                if ($(".block:hidden").length == 0) {
                    $(".more").fadeOut('slow');
                }
            });
        });

$(function () {

$.cookie("user",1)
alert("ee")
// $(".follow").click(function(){
//    $.post("star",{userId:"$.cookie().get("user")",starType:"1",Id:$("this").attr("creation")},function(data){
//     if data==0
//     	alert("操作失败");
//     else
//     	alert("点赞成功")


// })


// })

})

