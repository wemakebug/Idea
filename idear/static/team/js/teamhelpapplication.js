/**
 * Created by admin on 2017/7/23.
 */

$("body").on("click","#allpy",function () {
    user_email = $.cookie("user_email");
    var sHTML = $(".note-editable").get(0).innerHTML;
    var vals = $("#vals").val();
    if(user_email == null ){
        alert("请先登录")
    }
    else{
        var data ={
            'user_email':user_email,
            'sHTML':sHTML
        };
        $.post('/idear/teamhelpapplication/'+vals,data,function (result) {
            result =JSON.parse(result);
            if(result.status == 0){
                alert("获取信息失败")
            }else if(result.status == 1){
                alert('成功')
            }
        });
    }
});
