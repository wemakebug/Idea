/**
 * Created by admin on 2017/7/23.
 */

$(document).ready(function() {
    $("#petitionhelp").click(function () {
        //点击按钮后发送跳转到指定页面的事件。
        window.location.href = "teamhelpapplication";
    });
});


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
        }
        $("#contectnumber1").val("");
         var comment_text = document.getElementById("contectnumber1").value;
        $.post('/idear/teamdetails',{

            "string":comment_text
        }, function (data) {
            data = JSON.parse(data);
            if(data.status == 0){
                alert("Wrong");
            }
        });

});

