/**
 * Created by Administrator on 2018/1/6.
 */
//删除消息记录
$(".delete").click(function () {
    var messageId= $(this).val();
    console.log(messageId);
    var show = layer.open({
        type: 1,
        offset: '200px',
        resize: false,
        move: false,
        area: ['200px', '200px'],
        title: ['确定删除此消息？', 'font-size:18px;text-align:center;'],
        shade: 0.6,
        maxmin: false,
        anim: 0,//0-6的动画形式，-1不开启,
        content: '<button class="putreport">取消</button> '+'<button class="putreport">确定</button> '
    });
    $("#deleteputreport").click(function () {
        layer.close(show);
    });
    $("#putreport").click(function () {
        layer.close(show);
        $.post("unread_messages",{"messageId":messageId},function (data) {
             data = JSON.parse(data);
             if(data.status === 0){
                 alert("删除失败！");
             } else {
                 alert("删除成功！");
                 window.location.reload();
             }
        });
    });
});


$(".close_message").click(function () {
    window.location.reload();
});


//展示未读消息详情页面
// $(".examine").click(function() {
//     var infoId = $(this).val();
//     $.post("show_messages",{"infoId":infoId},function (data) {
//         var jsonData = $.parseJSON(data);
//         var str = "";
//         str += "<div class='modal-body'>";
//         str += "时间：" + jsonData.Date + "<br><br>";
//         str += "消息等级：" + jsonData.Priority +"<br><br>";
//         str += "消息内容：" + jsonData.Content + "<br><br>";
//         $(".modal-body").empty().append(str);
//     });
//     $.post("unread_read",{"infoId":infoId},function (result) {
//         result = JSON.parse(result);
//         if(result.status === 0){
//             alert("删除失败！");
//         }
//     })
// });