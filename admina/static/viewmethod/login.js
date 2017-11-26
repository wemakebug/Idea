/* 登陆用js */
var submit_btn = document.getElementById("submit_btn");
$("#user_account").val(localStorage.getItem("admin_account"));
$("#user_passwd").val(localStorage.getItem("admin_passwd"));

submit_btn.onclick = function () {
    var account  = $("#user_account").val();
    var passwd = $("#user_passwd").val();
    if(passwd === '' || passwd === null || passwd === undefined){
        alert("密码不能为空");
    }else if(account === '' || account === null || passwd === undefined){
        alert("账号不能为空");
    }else {
        $.post('/admina/login',{
           account:account,
            passwd:passwd
        },function (data) {
            data = JSON.parse(data);
            if(data["status"] === 1){
                if($("#remember_me_check").attr("checked")==="checked"){
                    localStorage.setItem("admin_account",account);
                   localStorage.setItem("admin_passwd",passwd);
                };
                window.location.href = "/admina/";
            }else if(data["status"] === 0){
                alert(data["message"]);
                window.location.href = "/admina/login";
            }
        })
    }
};

document.onkeydown=function(event){
        var e = event ? event :(window.event ? window.event : null);
        if(e.keyCode===13){
            //执行的方法
            submit_btn.onclick();
        }
};