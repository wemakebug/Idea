/**
 * Created by admin on 2017/7/23.
 */

/*cookie值转码*/
function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}

//预加载时判断该用户有没有关注

$(function(){
    var strcookie = document.cookie;
    var arrcookie = strcookie.split("; ");
    for ( var i = 0; i < arrcookie.length; i++) {
        var user_email = arrcookie[i].split("=");
    }
    user_email = user_email[user_email.length - 1];
    var team_mark = $("#team_mark").val();


    //随机颜色标签圆球
    $('.repo-language-color').each(function() {
        var col = 'rgb' + '(' + Math.ceil(Math.random() * 245) + ',' + Math.ceil(Math.random() * 245) + ',' + Math.ceil(Math.random() * 245) + ')';
        $(this).css('background', col);
    });
    var praise_txt1 = $("#praise-txt11-1");
    var praise_txt2 = $("#praise-txt11");


    //团队点赞异步刷新显示页面
    $.post("/idear/teamattend",{team_mark:team_mark,type:1},function (data) {
        if(data == 1){
             document.getElementById("praise-img11-dianzan").src="/static/team/imgs/dianzan.png";
        }else if(data == 2){
             document.getElementById("praise-img11-dianzan").src="/static/team/imgs/redzan.png";
             praise_txt2.addClass("hover");
        }
    });


    //团队关注异步刷新显示页面
    $.post("/idear/teamattend",{team_mark:team_mark,type:2},function (data) {
        if(data == 1){
             document.getElementById("praise-img11-guanzhu").src="/static/team/imgs/xinxing.png";
        }else if(data == 2){
             document.getElementById("praise-img11-guanzhu").src="/static/team/imgs/redxin.png";
             praise_txt1.addClass("hover");
        }
    });
});

//判断评论输入框为空，不为空往后台添加记录
$("#putcommentbutton").click(function () {
        var comment_text = document.getElementById("contectnumber1").value;
        if (comment_text == null) {
            swal({
                title: "评论为空",
                text: "按确定建后添加评论语",
                type: "warning"
            });
        } else if (comment_text == "") {
            swal({
                title: "评论为空",
                text: "按确定建后添加评论语",
                type: "warning"
            });
        } else if (comment_text == undefined) {
            swal({
                title: "评论为空",
                text: "按确定建后添加评论语",
                type: "warning"
            });
        } else {
            var teamid = window.location.pathname;
            team_id = teamid.replace(/[^0-9]/ig, "");
            $.post('/idear/teamdetails/' + team_id + "/", {
                "string": comment_text
            }, function (data) {
                data = JSON.parse(data);
                if (data.status == 0) {
                    alert("Wrong");
                } else {
                    $("#contectnumber1").val("");
                    window.location.reload();
                }
            });
        }
});

//获取评论框旁的用户头像
$(document).ready(function () {
    var user_img = document.getElementById('u-img');

    $.post('/idear/getimg', function (result) {
        result = JSON.parse(result);
        if (result['status'] === 1) {
            var img_path = result['img_path'];
            var message = result['message'];
            user_img.src = '/static' + img_path;
//            document.getElementById('user_img').style.src= user_img.src;
        } else if (result['status'] === 0) {
            var img_path = 'photos/2017/09/19/user/default.jpg';
            user_img.src = '/static/photos/' + img_path;

        }
    });
});

//end评论添加记录结束

//判断回复输入框为空，不为空往后台添加记录
$(".putcomment_reply").click(function () {
    var reply_comment = $(this).prev(".commentreply-text").val();
    if (reply_comment === "" || reply_comment === undefined || reply_comment === null) {
        swal({
            title: "评论为空",
            text: "按确定建后添加评论语",
            type: "warning"
        });
    } else {
        var teamid = window.location.pathname;
            team_id = teamid.replace(/[^0-9]/ig,"");
        var comment_id = $(this).attr("backgroundid");
        $.post('/idear/teamcomment', {
            "strings": reply_comment,
            "team_id":team_id,
            "comment_id":comment_id
        }, function (data) {
            data = JSON.parse(data);
            if (data.status === 0) {
                alert("Wrong");
            } else {
                $(".commentreply-text").val("");
                window.location.reload();
            }
        });
    }
});

