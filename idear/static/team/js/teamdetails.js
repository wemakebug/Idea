/**
 * Created by admin on 2017/7/23.
 */
//点击按钮后发送跳转到指定页面的事件。
$(document).ready(function() {
    $("#petitionhelp").click(function () {
        window.location.href = "teamhelpapplication";
    });
});
//end跳到指定页面结束

//判断评论输入框为空，不为空往后台添加记录
$("#putcommentbutton").click(function () {
    function createteamcomment() {
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
            var myDate = new Date();
            //获取当前年
            var year = myDate.getFullYear();
            //获取当前月
            var month = myDate.getMonth() + 1;
            //获取当前日
            var date = myDate.getDate();
            var h = myDate.getHours();       //获取当前小时数(0-23)
            var m = myDate.getMinutes();     //获取当前分钟数(0-59)
            if (m < 10) m = '0' + m;
            var s = myDate.getSeconds();
            if (s < 10) s = '0' + s;
            var nows = year + '-' + month + "-" + date + " " + h + ':' + m + ":" + s;

            var parentdiv = document.createElement("div");
            parentdiv.className = "cmain";

            var userimg = document.createElement("img");
            userimg.className = "c-img";
            userimg.src = "/static/project/imgs/user.svg";

            var leftdiv = document.createElement("div");
            leftdiv.className = "comment-box";

            var leftdivtop = document.createElement("div");
            leftdivtop.className = "comment-head";

            var leftdivtoph6 = document.createElement("h6");
            leftdivtoph6.className = "comment-name ";

            var leftdivtoph6a = document.createElement("a");

            var leftdivtopspan = document.createElement("span");
            leftdivtopspan.className = "cdate";
            leftdivtopspan.innerText = nows;

            var leftdivtopleftdiv = document.createElement("div");
            leftdivtopleftdiv.className = "c-option";

            var leftdivtopleftdivimg1 = document.createElement("img");
            leftdivtopleftdivimg1.className = "clike";
            leftdivtopleftdivimg1.src = "/static/project/imgs/like1.svg";

            var leftdivtopleftdivspan = document.createElement("span");
            leftdivtopleftdivspan.className = "clikenum";

            var leftdivtopleftdivimg2 = document.createElement("img");
            leftdivtopleftdivimg2.className = "creply";
            leftdivtopleftdivimg2.src = "/static/project/imgs/reply.svg";

            var leftdivtopleftdivimg3 = document.createElement("img");
            leftdivtopleftdivimg3.className = "creport";
            leftdivtopleftdivimg3.src = "/static/creation/imgs/report.png";

            var leftdivbottomdiv = document.createElement("div");
            leftdivbottomdiv.className = "comment-content";

            var leftdivbottomdivp = document.createElement("p");
            leftdivbottomdivp.innerHTML = comment_text;

            var cmain_commentreply = document.createElement("div");
            cmain_commentreply.className = "commentreply";
            cmain_commentreply.name = "commentreply";

            var commentreply_text = document.createElement("textarea");
            commentreply_text.className = "commentreply-text";

            var commentreply_putcomment = document.createElement("button");
            commentreply_putcomment.className = "putcomment";
            commentreply_putcomment.textContent = "回复"

            parentdiv.appendChild(userimg);
            parentdiv.appendChild(leftdiv);

            leftdiv.appendChild(leftdivtop);
            leftdiv.appendChild(leftdivbottomdiv);
            leftdiv.appendChild(cmain_commentreply);

            leftdivtop.appendChild(leftdivtoph6);
            leftdivtop.appendChild(leftdivtopspan);
            leftdivtop.appendChild(leftdivtopleftdiv);


            leftdivbottomdiv.appendChild(leftdivbottomdivp);

            leftdivtoph6.appendChild(leftdivtoph6a);

            leftdivtopleftdiv.appendChild(leftdivtopleftdivimg1);
            leftdivtopleftdiv.appendChild(leftdivtopleftdivspan);
            leftdivtopleftdiv.appendChild(leftdivtopleftdivimg2);
            leftdivtopleftdiv.appendChild(leftdivtopleftdivimg3);

            cmain_commentreply.appendChild(commentreply_text);
            cmain_commentreply.appendChild(commentreply_putcomment);

            var c_all = document.getElementsByName("c-all")[0];
            var c_main = document.getElementsByClassName("cmain")[0];
            c_all.insertBefore(parentdiv, c_main);

            $("#contectnumber1").val("");
        }
    }
        var comment_text = document.getElementById("contectnumber1").value;
        var teamid = window.location.href.split("/");
        teamid = teamid[teamid.length - 1];
        alert(teamid);
        $.post('/idear/teamdetails/'+teamid,{
            "string":comment_text
        }, function (data) {
            data = JSON.parse(data);
            if(data.status == 0) {
                alert("Wrong");
            }else {
                createteamcomment(data);
            }
        });
});
//end评论添加记录结束

