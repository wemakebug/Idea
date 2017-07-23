 $(function () {
            $(".block").slice(0, 12).show();
            $(".more").on('click', function (e) {
              
              if ($(".block:hidden").length == 0) {
               $(".more").css('display', 'none');
              }
                e.preventDefault();
                $(".block:hidden").slice(0, 4).slideDown();
                if ($(".block:hidden").length == 0) {
                    $(".more").fadeOut('slow');
                }
            });
        });