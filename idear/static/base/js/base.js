/**
 * Created by root on 17-9-8.
 */



function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");

    if (arr = document.cookie.match(reg))

        return unescape(arr[2]);
    else
        return null;
}



$(document).ready(function () {
    $('.nav li a').each(function () {
        $this = $(this);
        if ($this[0].href == String(window.location.href)) {
            $this.addClass('active');
        }
    });

    var user_img = document.getElementById('user_img');
    var username = getCookie('username');
    if (username === null) {
        var hidden_item = document.getElementById('login_status_true');
        hidden_item.style.display = 'none';
    } else {
        var hidden_item = document.getElementById('login_status_false');
        hidden_item.style.display = 'none';
         var email = $.cookie('email');
    var username = $.cookie('username');
    var data = {
        'email': email,
        'username': username
    };
    $.post('getimg', {}, function (result) {
        result = JSON.parse(result);
        if (result['status'] === 1) {
            // alert(result['message']);
            var img_path = result['img_path'];
            var message = result['message'];
            user_img.src = 'static/photos/' + img_path;
        } else if (result['status'] === 0) {
            // var message = result['message'];
            // alert(message);
        } else {

        }

    });
    }



});