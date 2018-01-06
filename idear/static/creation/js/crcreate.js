$(document).ready(function (){
    var oDiv = document.getElementsByName("content_pro_label");
    for(var i=0;i<oDiv.length;i++){
        oDiv[i].onclick = function(){
            if(!this.style.backgroundColor ){
               this.style.backgroundColor = '#7194B8';
               this.style.color = '#ffffff';
            }else{
               this.style.backgroundColor = '';
               this.style.color = 'gray';
            }
        };
    }
})