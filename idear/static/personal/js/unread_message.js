/**
 * Created by Administrator on 2018/1/6.
 */
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
        content: '<button class="putreport" id="deleteputreport">取消</button> '+'<button class="putreport" id="putreport">确定</button> '
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
             }
        });
    });
})