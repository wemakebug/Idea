/**
 * Created by admin on 2017/10/18.
 */


$("#backhomepage").click(function (){
    window.location.href = "homepage";
});

//页面已加载后获取信息
window.onload=function() {
    var identity = document.getElementById("identity").innerText;
    if(identity==0){
        document.getElementById("personalinput1-1").value = "学生";
    }else if(identity==1){
        document.getElementById("personalinput1-1").value = "教师";
    }else {
        document.getElementById("personalinput1-1").value = "团队";
    }
    var sex = document.getElementById("sex").innerText;
    if(sex==0){
        $("#boy").attr("checked");
    }else {
        $("#girl").attr("checked");
    }
};
//保存用户修改的信息
$(".personalinput1-8").click(function () {
    var username = document.getElementById("personalinput").value;
    var school = document.getElementById("personalinput1-2").value;
    var institude = document.getElementById("personalinput1-3").value;
    var major = document.getElementById("personalinput1-4").value;
    var sex = $('input:radio[name="personalinput1-6"]:checked').val();
    $.post('/idear/editprofile',{username:username,school:school,institude:institude,major:major,sex:sex},function (data) {
        data = JSON.parse(data);
        if(data.status==1){
            alert("修改成功");
            window.location.reload();
        }else{
            alert("系统故障");
        }
    })
    

});