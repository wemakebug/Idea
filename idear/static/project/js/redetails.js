
//申请加入下拉
$("#rdrbutton").click(function(){
    $("#rdr-apply").slideDown("slow");
});
// 收起提交申请部分
$("#rdclose").click(function(){
    $("#rdr-apply").slideUp("slow");
});
//招募申请提交部分
var rdsubapply = document.getElementById("rdsubapply");
rdsubapply.onclick = function () {
    var content  = $(".note-editable").get(0 ).innerHTML;
    var user = getCookie('user_email');
    if(user === null || user ===''){
        alert("请您登陆");
        window.location.href="/idear/login";
    }
    else {
        var projectid = document.getElementById("projectId").value;
        if (content == "<p><br></p>") {
             alert("请输入申请内容")
        }
        else {
            $.post('/idear/recruit_apply', {
                "projectId": projectid,
                "describe": content,
            }, function (data) {
                if (data == 1) {
                    $("#rdr-apply").slideUp("slow");
                }
                else {
                    alert("wrong");
                }
            });
        }
    }
};







