/**
 * Created by Administrator on 2018/1/6.
 */
function delete_message() {
    var messageid= document.getElementsByClassName("messageid").innerHTML;
    $.post("unread_messages",{"messageid":messageid},function (data) {
         data = JSON.parse(data);
         if(data.status === 0){
             swal({
                title: "删除失败",
                type: "warning"
            });
         } else {
             swal({
                title: "删除失败",
                type: "success"
            });
         }
    })
}