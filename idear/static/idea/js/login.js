$("#login_input").on('click',function () {
    var school=$(".school").var()
    var account=$(".account").val()
    var password=$(".password").val()
if (school==""||school==undefined||school==null){
    if (account==""||account==undefined||account==null){
        if(password ==""||password==undefined||password==null){
            $(".warning").css({ display: 'block' });
        }
        else {
            $("#warn0").css({ display: 'block' });
            $("#warn1").css({ display: 'block' });
            $("#warn2").css({ display: 'none' });
        }
    }
    else{if(password ==""||password==undefined||password==null){
            $("#warn0").css({ display: 'block' });
            $("#warn1").css({ display: 'none' });
            $("#warn2").css({ display: 'block' })
        }
        else {
            $("#warn0").css({ display: 'block' });
            $("#warn1").css({ display: 'none' });
            $("#warn2").css({ display: 'none' })
        }
    }
}
else {
    if (account==""||account==undefined||account==null){
         if(password ==""||password==undefined||password==null){
            $("#warn0").css({ display: 'none' });
            $("#warn1").css({ display: 'block' });
            $("#warn2").css({ display: 'block' });
        }
        else {
            $("#warn0").css({ display: 'none' });
            $("#warn1").css({ display: 'block' });
            $("#warn2").css({ display: 'none' });
        }
    }else {if(password ==""||password==undefined||password==null){
            $("#warn0").css({ display: 'none' });
            $("#warn1").css({ display: 'none' });
            $("#warn2").css({ display: 'block' })
        }
        else{
            $("#warn0").css({ display: 'none' });
            $("#warn1").css({ display: 'none' });
            $("#warn2").css({ display: 'none' })
        }
    }
}
    
})

// 点击登陆，返回上一访问页面
        function make() {


        }
