$("#comment11-22").click(function () {
    document.getElementById("comment-content1").focus();
});

var rdputcomment  = document.getElementById("rdputcomment");
rdputcomment.onclick = function(){
                    var reply_comment = document.getElementById("comment-content1").value;
                    var projectid = document.getElementById("projectId").value;
                    var user = getCookie('user_email');
                    if(user === null || user ===''){
                          alert("请您登陆");
                        window.location.href="/idear/login";
                    }
                    else {
                        if (reply_comment === "" || reply_comment === undefined || reply_comment === null) {
                         alert("请输入评论内容！")
                    } else {
                        $.post('project_comment',
                            {
                                "content": reply_comment,
                                "projectId":projectid}, function (data) {
                             //data = JSON.parse(data);

                            if (data.status == 1) {
                                 alert("Wrong");
                            } else {
                                $(".commentreply-text").val("");
                                window.location.reload();
                            }
                        });
                    }
                }
         };

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
    reply.slideDown("slow");
 });

var putcomments  = document.getElementsByClassName("putcomments");
for (var i = 0; i < putcomments.length; i ++) {
    putcomments[i].onclick = function(){
    var ele = this;
    var parent_div = ele.parentNode.parentNode;
    var reply = parent_div.lastChild;
    if(reply.tagName === undefined){
        reply = parent_div.childNodes[parent_div.childNodes.length-2];
    }else {
        reply = parent_div.lastChild;
    }
    reply = $(reply);
    var content = reply.children("#commentreplytext").val()
    var commentedId = $(this).attr("backcommentId");
    var username = getCookie('user_email');
    var projectId = $("#projectId").val()

     if(username === null || username ===''){
          alert("请您登陆");
        window.location.href="/idear/login";
    }
    else{
        if(content == ""){
            alert("请输入评论内容")
        }
        else {
            $.post('/idear/prcomment',{
            "content":content,
            "username":username,
            "projectId":projectId,
            "commentedId":commentedId
            },function(data){
            location.reload()
          })
            reply.slideUp("slow");
        }
    }
 };
}

 $(document).ready(function () {
    var user_img = document.getElementById('u-img');

    $.post('/idear/getimg', function (result) {
        result = JSON.parse(result);
        if (result['status'] === 1) {
            var img_path = result['img_path'];

            var message = result['message'];
            user_img.src = '/static' + img_path;
        } else if (result['status'] === 0) {
            var img_path = 'photos/2017/09/19/user/default.jpg';
            user_img.src = '/static/photos/' + img_path;

        }
    });
});

var preport = document.getElementById("rdpreport");
preport.onclick = function(){

    var user = getCookie('user_email');
    if(user === null || user ===''){
          alert("请您登陆")
        window.location.href="/idear/login";
    }
    else {
            layer.open({
            type: 1,
            offset: '200px',
            resize: false,
            move: false,
            area: ['500px', '400px'],
            title: ['请填入举报理由', 'font-size:18px;text-align:center;'],
            shade: 0.6,
            maxmin: false,
            anim: 0//0-6的动画形式，-1不开启
            ,
            content: '<textarea placeholder="" name="" id="comment-content2" class="report-text"></textarea> ' +
            '<button class="putreport" id="putreport">提交</button> '
        });

             var projectId = $("#projectId").val()
             var username = getCookie('user_email');
             var putreport = document.getElementById("putreport");
             putreport.onclick = function(){
             var reason = document.getElementById("comment-content2").value;
             if(username === null || username ===''){
                 alert("请您登陆");
                 window.location.href="/idear/login";
             }
             else {
                 if (content == "") {
                     alert("请您填入举报内容！");
                 }
                 else {
                     layer.close(layer.index);
                     $.post("/idear/preport", {
                         "reason": reason,
                         "projectId": projectId
                     }, function (data) {
                         alert("提交成功")
                         window.location.reload()
                     });
                 }
             }
        };
    }
};


 // 评论举报

var creport = document.getElementById("rdcreport");
creport.onclick = function(){
    var user = getCookie('user_email');
    if(user === null || user ===''){
         layer.open({
                type: 1,
                offset: '200px',
                resize: false,
                move: false,
                area: ['250px', '250px'],
                content: '请您登录',
                shade: 0.6,
                maxmin: false,
                anim: 0//0-6的动画形式，-1不开启
                ,
            });
    }
    else {
        layer.open({
            type: 1,
            offset: '200px',
            resize: false,
            move: false,
            area: ['500px', '400px'],
            title: ['请填入举报理由', 'font-size:18px;text-align:center;'],
            shade: 0.6,
            maxmin: false,
            anim: 0//0-6的动画形式，-1不开启
            ,
            content: '<textarea placeholder="" name="" id="comment-content2" class="report-text"></textarea> ' +
            '<button class="putreport" id="putreport">提交</button> '
        });

    }

}

                // 评论回复举报
                // var rcreport = document.getElementById("rdrcreport");
                // rcreport.onclick = function(){
                //     layer.open({
                //         type: 1,
                //         offset: '200px',
                //         resize: false,
                //         move: false,
                //         area: ['500px', '400px'],
                //         title: ['请填入举报理由', 'font-size:18px;text-align:center;'],
                //         shade: 0.6,
                //         maxmin: false,
                //         anim: 0//0-6的动画形式，-1不开启
                //         , content: '<textarea placeholder="" name="" id="comment-content1" class="report-text"></textarea> ' +
                //         '<button class="putreport" id="putreport">提交</button> '
                //     });
                // }

function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}
