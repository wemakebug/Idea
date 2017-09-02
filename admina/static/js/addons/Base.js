/**
 * Created by chrisprosise on 17-8-31.
 */

function getCookie(name)
{
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");

    if(arr=document.cookie.match(reg))

        return arr[2];
    else
        return null;
}

$(document).ready(function () {
   var account = getCookie('account');
   var content = document.getElementById('base_logout');
   var user = document.getElementById('base_username');
   if(account === null || account === '' || account === undefined ){
        //后台用户显示  
       user.textContent = '数据异常，请先登陆！';
       content.textContent = '登陆';
       content.href = 'login';
       alert(content.href);
       
   }else{
      user.textContent = account;
      content.textContent = '注销'
   }
   
});