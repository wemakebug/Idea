/**
 * Created by zhanglingxue on 2017/10/16.
 */

$(document).ready(function () {
   /*项目公开程度*/
    var div = document.getElementById('openness');
    div.onclick = function () {
        if (div.innerHTML === "<p>公开</p>") {
            div.innerHTML = "<p>隐私</p>";
        } else {
            div.innerHTML = "<p>公开</p>";
        }
    };

   /*标签选择 */
    var oDiv = document.getElementsByName("chance_pro_label");
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

    $("#agreeing").click(function () {
        $(".pop-up").fadeToggle(500);
        $(".wrap").fadeToggle(500);
    });

    $("#closing").click(function () {
        $(".wrap").fadeToggle(500);
        $(".pop-up").fadeToggle(500);
    });
});


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
        document.getElementById("username2").innerHTML = username;
        return;
    }
});



