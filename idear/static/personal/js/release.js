/**
 * Created by zhanglingxue on 2017/10/16.
 */
        /*富文本固定*/
    window.onload = function () {
        var oDiv = document.getElementById(""),
            H = 0,
            Y = oDiv;
        while (Y) {
            H += Y.offsetTop;
            Y = Y.offsetParent
        }
        window.onscroll = function () {
            var s = document.body.scrollTop || document.documentElement.scrollTop;
            if (s > H) {
                oDiv.style = "position:fixed;top:66px;"
            } else {
                oDiv.style = ""
            }
        }
    }

   /*项目公开程度*/
   $(document).ready(function () {
       var div = document.getElementById('openness');
       div.onclick = function () {
           if (div.innerHTML == "<p>公开</p>") {
               div.innerHTML = "<p>隐私</p>";
           } else {
               div.innerHTML = "<p>公开</p>";
           }
       }
         /*标签选择 */
       var oDiv = document.getElementsByName("chance_pro_label")
       for(var i=0;i<oDiv.length;i++){
           oDiv[i].onclick = function(){
               if(!this.style.backgroundColor ){
                   this.style.backgroundColor = '#295e6a';
                   this.style.color = '#ffffff';
               }else{
                   this.style.backgroundColor = '';
                   this.style.color = 'gray';
               }
           };
       }
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
            return
        }
    });