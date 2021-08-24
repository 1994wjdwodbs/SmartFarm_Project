

// 페이지 로드시 자동 실행하는 함수
$(document).ready(function() {
   // 조명
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
    // 환풍기 1
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
    // 환풍기 2
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
    // 펌프
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
            $('#switch2').prop('checked', parseInt(data["fan_in"]));
            $('#switch3').prop('checked',parseInt(data["fan_out"]));
            $('#switch4').prop('checked',parseInt(data["pump"]));
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