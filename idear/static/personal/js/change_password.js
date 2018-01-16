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
    }else if (new_password != confirm_password){
        alert("两次密码不一致");
    }else {
        $.post("change_password", {
            "change_password_email": change_password_email,
            "old_password": old_password,
            "new_password": new_password
        }, function (data) {
            data = JSON.parse(data);
            if (data.status == 1) {
                var show = layer.open({
                    title: '<p style="color: rgba(255,255,240,0.9);">密码修改情况</p>'
                    , content: '<p style="color: rgb(105,105,105);">密码修改成功</p>'
                });
            }else{
                alert("输入的旧密码不正确")
            }
        });
        $(".layui-layer-btn0").click(function () {
            show.close();
            window.location.reload();
        })
    }
});