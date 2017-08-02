/**
 * Created by root ChrisProsise 17-7-24.
 */

$(document).ready(function () {
    var tds = $("td[name='Identity_td']");
    $.each(tds,function () {
        var real_Identity = $(this).parents("tr").children("td").eq(5).text();
        real_Identity = parseInt(real_Identity);
        if (real_Identity === 0){
            $(this).parents("tr").children("td").eq(4).text('学生');
        }else if(real_Identity === 1){
            $(this).parents("tr").children("td").eq(4).text('教师');
        }else if(real_Identity === 2){
            $(this).parents("tr").children("td").eq(4).text('团队');
        }
    });

});


//删除项
$("i[name='removbtn']").on('click',function () {
    alert("ok");
    var current_url = window.location.pathname;
    current_url = current_url.substr(current_url.lastIndexOf("/")).replace('/','');
    var id = $(this).parents("tr").children("td").eq(0).text();
    data = {};
    id = parseInt(id);
    data["Id"] = id;
    if (confirm('确认删除id为'+id +'的数据？')){
            $.post(current_url,{
                'delete':true,
                'edit':false,
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

//修改项
$("i[name='editbtn']").on('click',function () {
    var current_url = window.location.pathname;
    current_url = current_url.substr(current_url.lastIndexOf("/")).replace('/','');
    var td_vals =  $(this).parents("tr").children("td");
    var record_name = td_vals.eq(1).text();
    var record_id = parseInt(td_vals.eq(0).text());
    $("#h4_title").remove();
    $("#message_content").prepend("<h4 id='h4_title'>修改姓名为"+ record_name +"的数据<h4>");
    $("#show1").val(td_vals.eq(1).text());
    $("#show2").val(td_vals.eq(2).text());
    $("#show3").val(td_vals.eq(3).text());
    var radio_id ="#Identity_radio" + parseInt(td_vals.eq(5).text());
    // $("input[name='identity']").removeAttr("checked");
    $("#Identity_radio0").prop("checked","checked");
    $("button[name='sub_btn']").on('click',function () {
    })
});
