 // $(function () {
 //            $(".block").slice(0, 12).show();
 //           if($(".block").length <= 12) {
 //           $(".more").hide();
 //           }
 //            $(".more").on('click', function (e) {
              
 //              if ($(".block:hidden").length == 0) {
 //               $(".more").css('display', 'none');
 //              }
 //                e.preventDefault();
 //                $(".block:hidden").slice(0, 4).slideDown();
 //                if ($(".block:hidden").length == 0) {
 //                    $(".more").fadeOut('slow');
 //                }
 //            });
 //        });


$(function () {

$.cookie("user",3)

userId = $.cookie("user")
		
$(".follow").click(function(){
   Id = $(this).attr("creation")
   $.post("attend",{userId:userId,attendType:"1",Id:Id},function(data){
    if(data == 1)
    	alert("关注成功")
    else
    	alert("操作失败")
})

})

})

