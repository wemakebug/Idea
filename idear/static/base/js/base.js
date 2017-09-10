/**
 * Created by root on 17-9-8.
 */
alert(window.cookie);

$(document).ready(function(){
    $(".nav li a").each(function(){
        $this = $(this);
        if($(this)[0].href==String(window.location)) {
            $(this).addClass('active');
        }
    });
});