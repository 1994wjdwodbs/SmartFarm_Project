// 페이지 로드시 자동 실행하는 함수
$(document).ready(function() {
    $('#switch1').change(function() {
        $.ajax({
          type:'POST',
          dataType:'JSON',
          url:'Choco',
          data:{"Name" : "coco"},
          success : function(data) {
             if ($("#switch1").is(":checked")){
                alert("On")
             }
             else
             {
                alert("Off")
             }
            },
        });
    });
    $('#switch2').change(function() {
        $.ajax({
          type:'POST',
          dataType:'JSON',
          url:'Choco',
          data:{"Name" : "coco"},
          success : function(data) {
             if ($("#switch2").is(":checked")){
                alert("On")
             }
             else
             {
                alert("Off")
             }
            },
        });
    });
    $('#switch3').change(function() {
        $.ajax({
          type:'POST',
          dataType:'JSON',
          url:'Choco',
          data:{"Name" : "coco"},
          success : function(data) {
             if ($("#switch3").is(":checked")){
                alert("On")
             }
             else
             {
                alert("Off")
             }
            },
        });
    });
    $('#switch4').change(function() {
      $.ajax({
        type:'POST',
        dataType:'JSON',
        url:'Choco',
        data:{"Name" : "coco"},
        success : function(data) {
           if ($("#switch4").is(":checked")){
              alert("On")
           }
           else
           {
              alert("Off")
           }
          },
      });
    });
    $(function (){ $("#pressMe").one("click", function(){
        alert("측정 시작"); 
      }); 
    });
    // Refresh 함수
    $("#refresh_sf").click(function(){
      $.ajax({
         type:'POST',
         dataType:'JSON',
         url:'getAllProperty',
         data:{"id" : "All"},
         success : function(data) {
            console.log(data);
         },
         error : function(e) {
            alert('Error!');
            return false;
         }
       });
    });
   //  LED Range 함수
    $('.input-range').on('input', function () {
      $(this).next('.range-value').html(this.value);
  });
});