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
            document.getElementById("warn1").style.display = "block";
            document.getElementById("warn2").style.display = "block";
            alert("请填写完整的信息!");
        } else {
            document.getElementById("warn1").style.display = "block";
            document.getElementById("warn2").style.display = "none";
            alert("请填写完整的信息!");
        }
    } else {
        if (password === "" || password === undefined || password === null) {
            document.getElementById("warn1").style.display = "none";
            document.getElementById("warn2").style.display = "block";
            alert("请填写完整的信息!");
        } else {
            document.getElementById("warn1").style.display = "none";
            document.getElementById("warn2").style.display = "none";
        }
    }
}
// 判断用户邮箱或密码是否正确
$("input[class='login_input']").click(function () {
    if ($("#email").val() !== "" && $("#password").val() !== "") {
        var email = $("input[id='email']").val();
        var passwd = $("input[id='password']").val();
        if (isemail(email)) {
            $.post("login", {
                "email": email,
                "password": passwd
            }, function (result) {
                result = JSON.parse(result);
                if (result["status"] === 0) {
                    alert(result["message"]);
                    window.location.reload();
                } else if (result["status"] === 1) {
                   var username =  $.cookie('username', result["username"]);
                    var email = $.cookie('email', result['email']);

                    window.location.href =  '/idear/index'
                } else {
                    alert('服务器异常');
                    window.location.reload()
                }
            });
        }
        else {
            alert('请输入正确的邮箱')
        }

    }
});
