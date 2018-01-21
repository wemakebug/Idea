// /**
//  * Created by zhanglingxue on 2017/10/16.
//  */
// alert("111")
//    /*标签选择 */
//     var oDiv = document.getElementsByName("chance_pro_label");
//     for(var i=0;i<oDiv.length;i++){
//         oDiv[i].onclick = function(){
//             if(!this.style.backgroundColor ){
//                this.style.backgroundColor = '#7194B8';
//                this.style.color = '#ffffff';
//             }else{
//                this.style.backgroundColor = '';
//                this.style.color = 'gray';
//             }
//         };
//     }
//
//     $("#agreeing").click(function () {
//         $(".pop-up").fadeToggle(500);
//         $(".wrap").fadeToggle(500);
//     });
//
//     $("#closing").click(function () {
//         $(".wrap").fadeToggle(500);
//         $(".pop-up").fadeToggle(500);
//     });
// });
//
//
//  /*cookie值转码*/
// function getCookie(name) {
//     var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
//     if (arr = document.cookie.match(reg))
//         return unescape(arr[2]);
//     else
//         return null;
// }
//
// /*创建人名称*/
// $(document).ready(function () {
//     var username = getCookie('username');
//     if (username === null || username === '') {
//
//     } else {
//         var email = $.cookie('email');
//         var username = $.cookie('username');
//         document.getElementById("username1").innerHTML = username;
//         document.getElementById("username2").innerHTML = username;
//         return;
//     }
// });
$(function () {
    //删除成员
     var num;
    $("#people").click(function () {
        var projectId = $("#projectId").val();
        var peopleId = $("#peopleId").val();
        var data = {
            'projectId': projectId,
            'peopleId':peopleId
        };
        num = $(this).index();
        $(".pop").fadeIn('fast');
        $(".popBottom").on('click', 'span', function (event) {
            event.preventDefault();
            if ($(this).hasClass('confirm')) {
                $.post('/idear/delpeople', data, function (result) {
                    result = JSON.parse(result);
                    if (result.status == 1) {
                        window.location.reload();
                    } else {
                        alert("删除错误")
                    }
                });
            } else {
                $(".pop").fadeOut();
                num = "";
            }
        });
    });

    //富文本中文字
    var description = $("#description").val();
    $('#summernote').summernote('code', description);

    //标签选择
    $(".chance_pro_label").on("click",function () {
            // var col = 'rgb' + '(' + Math.ceil(Math.random() * 245) + ',' + Math.ceil(Math.random() * 245) + ',' + Math.ceil(Math.random() * 245) + ')';
            var lables = $(this);
            var $radio = $(this);
            if ($radio.data('waschecked') == true){
              $radio.prop('checked', false);
              $radio.data('waschecked', false);
              lables.css('background-color','');
            } else {
              $radio.prop('checked', true);
              $radio.data('waschecked', true);
              lables.css('background-color','#87CEFA');
            }
        });

    //控制按钮选中状态
    var plan;
    var status = $("#status").val();
    if(status==1){
        $("#optionsRadios1").attr("checked","checked");
        plan=1;
    }else if (status==2){
        $("#optionsRadios2").attr("checked","checked");
        plan=2;
    }else if (status==3){
         $("#optionsRadios3").attr("checked","checked");
         plan=3;
    }else if (status==4){
         $("#optionsRadios4").attr("checked","checked");
         plan=4;
    }


    $("body").on("click","#releasePro",function () {
        var projectId = $("#projectId").val();
        //所需数据
        var proTitle = $(".input_title").val();//项目名称
        if(!proTitle ){
            alert("项目名称不能为空！");
        }
        var numPerson =$("#numPerson").val();//所需人数
        var re = /^[1-9]+.?[1-9]*$/; //判断数字正则表达式
        if(!re.test(numPerson)){
            alert("请输入大于0的数字");
            $("#numPerson").css("border","1px solid red");
            return ;
        }
        var proLabels = '';//项目标签
        var oDiv = document.getElementsByName("chance_pro_label");
        for(var i = 0;i < oDiv.length;i ++){
            if(oDiv[i].style.backgroundColor != "")
                proLabels+=oDiv[i].innerHTML + '*';
        }
        var tlabel;
        if(proLabels === ""){
            tlabel=0;
        }else {
            tlabel=1;
        }
        var coverMap = $(".file-preview-image").attr("src");
        var picture;//图片
        if(!coverMap){
            picture = 0;
            coverMap = 0;
        }else {
            picture = 1;
        }

        var postCon = $("#postCon").val();//招募贴
        var rhtml = $(".note-editable").get(0).innerHTML;//富文本
        if(!rhtml){
            alert("项目内容不能为空！");
        }
        var endTime = $("#flatpickr-tryme").val();//截止时间
        if(!endTime){
            alert("请选择结束时间！");
        }
        var data={
            "proTitle": proTitle,
            "coverMap": coverMap,
            "picture":picture,
            "rhtml": rhtml,
            "numPerson": numPerson,
            "endTime": endTime,
            "proLabels": proLabels,
            "tlabel":tlabel,
            "postCon": postCon,
            "plan": plan
        };
        $.post("/idear/PM_content/"+projectId,data,function (result) {
            var result = JSON.parse(result);
            if(result.status){
                alert("修改成功");
            }
        });
    });

});

