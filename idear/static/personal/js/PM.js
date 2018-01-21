//添加选择列表样式
$(function(){
        var navLi=$('.pm_border1 ul li a ') ;//此处填写你的侧边导航html对象
        var windowUrl=String(window.location.href);//获取当前url链接
        navLi.each(function(){
            $this = $(this);
            var t = $this[0].href;
            if(t === windowUrl) {
                $(this).addClass('addsty');
                $(this).prev().addClass('addsty')//添加当前位置样式
            }
        });
});
//删除项目
$(function () {
    var num;
    $("#pm_delete").click(function () {
        var projectId = $("#projectId").val();
        var data = {'projectId': projectId};
        num = $(this).index();
        $(".pop").fadeIn('fast');
        $(".popBottom").on('click', 'span', function (event) {
            event.preventDefault();
            if ($(this).hasClass('confirm')) {
                $.post('PM', data, function (result) {
                    result = JSON.parse(result);
                    if (result.status == 1) {
                        window.location.reload();
                    } else {
                        alert("删除错误")
                    }
                });
            } else {
                $(".pop").fadeOut();
                num = "";
            }
        });
    });
});
//草稿发布
$(function () {
    var num;
    $("#issue").click(function () {
        var projectId = $("#projectId").val();
        var data = {'projectId': projectId};
        num = $(this).index();
        $(".pop").fadeIn('fast');
        $(".popBottom").on('click', 'span', function (event) {
            event.preventDefault();
            if ($(this).hasClass('confirm')) {
                $.post('PM_draft', data, function (result) {
                    result = JSON.parse(result);
                    if (result.status == 1) {
                        window.location.reload();
                    } else {
                        alert("删除错误")
                    }
                });
            } else {
                $(".pop").fadeOut();
                num = "";
            }
        });
    });
});
// //退出项目
// $(function () {
//     var num;
//     $("#exit").click(function () {
//         var projectId = $("#projectId").val();
//         var data = {'projectId': projectId};
//         num = $(this).index();
//         $(".pop").fadeIn('fast');
//         $(".popBottom").on('click', 'span', function (event) {
//             event.preventDefault();
//             if ($(this).hasClass('confirm')) {
//                 $.post('PM_join', data, function (result) {
//                     result = JSON.parse(result);
//                     if (result.status == 1) {
//                         window.location.reload();
//                     } else {
//                         alert("删除错误")
//                     }
//                 });
//             } else {
//                 $(".pop").fadeOut();
//                 num = "";
//             }
//         });
//     });
// });

