/**
 * Created by admin on 2018/1/9.
 */

$(function () {
    var sex = $("#sex").val();
    if(sex == 0){
        $("#boy").attr("checked",true);
    }else {
        $("#girl").attr("checked",true);
    }
});

//更新数据
$("#save_personal_information").click(function () {
    var user_id = $("#user_id").val();
    var personal_input = $("#personal_input").val();
    var user_school = $("#user_school").val();
    var user_college = $("#user_college").val();
    var user_major = $("#user_major").val();
    var sex = $('input[name="personalinput1-6"]:checked ').val();
    $.post("personal_information",{"personal_input":personal_input,"user_school":user_school,"user_college":user_college,"user_major":user_major,"sex":sex,"user_id":user_id},function (data) {
        data = JSON.parse(data);
        if(data.status == 1){
            var show = layer.open({
                title: '<p style="color: rgba(255,255,240,0.9);">个人信息修改情况</p>'
                ,content: '<p style="color: rgb(105,105,105);">个人信息修改成功</p>'
            });
        }
    });
    $(".layui-layer-btn0").click(function () {
        show.close();
        window.location.reload();
    })
});