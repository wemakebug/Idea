/**
 * Created by admin on 2017/7/17.
 */
$(function () {
    document.getElementsByName("name")[0].focus();
});

$(document).ready(function () {
    $("#reset").click(function () {
        $("input[name='name']").val("");
        $("input[name='account']").val("");
        $("input[name='password']").val("");
        $("input[name='ConfirmPassword']").val("");
        $("input[name='email']").val("");
        $("input[name='opinion']").attr("checked", false);
    });

    $("#agreeing").click(function () {
        $(".pop-up").fadeToggle(500);
        $(".wrap").fadeToggle(500);
    });

    $("#closing").click(function () {
        $(".wrap").fadeToggle(500);
        $(".pop-up").fadeToggle(500);
    });

});

// 判断是否为字母和数字构成的内容
function isalphanumber(str) {
    var result = str.match(/^[a-zA-Z0-9]+$/);
    if (result == null) return false;
    return true;
}

// 判断是否为邮箱
function isemail(str) {
    var result = str.match(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/);
    if (result == null) return false;
    return true;
}

$('#submit_btn').click(function () {

    var UserName = document.getElementById("registname").value;
    var Email = document.getElementById("registemail").value;
    var Passwd = document.getElementById("registpassword").value;
    var ConfirmPassword = document.getElementById("ConfirmPassword").value;
    var Option = document.getElementById("registopinion");

    if (Option.checked === false) {
        alert('请同意用户协议');
    } else if (UserName === '' || UserName === null || UserName === undefined) {
        alert('请填写用户名');
    } else if (Email === '' || Email === null || Email === undefined) {
        alert('请填写邮箱');
    } else if (Passwd === '' || Passwd === null || Passwd === undefined) {
        alert('请填写密码');
    } else if (Passwd !== ConfirmPassword) {
        alert('两次密码不一致');
    } else if (!isemail(Email)) {
        alert('邮箱格式不正确');
    } else if (!isalphanumber(UserName)) {
        alert('用户名包含非法字符');
    } else {
        var data = {
            'UserName': UserName,
            'Passwd': Passwd,
            'Email': Email
        };
        alert('well');

        $.post('regist', data, function (result) {
            result =JSON.parse(result);
            if (result.status === 0) {
                alert(result.message);
                window.location.reload();
            } else if (result.status === 1) {
                $.cookie('email', Email);
                $.cookie('username', UserName);
                alert(result.message);
                window.location.href = 'index'
            }
            else {
                alert('服务器异常！请稍后重试');
            }
        });
    }

});
