/**
 * Created by admin on 2017/7/20.
 */

$(document).ready(function () {
    $("#getVerification").click(function () {
        var email = $("#e-mail").val();
        var re=/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
        if (re.test(email) !== true) {
            swal({
                title:"aaa",
                text:"请填写完整信息!",
                type:"warning"
            });
        }else {
            $.post('obtainVerify', {"email": email});
        }
    });
    $("#resetOk").click(function () {
        var email = $("#e-mail").val();
        var newPassword = $("#newPassword").val();
        var confirmPassword = $("#confirmPassword").val();
        var identifyingcode = $("#identifyingcode").val();
        if(email !== ""){
            var re=/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
            if (re.test(email) !== true) {
                swal({
                    title:"邮箱格式不正确",
                    text:"请填写完整信息!",
                    type:"warning"
                });
            } else if(newPassword === ""){
                swal({
                    title:"请输入新密码",
                    text:"请填写完整信息!",
                    type:"warning"
                });
            } else if(confirmPassword === ""){
                swal({
                    title:"请再次输入密码",
                    text:"请填写完整信息!",
                    type:"warning"
                });
            } else if(newPassword !== confirmPassword){
                swal({
                    title:"两次输入密码不一致",
                    text:"请填写完整信息!",
                    type:"warning"
                });
            } else if(identifyingcode === ""){
                swal({
                    title:"请输入验证码",
                    text:"请填写完整信息!",
                    type:"warning"
                });
            }  else{
                $.post('forgetPassword', {"email": email, "newPassword": newPassword, "identifyingcode":identifyingcode},function (data) {
                    var jsonData = $.parseJSON(data);
                    if(jsonData === -1){
                        swal({
                            title:"重置密码失败",
                            text:"请重新输入!",
                            type:"warning"
                        });
                    } else if(jsonData === 1){
                        alert("重置密码成功！")
                        window.location.href  = '/idear/login';
                        // location.replace(document.referrer);
                    }
                });
            }
        } else if(email === ""){
            swal({
                title:"邮箱不能为空",
                text:"请填写完整信息!",
                type:"warning"
            });
        }
    });
});


