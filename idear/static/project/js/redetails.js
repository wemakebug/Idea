
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


                 $(".likebutton").click(function(){

                     Id = $(this).attr("project")
                     like = $(this)
                     $.post("star", {userId: userId, starType: "2", Id: Id}, function (data) {
                         if (data == 1)    //点赞成功
                         {
                             like.children().attr("src", "../static/project/imgs/liked.png")
                             like.children(".plikenum").html(parseInt(like.children(".plikenum").html()) + 1)
                         }
                         else if (data == 0)
                             alert(data)
                         else    //取消点赞成功
                         {
                             like.children().attr("src", "../static/project/imgs/like1.svg")
                             like.children(".plikenum").html(parseInt(like.children(".plikenum").html()) - 1)
                         }

                     });
                 });

  




