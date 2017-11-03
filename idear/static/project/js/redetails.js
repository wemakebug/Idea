
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


        $("#rdputcomment").click(function () {
            var c_main = document.createElement("div");
            c_main.className = "cmain";

            var cmain_cimg = document.createElement("img");
            cmain_cimg.className = "c-img";
            cmain_cimg.src = "/static/project/imgs/user.svg";

            var cmain_commentbox = document.createElement("div");
            cmain_commentbox.className = "comment-box";

            var commentbox_commenthead = document.createElement("div");
            commentbox_commenthead.className = "comment-head";

            var commenthead_cname = document.createElement("h6");
            commenthead_cname.className = "comment-name";

            var commenthead_cdate = document.createElement("span");
            commenthead_cdate.className = "cdate";

            var commenthead_coption = document.createElement("div");
            commenthead_coption.className = "c-option";

            var coption_clike = document.createElement("img");
            coption_clike.className = "clike";
            coption_clike.src = "/static/project/imgs/like1.svg";

            var coption_clikenum = document.createElement("span");
            coption_clikenum.className = "clikenum";

            var coption_creply = document.createElement("img");
            coption_creply.className = "creply";
            coption_creply.src = "/static/project/imgs/reply.svg";

            var coption_creport = document.createElement("img");
            coption_creport.className = "creport";
            coption_creport.src = "/static/creation/imgs/report.png";

            var commentbox_commentcontent = document.createElement("div");
            commentbox_commentcontent.className = "comment-content";

            var commentcontent_p = document.createElement("p");
            commentcontent_p.textContent = "ASDASDASDAWDF";

            var commentbox_commentreply = document.createElement("div");
            commentbox_commentreply.className = "commentreply";
            commentbox_commentreply.name = "commentreply";


            var commentreply_text = document.createElement("textarea");
            commentreply_text.className = "commentreply-text";

            var commentreply_putcomment = document.createElement("button");
            commentreply_putcomment.className = "putcomment";
            commentreply_putcomment.textContent = "回复";

            c_main.appendChild(cmain_cimg);
            c_main.appendChild(cmain_commentbox);

            cmain_commentbox.appendChild(commentbox_commenthead);
            cmain_commentbox.appendChild(commentbox_commentcontent);
            cmain_commentbox.appendChild(commentbox_commentreply);
            commentbox_commenthead.appendChild(commenthead_cname);
            commentbox_commenthead.appendChild(commenthead_cdate);
            commentbox_commenthead.appendChild(commenthead_coption);
            commenthead_coption.appendChild(coption_clike);
            commenthead_coption.appendChild(coption_clikenum);
            commenthead_coption.appendChild(coption_creport);
            commenthead_coption.appendChild(coption_creply);
            commentbox_commentcontent.appendChild(commentcontent_p);

            commentbox_commentreply.appendChild(commentreply_text);
            commentbox_commentreply.appendChild(commentreply_putcomment);

            var comment_input = document.getElementById("comment-content1");
            var comment_content = comment_input.value;
            commentcontent_p.innerHTML = comment_content
            var c_all = document.getElementsByName("c-all")[0];
            var cmain = document.getElementsByClassName("cmain")[0];
            c_all.insertBefore(c_main,cmain);

        });
