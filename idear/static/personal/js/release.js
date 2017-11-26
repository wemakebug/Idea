/**
 * Created by zhanglingxue on 2017/10/16.
 */
        /*富文本固定*/
    // window.onload = function () {
    //     var oDiv = document.getElementById(""),
    //         H = 0,
    //         Y = oDiv;
    //     while (Y) {
    //         H += Y.offsetTop;
    //         Y = Y.offsetParent
    //     }
    //     window.onscroll = function () {
    //         var s = document.body.scrollTop || document.documentElement.scrollTop;
    //         if (s > H) {
    //             oDiv.style = "position:fixed;top:66px;"
    //         } else {
    //             oDiv.style = ""
    //         }
    //     }
    // };


   $(document).ready(function () {
       /*项目公开程度*/
       var div = document.getElementById('openness');
       div.onclick = function () {
           if (div.innerHTML == "<p>公开</p>") {
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
                   this.style.backgroundColor = '#295e6a';
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
            return
        }
    });

    /* 上传图片 */
    var result = document.getElementById("result");
    var file = document.getElementById("file");
    //判断浏览器是否支持FileReader接口
    if(typeof FileReader === 'undefined')  {
        result.InnerHTML = "<p>你的浏览器不支持FileReader接口！</p>";
        //使选择控件不可操作
        file.setAttribute("disabled", "disabled"); //使得之前操作失效，重新启动
    }
    function readAsDataURL() {
        //检验是否为图像文件
        var file = document.getElementById("file").files[0];
        if(!/image\/\w+/.test(file.type)) {
            alert("这不是图片文件！请检查！");
            return false;
        }
        var reader = new FileReader();
        //将文件以Data URL形式读入页面
        reader.readAsDataURL(file);
        reader.onload = function(e) {
            var result = document.getElementById("result");
            //显示文件
            result.innerHTML = '<img src="' + this.result + '" alt=""/>';
        }
    }
