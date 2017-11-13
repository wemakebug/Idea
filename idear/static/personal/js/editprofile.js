/**
 * Created by admin on 2017/10/18.
 */


$("#backhomepage").click(function (){
    window.location.href = "homepage";
});

$("#editcontent1-3").click(function () {
    $("#editcontent1-33").addClass("editcontent11-3");
    $("#personalinformation").removeClass("publicclass1-1");
    $("#editmaincontect").addClass("publicclass1-1");
    $("#editcontent1-44").removeClass("publicclass");
    $("#changepassword").addClass("publicclass1-1");

});
$("#editcontent1-4").click(function () {
    $("#editcontent1-44").addClass("publicclass");
    $("#editmaincontect").removeClass("publicclass1-1");
    $("#personalinformation").addClass("publicclass1-1");
    $("#changepassword").addClass("publicclass1-1");
    $("#editcontent1-33").removeClass("editcontent11-3");

});
$("#editcontent1-5").click(function () {
    $("#editmaincontect").addClass("publicclass1-1");
    $("#personalinformation").addClass("publicclass1-1");
    $("#editcontent1-55").addClass("publicclass");
    $("#changepassword").removeClass("publicclass");
    $("#editcontent1-44").removeClass("publicclass");
});