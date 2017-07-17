/**
 * Created by admin on 2017/7/17.
 */
// $(function(){
//     document.getElementsByName("name")[0].focus();
// });
$("input[name='reset']").click(function () {
    $("input[name='name']").val("");
    $("input[name='account']").val("");
    $("input[name='password']").val("");
    $("input[name='ConfirmPassword']").val("");
    $("input[name='school']").val("");
    $("input[name='email']").val("");
});
