/**
 * Created by zhanglingxue on 2017/10/16.
 */
        /*富文本固定*/
    window.onload = function () {
        var oDiv = document.getElementById("cke_1_top"),
            H = 0,
            Y = oDiv;
        while (Y) {
            H += Y.offsetTop;
            Y = Y.offsetParent
        }
        window.onscroll = function () {
            var s = document.body.scrollTop || document.documentElement.scrollTop;
            if (s > H) {
                oDiv.style = "position:fixed;top:66px;width:43.88%;min-width:647px;"
            } else {
                oDiv.style = ""
            }
        }
    }
        /*项目公开程度*/
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
