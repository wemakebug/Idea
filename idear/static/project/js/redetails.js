
       //$('.ppc-percents span').html( percent + '/' +  );
              // $('.ppc-percents span').html('1' + '/' + percent/100);
                //进度条中间显示计算 已招募人数/预计招募人数

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
               // 评论回复部分
                $(".creply").click(function(){
                    $("#commentreply").slideDown("slow");
                });

                 $('.rcreply').click(function(){
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

