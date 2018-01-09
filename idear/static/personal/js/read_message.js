/**
 * Created by admin on 2018/1/8.
 */
$(".delete_read").click(function () {
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
        content: '<button class="putreport cancel">取消</button> '+'<button class="putreport determine">确定</button> '
    });
    $(".cancel").click(function () {
        layer.close(show);
    });
    $(".determine").click(function () {
        layer.close(show);
        $.post("read_message",{"messageId":messageId},function (data) {
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


$(".close_read_message").click(function () {
    window.location.reload();
});