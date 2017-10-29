          // 招募进度条
            $(function () {
                //var $ppc = $('.progress-pie-chart').val(),
                    //percent = parseInt($ppc.data('percent')),

              //  var percent = {{ recruit.RecruitedNumber }}/{{ recruit.PredictNumber }};
                    deg = 360 * percent ;
                if (percent > 50) {
                    $ppc.addClass('gt-50');
                }
                if (percent > 100){
                    deg = 360;
                }
                $('.ppc-progress-fill').css('transform', 'rotate(' + deg + 'deg)');
                  //$('.ppc-percents span').html( percent + '/' +  );
              // $('.ppc-percents span').html('1' + '/' + percent/100);
                //进度条中间显示计算 已招募人数/预计招募人数
                });
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

