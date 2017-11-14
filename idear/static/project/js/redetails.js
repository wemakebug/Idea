
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
                    $("#rdr-apply").slideUp("slow");
                });
                //评论回复
                $(".putcomment").click(function () {
                    $(".commentreply").slideUp("slow");
                })

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

                //               关注部分点击图片替换#}
//
//                   $("#putcomment").click(function(){
//                       comment = $("#comment-content1").val()
//                       if (comment=="")
//                         alert("您的输入为空")
//                       else
//                       $.post("project_comment",{content:$("#comment-content1").val(),projectId:$("#projectId").val()},function(data){
//                           if (data == 1)
//                             location.reload()
//                           else
//                             alert("Sorry, 出现了一些问题")
//                     })
//
// })



