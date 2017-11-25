
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
                //提交部分
                var rdsubapply = document.getElementById("rdsubapply");
                rdsubapply.onclick = function () {
                    var content = document.getElementById("comment-content2").value;
                    var projectid = document.getElementById("projectId").value;
                    if(content == ""){
                        layer.open({
                        type: 1,
                        offset: '200px',
                        resize: false,
                        move: false,
                        area: ['250px', '250px'],
                        content:'请填入申请理由',
                        shade: 0.6,
                        maxmin: false,
                        anim: 0//0-6的动画形式，-1不开启
                        ,
                    });
                    }
                    else
                    {
                        $("#rdr-apply").slideUp("slow");
                        $.post('/idear/recruit_apply',{
                            "projectId":projectid,
                            "describe":content,
                        })
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
                $('.putcomment').click(function(){

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









