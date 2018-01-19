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