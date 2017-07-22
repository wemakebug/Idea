/**
 * Created by admin on 2017/7/17.
 */
$(function(){
    document.getElementsByName("name")[0].focus();
});
$(document).ready(function(){
    $("#reset").click (function () {
        $("input[name='name']").val("");
        $("input[name='account']").val("");
        $("input[name='password']").val("");
        $("input[name='ConfirmPassword']").val("");
        $("input[name='email']").val("");
        $("input[name='opinion']").attr("checked",false);
    })
});
$(document).ready(function(){
    $("#agreeing").click (function () {
        $(".pop-up").fadeToggle(500);
        $(".wrap").fadeToggle(500);
    })
});

$(document).ready(function(){
    $("#closing").click (function () {
        $(".wrap").fadeToggle(500);
        $(".pop-up").fadeToggle(500);
    })
});

