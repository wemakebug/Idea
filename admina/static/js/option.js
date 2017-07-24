/**
 * Created by root on 17-7-24.
 */
$("i[name='removbtn']").on('click',function () {
    var current_url = window.location.pathname;
    current_url = current_url.substr(current_url.lastIndexOf("/")).replace('/','');
    var id = $(this).parents("tr").children("td").eq(0).text();
    data = {};
    id = parseInt(id);
    data["Id"] = id;
    if (confirm('确认删除id为'+id +'的数据？')){
        alert('well');
            $.post(current_url,{
                'id': id,
                'confirm': true
            },function (result) {
                result = JSON.parse(result);
                if(result['status'] === 1){
                    alert(result["message"]);
                    window.location.reload();
                }
                else if (result['status'] ===0){
                    alert(result["message"]);
                    window.location.reload();
                }
                else {
                    alert('服务器异常');
                    window.location.reload();
                }
            });
    }

});
