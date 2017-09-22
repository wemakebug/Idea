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


    if (UserName === '' || UserName === null || UserName === undefined) {
        swal({
            title:"请输入用户名",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    } else if (Email === '' || Email === null || Email === undefined) {
        swal({
            title:"请输入邮箱",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    } else if (Passwd === '' || Passwd === null || Passwd === undefined) {
        swal({
            title:"请输入密码",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    } else if (Passwd !== ConfirmPassword) {
        swal({
            title:"两次密码不一致",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    } else if  (Option.checked === false) {
         swal({
            title:"请同意用户协议",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    } else if (!isemail(Email)) {
         swal({
            title:"邮箱格式不正确",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    } else if (!isalphanumber(UserName)) {
         swal({
            title:"用户包含非法字符",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    } else {
        var data = {
            'UserName': UserName,
            'Passwd': Passwd,
            'Email': Email
        };

        $.post('regist', data, function (result) {
            result =JSON.parse(result);
            if (result.status == 0) {
                swal({
                    title:"获取信息失败",
                    text:"非常抱歉，获取信息失败",
                    type:"error",
                    timer: 2000,
                    showConfirmButton: false,
                    inputAutoTrim:true
                 })
                // window.location.reload();
            } else if (result.status == 1) {
                $.cookie('email', result['email']);
                $.cookie('username', result['username']);
                swal({
                    title:"注册成功，正在调转!",
                    text:"恭喜你，注册成功！",
                    type:"success",
                    timer: 3500,
                    showConfirmButton: false
                 });
                window.location.href = 'index'
            }
            else {
                 swal({
                    title:"服务器异常！请稍后重试",
                    type:"warning"
                 });
            }
        });
    }

});
