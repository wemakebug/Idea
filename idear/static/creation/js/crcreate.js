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
    var coverMap = $(".file-preview-image").attr("src"); //封面图
    var labels = ''
    var labels_all = document.getElementsByName('content_pro_label')
    for(var i = 0;i < labels_all.length;i ++){
        if(labels_all[i].style.backgroundColor === "rgb(113, 148, 184)")
            labels+=labels_all[i].innerHTML+"*"
    }
    var describe = $(".note-editable").get(0).innerHTML;
    var isUse = $('#create_btn_draft').val()
    $.post("crcreate",{
        "name":name,
        "coverMap": coverMap,
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
    if(name == ""){
        alert("请添加创意标题")
        return
    }
    var coverMap = $(".file-preview-image").attr("src"); //封面图
    if(!coverMap){
        alert("请添加封面图")
        return
    }
    var labels = ''
    var labels_all = document.getElementsByName("content_pro_label")
    for(var i = 0;i < labels_all.length;i ++){
        if(labels_all[i].style.backgroundColor === "rgb(113, 148, 184)")
            labels+=labels_all[i].innerHTML+"*"
    }
    var describe = $(".note-editable").get(0).innerHTML;

    if(labels == ""){
        alert("请添加创意标签")
        return
    }
    var isUse = $('#create_btn_ok').val()
    $.post("crcreate",{
        "name":name,
        "coverMap": coverMap,
        "describe":describe,
        "labels":labels,
        "isUse":isUse
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

