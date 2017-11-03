/* 登陆用js */
var submit_btn = document.getElementById("submit_btn");
submit_btn.onclick = function () {
    var account  = $("#user_account").val();
    var passwd = $("#user_passwd").val();
    if(passwd === '' || passwd === null || passwd === undefined){
        alert("密码不能为空");
    }else if(account === '' || account === null || passwd === undefined){
        alert("账号不能为空");
    }else {
        $.post('/user/login',{
           account:account,
            passwd:passwd
        },function (data) {
            data = JSON.parse(data);
            alert(data)
        })
    }
};