//end

//回复举报
// var aLi = document.querySelectorAll('.creport');
// for (var i = 0; i < aLi.length; i++) {
//         aLi[i].addEventListener('click', function(){
//             layer.open({
//                 type: 1,
//                 offset: '200px',
//                 resize: false,
//                 move: false,
//                 area: ['500px', '400px'],
//                 title: ['请填入举报理由', 'font-size:18px;text-align:center;'],
//                 shade: 0.6,
//                 maxmin: false,
//                 anim: 0//0-6的动画形式，-1不开启
//                 , content: '<textarea placeholder="" name="" id="comment-content1" class="report-text"></textarea> ' +
//                 '<button class="putreport" id="putreport">提交</button> '
//             });
//         });
//     }

$(".submit_report").click(function () {
    var report_text = $(".report_reason").val();
    if(report_text === "" || report_text === undefined || report_text === null){
        swal({
            title: "举报理由为空",
            text: "按确定建后添加举报理由",
            type: "warning"
        });
    }else{

    }
});
//end

//回复内容框显示
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
//end

//获得焦点跳转到评论
$("#comment11-2").click(function () {
        document.getElementById("contectnumber1").focus();
    });
//end跳转到评论结束


//团队详情关注

$("#praise11-1").click(function () {
    var user = getCookie('user_email');
    var team_mark = $("#team_mark").val();
    var praise_txt1 = $("#praise-txt11-1");
    var num1=parseInt(praise_txt1.text());
    if(user ==="" || user === undefined || user === null) {
        alert("请您登陆");
        window.location.href = "/idear/login";
    } else {
        $.post("/idear/team_attend", {"team_mark": team_mark}, function (data) {
            data = JSON.parse(data);
            if (data.status === 1) {

                // $(this).html("<img src='/static/team/imgs/redxin.png' id='praise-img11-1' class='animation' />");
                document.getElementById("praise-img11-guanzhu").setAttribute("src", "/static/team/imgs/redxin.png");
                praise_txt1.addClass("hover");
                praise_txt1.addClass("hover");
                num1 += 1;
                praise_txt1.text(num1);
            } else if (data.status === 0) {
                alert("操作失败！");
                //删除记录
            } else if (data.status === 2) {

                document.getElementById("praise-img11-guanzhu").src = "/static/team/imgs/xinxing.png";
                praise_txt1.removeClass("hover");
                num1 -= 1;
                praise_txt1.text(num1);
            }
        })
    }
});

//end

//团队点赞

$("#praise11").click(function () {
    var user = getCookie('user_email');
    var team_mark = $("#team_mark").val();
    var praise_txt2 = $("#praise-txt11");
    var num2=parseInt(praise_txt2.text());
    if(user ==="" || user === undefined || user === null) {
        alert("请您登陆");
        window.location.href = "/idear/login";
    } else {
        $.post("/idear/team_star", {team_mark: team_mark}, function (data) {
            data = JSON.parse(data);
            if (data.status === 1) {
                document.getElementById("praise-img11-dianzan").setAttribute("src", "/static/team/imgs/redzan.png");
                praise_txt2.addClass("hover");
                num2 += 1;
                praise_txt2.text(num2);
            } else if (data.status === 0) {
                alert("操作失败！");
                //删除记录
            } else if (data.status === 2) {
                document.getElementById("praise-img11-dianzan").src = "/static/team/imgs/dianzan.png";
                praise_txt2.removeClass("hover");
                num2 -= 1;
                praise_txt2.text(num2);
            }
        })
    }
});
//end


