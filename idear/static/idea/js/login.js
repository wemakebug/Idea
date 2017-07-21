$(function () {
    $("input[id='account']").val("");
    $("input[id='password']").val("");

})
// 判断信息是否填写完整
function login() {
    var account=document.getElementById("account").value;
    var password=document.getElementById("password").value;
    var warn1=document.getElementById("warn1");
    var warn2=document.getElementById("warn2");
    if(account==""||account==undefined||account==null){
        if(password==""||password==undefined||password==null){
            document.getElementById("warn1").style.display="block";
            document.getElementById("warn2").style.display="block";
            alert("请填写完整的信息!");
        }else {
            document.getElementById("warn1").style.display="block";
            document.getElementById("warn2").style.display="none";
            alert("请填写完整的信息!");
        }
    }else {
        if(password==""||password==undefined||password==null){
            document.getElementById("warn1").style.display="none";
            document.getElementById("warn2").style.display="block";
            alert("请填写完整的信息!");
        }else {
            document.getElementById("warn1").style.display="none";
            document.getElementById("warn2").style.display="none";
        }
    }
}
// 判断用户邮箱或密码是否正确
$("input[class='login_input']").click(function () {
    if ($("#account").val() != "" && $("#password").val() != "") {
        account = $("input[id='account']").val()
        $.post("login", {
            "account": account,
            "password": $("input[id='password']").val()
        }, function (result) {
            if (result.status == 0) {
                alert(result.message);
                window.location.reload();
            } else if (result.status == 1) {
                $.cookie('username', result.username);
                $.cookie('uuid', result.UUID);
                $.cookie('account', account);
                alert(result.message);
                window.location.href = 'index'
            } else {
                alert('服务器异常');
                window.location.reload()
            }
        });
    }
})