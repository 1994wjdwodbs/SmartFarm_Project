// 센서별 ajax 요청 함수
function Turn_Fan_In(arg_val) {
   $.ajax({
      type:'POST',
      dataType:'JSON',
      url:'setProperty',
      data:{"COMMAND" : "FAN_IN", "TURN" : arg_val},
      success : function(data) {
         console.log("Fan-In : " + data)
        },
      error : function(e) {
         alert('Fan-In Error!');
         return false;
      }
    });
}

// 페이지 로드시 자동 실행하는 함수
$(document).ready(function() {
    // SetInterval (주기적 값 갱신용)

    // 조명
    $('#switch1').change(function() {
        // Dummy
    });
    // 환풍기 1
    $('#switch2').change(function() {
      if ($("#switch2").is(":checked")){
         Turn_Fan_In("ON");
      }
      else
      {
         Turn_Fan_In("OFF");
      }
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