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
$(".input1-21").click(function () {
    var userName = $("#registname").val();
    var Email = $("#registemail").val();
    if(Email === '' || Email === null || Email === undefined){
        swal({
            title:"请填写邮箱",
            text:"请点击确定建后添加完整信息",
            type:"warning"
            })
    }else if (!isemail(Email)) {
        swal({
            title: "邮箱格式不正确",
            text: "请点击确定建后填写正确信息",
            type: "warning"
        });
    }else {
        var data = {
            'UserName': userName,
            'Email': Email
        };
        $.post('regist', data, function (result) {
            result = JSON.parse(result);
            if (result.status == 1) {
                swal({
                title:"邮箱已被注册",
                text:"请核对后再进行，或者进行密码找回",
                type:"warning"
            });
            }else if (result.status == 3){
                swal({
                    title:"该用户名已被注册",
                    text:"请更改用户名，再进行注册",
                    type:"warning"
                     })
            }else if (result.status == 0){
                swal({
                        title:"获取信息失败",
                        text:"非常抱歉，获取信息失败",
                        type:"error",
                        timer: 2000,
                        showConfirmButton: false,
                        inputAutoTrim:true
                     })
            }else if(result.status == 2) {
                swal({
                    title: "已发送",
                    text: "验证码已发送至您的邮箱，请注意查收！",
                    type: "success"
                });
            }
        });
    }
});
function registlogin(){
    var UserName = document.getElementById("registname").value;
    var Email = document.getElementById("registemail").value;
    var Passwd = document.getElementById("registpassword").value;
    var ConfirmPassword = document.getElementById("ConfirmPassword").value;
    var incode = document.getElementById("incode").value;
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
    }else if (Passwd === '' || Passwd === null || Passwd === undefined) {
        swal({
            title:"请输入密码",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    }else if (Passwd !== ConfirmPassword) {
        swal({
            title:"两次密码不一致",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    }else if (incode === '' || incode === null || incode === undefined) {
        swal({
            title:"验证码为空",
            text:"请点击确定建后添加完整信息",
            type:"warning"
        });
    }else if (!isemail(Email)) {
         swal({
            title:"邮箱格式不正确",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    }else if  (Option.checked === false) {
         swal({
            title:"请同意用户协议",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    } else if (!isalphanumber(UserName)) {
         swal({
            title:"用户名包含非法字符",
            text:"按确定建后添加完整信息",
            type:"warning"
        });
    } else {
        var data = {
            'UserName': UserName,
            'Passwd': Passwd,
            'Email': Email,
            'incode':incode
        };

        $.post('inCode', data, function (result) {
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
            }else if (result.status == 1){
                swal({
                title:"邮箱已被注册",
                text:"请核对后再进行，或者进行密码找回",
                type:"warning"
                });
            }else if (result.status == 2){
                swal({
                    title:"该用户名已被注册",
                    text:"请更改用户名，再进行注册",
                    type:"warning"
                     })
            }else if (result.status == 3){
                swal({
                    title:"验证码错误",
                    text:"验证码输入错误，请仔细核对",
                    type:"warning"
                     })
            } else if (result.status == 4) {
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

}
//回车键实现登录
document.onkeydown=keyListener;
    function keyListener(e){
       if (e.keyCode==13){  //回车键的键值为13
           registlogin(); //调用注册按钮的注册事件
       }
    }
