$(function () {
    document.getElementsByName("name")[0].focus();
});


$(function () {
    $("input[id='email']").val("");
    $("input[id='password']").val("");
});

// 判断是否为邮箱
function isemail(str) {
    var result = str.match(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/);
    if (result == null) return false;
    return true;
}

// 判断信息是否填写完整
function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var warn1 = document.getElementById("warn1");
    var warn2 = document.getElementById("warn2");
    if (email === "" || email === undefined || email === null) {
        if (password === "" || password === undefined || password === null) {
            // document.getElementById("warn1").style.display = "block";
            // document.getElementById("warn2").style.display = "block";
            swal({
                title:"请输入邮箱",
                text:"请填写完整信息！",
                type:"warning"
            })
        } else {
            // document.getElementById("warn1").style.display = "block";
            // document.getElementById("warn2").style.display = "none";
            swal({
                title:"请输入邮箱",
                text:"请填写完整信息！",
                type:"warning"
            })
        }
    } else {
        if (password === "" || password === undefined || password === null) {
            // document.getElementById("warn1").style.display = "none";
            // document.getElementById("warn2").style.display = "block";
            swal({
                title:"请输入密码",
                text:"请填写完整信息！",
                type:"warning"
            })
        } else {
            document.getElementById("warn1").style.display = "none";
            document.getElementById("warn2").style.display = "none";
            swal({
                title:"登录成功",
                text:"恭喜你登录成功！",
                type:"success"
            })
        }
    }
}
// 判断用户邮箱或密码是否正确
$("input[class='login_input']").click(function () {
    if ($("#email").val() !== "" && $("#password").val() !== "") {
        var email = $("input[id='email']").val();
        var passwd = $.trim($("input[id='password']").val());
        if (isemail(email)) {
            $.post("login", {
                "email": email,
                "password": passwd
            }, function (result) {
                result = JSON.parse(result);
                if (result.status === 0) {
                    alert(result.message);
                    window.location.reload();
                } else if (result.status === 1) {
                    window.location.href  = '/idear/index'
                } else {
                    alert('服务器异常');
                    window.location.reload()
                }
            });
        }
        else {
             swal({
                title:"邮箱不正确",
                text:"请输入正确邮箱！",
                type:"warning"
            })
        }

    }
});
//按回车键实现页面登录
function keyLogin(){
 if (event.keyCode==13)  //回车键的键值为13
   document.getElementById("backjian").click(); //调用登录按钮的登录事件
}