 //加载更多
 $(function () {
            $(".project_top").slice(0, 12).show();
           if($(".project_top").length <= 12) {
           $(".more").hide();
           }
            $(".more").on('click', function (e) {

              if ($(".project_top:hidden").length == 0) {
               $(".more").css('display', 'none');
              }
                e.preventDefault();
                $(".project_top:hidden").slice(0, 4).slideDown();
                if ($(".project_top:hidden").length == 0) {
                    $(".more").fadeOut('slow');
                }
            });
        })