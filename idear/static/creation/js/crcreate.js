$(document).ready(function (){
    var oDiv = document.getElementsByName("content_pro_label");
    for(var i=0;i<oDiv.length;i++){
        oDiv[i].onclick = function(){
            if(!this.style.backgroundColor ){
               this.style.backgroundColor = '#7194B8';
               this.style.color = '#ffffff';
            }else{
               this.style.backgroundColor = '';
               this.style.color = 'gray';
            }
        };
    }
})


$("#create_btn_draft").click(function(){
    var name = $(".input_title").val();
    var labels = ''
    var isUse = document.getElementsByName('isUse').value
    var labels_all = document.getElementsByName('content_pro_label')
    for(var i = 0;i < labels_all.length;i ++){
        if(labels_all[i].style.backgroundColor === "rgb(113, 148, 184)")
            labels+=labels_all[i].innerHTML+"*"
    }
    var describe = $(".note-editable").get(0).innerHTML;
    $.post("crcreate",{
        "name":name,
        "describe":describe,
        "labels":labels,
        "isUse":isUse
    },function(data){
        var jsonData = $.parseJSON(data);
        alert("已存入草稿箱")
    })
})


$("#create_btn_ok").click(function(){
    var name = $(".input_title").val();
    var labels = ''
    var labels_all = document.getElementsByName("content_pro_label")
    for(var i = 0;i < labels_all.length;i ++){
        if(labels_all[i].style.backgroundColor === "rgb(113, 148, 184)")
            labels+=labels_all[i].innerHTML+"*"
    }
    var describe = $(".note-editable").get(0).innerHTML;
    $.post("crcreate",{
        "name":name,
        "describe":describe,
        "labels":labels
    },function(data){
        var jsonData = $.parseJSON(data);
        alert("发布成功")
    })
})
/*cookie值转码*/
function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}

/*创建人名称*/
$(document).ready(function () {
    var username = getCookie('username');
    if (username === null || username === '') {

    } else {
        var email = $.cookie('email');
        var username = $.cookie('username');
        document.getElementById("username1").innerHTML = username;
        return;
    }
});

