/*注册页面相关*/
var submit_btn_regist = document.getElementById("submit_btn_regist");
submit_btn_regist.onclick = function () {
    var account_regist = $("#account_regist");
    var passwd_regist = $("#passwd_reist");
    var passwd_repeat_regist = $("#passwd_repeat_regist");

    var account = account_regist.val();
    var passwd = passwd_regist.val();
    var passwd_repeat = passwd_repeat_regist.val();

    if(passwd !== passwd_repeat){
        alert("两次输入的密码不一致");
    }else if(account === "" || account === undefined || account === null){
        alert("账户不能为空");
    }else if(passwd === "" || passwd === undefined || passwd === null){
        alert("密码不能为空");
    }else {
        $.post("/user/register",{account:account,passwd:passwd},function (data) {
            alert(data.message);
        })
    }
};
