//加载更多
$(function() {
    $(".border_0").slice(0, 6).show();
    if ($(".border_0").length <= 6) {
        $(".more_0").hide();
    }
    $(".more_0").on('click',function(e) {
        e.preventDefault();
        $(".border_0:hidden").slice(0, 6).slideDown();
        if ($(".border_0:hidden").length == 0) {
            $(".more_0").fadeOut('slow');
        }
    });
});
//点赞
    $(function(){
        $("body").on("click",".praise_0",function () {
            var praise_img = $(this).find("img");
            var text_box = $(this).siblings(".add-num");
            var praise_txt = $(this).siblings(".praise-txt");
            var num = parseInt(praise_txt.text());
            if(praise_img.attr("src") == "../static/team/imgs/yizan.png"){
                // $(this).html("<img src='{% static 'team/imgs/zan.png' %}'  name='praise_img' class='animation' />");
               $(this).html("<img src='../static/team/imgs/zan.png' name='praise_img' class='animation' />");
                praise_txt.removeClass("hover");
                text_box.show().html("<em class='add-animation'>-1</em>");
                $(".add-animation").removeClass("hover");
                num -=1;
                praise_txt.text(num);
            }else{
                $(this).html("<img src='../static/team/imgs/yizan.png' name='praise_img' class='animation' />");
                praise_txt.addClass("hover");
                text_box.show().html("<em class='add-animation'>+1</em>");
                $(".add-animation").addClass("hover");
                num +=1;
                praise_txt.text(num);
            }
        });
	});

//控制介绍字数
    $(document).ready(function () {
            $(".content_0").
            each(function () {
                var maxwidth = 136;
                if ($(this).text().length > maxwidth) {
                    $(this).text($(this).text().substring(0, maxwidth));
                    $(this).html($(this).html() +'…')
                    ;
                }
            });
        });
//随机显示颜色
$('.repo-language-color').each(function() {
    var col = 'rgb' + '(' + Math.ceil(Math.random() * 245) + ',' + Math.ceil(Math.random() * 245) + ',' + Math.ceil(Math.random() * 245) + ')';
    $(this).css('background', col)
});

//点击更换样式
$(".allsign").on("click",function () {
    var col = 'rgb' + '(' + Math.ceil(Math.random() * 245) + ',' + Math.ceil(Math.random() * 245) + ',' + Math.ceil(Math.random() * 245) + ')';
    $(".allsign").eq(index($(this)).css('background',col));


});