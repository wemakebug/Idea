
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
                $("#rdsubapply").click(function(){
                    var content =document.getElementById("comment-content2").value;
                    if(content == ""){

                        alert("请输入申请内容！");

                    }
                    else
                    {$("#rdr-apply").slideUp("slow");}
                });


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
                    alert(content);
                    if(content == ""){
                        alert("请输入回复内容！");
                    }
                    else {
                        reply.slideUp("slow");
                    }
                 });