//控制标签可以选择多个
document.onkeydown=Myfunction;
function Myfunction(){
   var oDiv = document.getElementById("teamlable1-4");
    for(var i=0;i<oDiv.length;i++){
        oDiv[i].onclick = function(){
            if(!this.style.backgroundColor ){
                this.style.backgroundColor = '#57cecd';
                this.style.color = '#ffffff';
            }else{
                this.style.backgroundColor = '';
                this.style.color = 'gray';
            }
        };
    }
};
//end标签选择多个的结束

//获得焦点跳转到评论
$("#comment11-2").click(function () {
        document.getElementById("contectnumber1").focus();
    });
//end跳转到评论结束

//评论动态效果
//     $(function(){
//         $("#praise11").on("click",function () {
//             var praise_img = $("#praise-img11");
//             var text_box = $("#add-num11");
//             var praise_txt = $("#praise-txt11");
//             var num=parseInt(praise_txt.text());
//             if(praise_img.attr("src") === ("{% static 'team/imgs/yizan.png' %}")){
//                 $(this).html("<img src='{% static 'team/imgs/点赞.png' %}' id='praise-img11' class='animation' />");
//                 praise_txt.removeClass("hover");
//                 text_box.show().html("<em class='add-animation'>-1</em>");
//                 $(".add-animation").removeClass("hover");
//                 num -=1;
//                 praise_txt.text(num)
//             }else{
//                 $(this).html("<img src='{% static 'team/imgs/yizan.png' %}' id='praise-img11' class='animation' />");
//                 praise_txt.addClass("hover");
//                 text_box.show().html("<em class='add-animation'>+1</em>");
//                 $(".add-animation").addClass("hover");
//                 num +=1;
//                 praise_txt.text(num)
//             }
//         });
// 	});
//      $(function(){
//         $("#praise11-1").on("click",function () {
//             var praise_img1 = $("#praise-img11-1");
//             var text_box1 = $("#add-num11-1");
//             var praise_txt1 = $("#praise-txt11-1");
//             var num1=parseInt(praise_txt1.text());
//                 if(praise_img1.attr("src") === ("{% static 'team/imgs/心形实心.png' %}")){
//                 $(this).html("<img src='{% static 'team/imgs/心形.png' %}' id='praise-img11-1' class='animation' />");
//                 praise_txt1.removeClass("hover");
//
//                 text_box1.show().html("<em class='add-animation'>-1</em>");
//                 $(".add-animation").removeClass("hover");
//                 num1 -=1;
//                 praise_txt1.text(num1)
//             }else{
//                 $(this).html("<img src='{% static 'team/imgs/心形实心.png' %}' id='praise-img11-1' class='animation' />");
//                 praise_txt1.addClass("hover");
//                 text_box1.show().html("<em class='add-animation'>+1</em>");
//                 $(".add-animation").addClass("hover");
//                 num1 +=1;
//                 praise_txt1.text(num1)
//             }
//         });
// 	});
 //end评论动态效果结束

//团队详情关注
$("#praise11-1").click(function () {
     // Id = $(this).attr("");
     $.post("/idear/attend",{userId:2,attendeType:"3"},function (data) {

     })
});

