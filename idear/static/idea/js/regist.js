/**
 * Created by admin on 2017/7/17.
 */
// $(function(){
//     document.getElementsByName("name")[0].focus();
// });
$(document).ready(function(){
    $("#reset").click (function () {
        $("input[name='name']").val("");
        $("input[name='account']").val("");
        $("input[name='password']").val("");
        $("input[name='ConfirmPassword']").val("");
        $("input[name='email']").val("");
        $("input[name='opinion']").val("");
    })
});
