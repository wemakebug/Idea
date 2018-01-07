//
// $(function () {
//
//     // chkAll全选事件
//     $("#chkAll").bind("click", function () {
//         $("[name = chkItem]:checkbox").attr("checked", this.checked);
//     });
//      $("[name = chkItem]:checkbox").bind("click", function () {
//         var $chk = $("[name = chkItem]:checkbox");
//         $("#chkAll").attr("checked", $chk.length == $chk.filter(":checked").length);
//      });
//     $("#delete").click(function () {
//         $("[name = chkItem]:checkbox").parent().parent().fadeOut("show"); //隐藏所有被选中的input元素
//     });
//     $("#moreDelete").click(function () {
//         $("[name = chkItem]:checkbox").parent().parent().fadeOut("show"); //隐藏所有被选中的input元素
//     });
//
// });
$(function () {
    $(".dele").click(function () {
         var creationId = $(this).children().val();
         var data = {'creationId':creationId}
         $.post('perCreation',data,function (result) {
             result = JSON.parse(result)
             if(result.status == 1){
                 alert("删除成功");
                 $(this).parent().parent().fadeOut("show");
                 window.location.reload();

             }else {
                 alert("删除错误")
             }

         });
    });
});