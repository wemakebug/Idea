/**
 * Created by admin on 2018/1/9.
 */
$(".submit_change").click(function () {
    var telphone = $(".new_telphone").val();
    var user_mark = $(".user_mark").val()
    if(telphone === "" || telphone === undefined || telphone === null){
        alert("新手机号不能为空")
    }else {
        $.post("account_information",{"telphone":telphone,"user_mark":user_mark},function (data) {
            data = JSON.parse(data);
            if(data.status ===1){
                alert("成功");
                window.location.reload();
            }
        })
    }
});
