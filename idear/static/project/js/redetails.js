
                $("#comment11-22").click(function () {
                   document.getElementById("comment-content1").focus();
                });
                //申请加入下拉
                $("#rdrbutton").click(function(){
                    $("#rdr-apply").slideDown("slow");
                });
               // 收起提交申请部分
                $("#rdclose").click(function(){
                    $("#rdr-apply").slideUp("slow");
                });
                //招募申请提交部分
                var rdsubapply = document.getElementById("rdsubapply");
                rdsubapply.onclick = function () {
                    var content  = $(".note-editable").get(0 ).innerHTML;
                    var user = getCookie('user_email');
                    if(user === null || user ===''){
                         layer.open({
                                type: 1,
                                offset: '200px',
                                resize: false,
                                move: false,
                                area: ['250px', '250px'],
                                content: '请填入申请理由',
                                shade: 0.6,
                                maxmin: false,
                                anim: 0//0-6的动画形式，-1不开启
                                ,
                            });
                    }
                    else {
                        var projectid = document.getElementById("projectId").value;
                        if (content == "<p><br></p>") {
                            layer.open({
                                type: 1,
                                offset: '200px',
                                resize: false,
                                move: false,
                                area: ['250px', '250px'],
                                content: '请填入申请理由',
                                shade: 0.6,
                                maxmin: false,
                                anim: 0//0-6的动画形式，-1不开启
                                ,
                            });
                        }
                        else {
                            $.post('/idear/recruit_apply', {
                                "projectId": projectid,
                                "describe": content,
                            }, function (data) {
                                if (data == 1) {
                                    $("#rdr-apply").slideUp("slow");
                                }
                                else {
                                    alert("wrong");
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
                $('#cputcomment').click(function(){

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
                    // alert(content);
                    if(content == ""){

                    }
                    else {
                        reply.slideUp("slow");
                    }
                 });
                //项目举报

                var preport = document.getElementById("rdpreport");
                preport.onclick = function(){
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
                    else{
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
                        , content: '<textarea placeholder="" name="" id="" class="report-text"></textarea> ' +
                        '<button class="preport" id="pputreport">提交</button> '
                         }
                        var preport = document.getElementsByClassName("report-text").value;


                };
                 //评论举报

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

                //评论回复举报
                var rcreport = document.getElementById("rdrcreport");
                rcreport.onclick = function(){
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
                        , content: '<textarea placeholder="" name="" id="comment-content1" class="report-text"></textarea> ' +
                        '<button class="putreport" id="putreport">提交</button> '
                    });
                }
                function getCookie(name) {
                    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
                    if (arr = document.cookie.match(reg))
                        return unescape(arr[2]);
                    else
                        return null;
}


