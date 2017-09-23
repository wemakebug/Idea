/**
 * Created by ubuntu on 9/23/17.
 */

function score_rank(id, Level, Value) {
    $.post("score_rank", {
        "id": id, "Level": Level, "Value": Value
    }, function (data) {
        alert(data);
        if(data != "数据异常，请刷新后重试"){
            window.location.reload(true);
        }
    });
}


$("body").on("click", "button[name='sub_btn']", function () {
    var Level = $("#Level").val();
    var Value = $("#Value").val();

    if(Level == ""){
        alert("请填写等级！");
    }else if(Value == ""){
        alert("请填写分值！");
    }else{
        if($("button[name='sub_btn']").text() == "添加"){
            score_rank("0", Level, Value);
        }else if($("button[name='sub_btn']").text() == "修改"){
            score_rank(this.id, Level, Value);
        }
    }
});


$("body").on("click", ".icon-remove", function () {
    if(confirm("是否删除？")){
        $.get("score_rank", {"id": this.id}, function (data) {
            alert(data);
            if(data != "数据异常，请刷新后重试"){
                window.location.reload(true);
            }
        });
    }
});


// 修改
$("body").on("click", ".icon-edit", function () {
    $("button[name='sub_btn']").text("修改");
    var curr
});


// 添加按钮
$("body").on("click", "button[name='add']", function () {
    
});