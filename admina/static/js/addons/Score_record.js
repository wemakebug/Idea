/**
 * Created by ubuntu on 9/23/17.
 */

function score_record(id, user, score, Event) {
    $.post("score_record", {
        "id": id, "user": user, "score": score, "Event": Event
    }, function (data) {
        alert(data);
        if(data != "数据异常，请刷新后重试"){
            window.location.reload(true);
        }
    });
}


$("body").on("click", "button[name='sub_btn']", function () {
    var user = $("#user").val();
    var score = $("#score").val();
    var Event = $("#Event").val();

    if(user == "0"){
        alert("请选择用户");
    }else if(score == "0"){
        alert("请选择等级");
    }else if(Event == ""){
        alert("请填写变动事件");
    }else if($(this).text() == "添加"){
        score_record("0", user, score, Event);
    }else if($(this).text() == "修改"){
        score_record($(this).val(), user, score, Event);
    }
});


