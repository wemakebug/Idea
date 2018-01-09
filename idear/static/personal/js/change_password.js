/**
 * Created by admin on 2018/1/9.
 */

$("#reset_password").click(function () {
    var change_password_email = $("#change_password_email").val();
    var old_password = $("#old_password").val();
    var new_password = $("#new_password").val();
    var confirm_password = $("#confirm_password").val();
    if(old_password === "" || old_password === undefined || old_password === null ){
        alert("请输入旧密码");
    }else if(new_password === "" || new_password === undefined || new_password === null ){
        alert("请输入新密码");
    }else if(confirm_password === "" || confirm_password === undefined || confirm_password === null){
        alert("请再次输入新密码");
    }else if (new_password === confirm_password){
        alert("两次密码不一致");
    }
    $.post("change_password",{"change_password_email":change_password_email,"old_password":old_password,"new_password":new_password,"confirm_password":confirm_password},function (data) {
        data = JSON.parse(data);

    })
});