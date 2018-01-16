/**
 * Created by zhanglingxue on 2018/1/9.
 */

//限制字符个数
// $(document).ready(function () {
//     $(".proContentShow p").each(function () {
//         var maxwidth = 104;
//         if ($(this).text().length > maxwidth) {
//             $(this).text($(this).text().substring(0, maxwidth));
//             $(this).html($(this).html() + '…')
//             ;
//         }
//     });
// });

//添加选择列表样式
$(function(){
        var navLi=$('.operationItem ul li a') ;//此处填写你的侧边导航html对象
        var windowUrl=String(window.location.href); //获取当前url链接
        navLi.each(function(){
            $this = $(this);
            var t = $this[0].href;
            if(t === windowUrl) {
                $(this).addClass('addsty');  //添加当前位置样式
            }
        });
    });



