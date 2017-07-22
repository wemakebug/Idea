$(function () {


$(".allsign").click(function(){
	$("#moreNum").val(0)
	$("#signNum").val($(this).attr("sign"))
})

$(".more").click(function(){

	$.get("creations/")
})



})