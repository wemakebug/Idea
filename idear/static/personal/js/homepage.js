/**
 * Created by admin on 2018/1/7.
 */

$(function () {
    $.post("get_follow_count", function (data) {
        data = JSON.parse(data);
        if(data.status === 1){
            var userfollow = data.userfollow;
            $("#followid").after(userfollow);
        }else{
            alert("系统异常！");
        }
    });
    $.post("/idear/getimg", function (datas) {
        datas = JSON.parse(datas);
        if(datas.status === 1){
            var img_path = datas['img_path'];
            var message = datas['message'];
            userimgs.src = '/static' + img_path;
            document.getElementById('userimgs').style.src= userimgs.src;
        }
    });
    $.post("get_praise_count", function (data1) {
        data1 = JSON.parse(data1);
        if(data1.status === 1){
            var userpraise = data1.userpraise;
            $("#praiseid").after(userpraise);
        }else{
            alert("系统异常！");
        }
    });
    $.post("get_user_name", function (data2) {
        data2 = JSON.parse(data2);
        if(data2.status === 1){
            var username = data2['username'];
            $("#usernameid").after(username);
        }else{
            alert("系统异常！");
        }
    });
});
