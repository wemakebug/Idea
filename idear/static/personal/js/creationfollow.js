/**
 * Created by zhanglingxue on 2018/1/9.
 */
//删除关注创意
$(".deletePro").click(function () {
    var creationId = $(this).val();
    var show = layer.open({
        type: 1,
        offset: '200px',
        resize: false,
        move: false,
        area: ['300px', '100px'],
        title: ['确定取消此关注？', 'font-size:18px;text-align:center;background:#000000;color:white;'],
        shade: 0.6,
        maxmin: false,
        anim: 0,//0-6的动画形式，-1不开启,
        content: '<button class="putreport" id="deleteputreport">取消</button> ' + '<button class="putreport" id="putreport">确定</button> '
    });
    $("#deleteputreport").click(function () {
        layer.close(show);
    });
    $("#putreport").click(function () {
        layer.close(show);
        $.post("creationfollow",{"creationId":creationId},function (data) {
             data = JSON.parse(data);
             if(data.status === 0){
                 alert("删除失败！");
             } else {
                 window.location.reload();
             }
        });
    });
});