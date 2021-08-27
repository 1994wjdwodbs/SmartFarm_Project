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
function Turn_Fan_Out(arg_val) {
   $.ajax({
      type:'POST',
      dataType:'JSON',
      url:'setProperty',
      data:{"COMMAND" : "FAN_OUT", "TURN" : arg_val},
      success : function(data) {
         console.log("Fan-Out : " + data)
        },
      error : function(e) {
         alert('Fan-Out Error!');
         return false;
      }
    });
}
function Turn_Pump(arg_val) {
   $.ajax({
      type:'POST',
      dataType:'JSON',
      url:'setProperty',
      data:{"COMMAND" : "PUMP", "TURN" : arg_val},
      success : function(data) {
         console.log("Pump : " + data)
        },
      error : function(e) {
         alert('Pump Error!');
         return false;
      }
    });
}
function Set_Led(arg_val) {
   $.ajax({
      type:'POST',
      dataType:'JSON',
      url:'setProperty',
      data:{"COMMAND" : "LED", "LED" : arg_val},
      success : function(data) {
         console.log("Led : " + data)
        },
      error : function(e) {
         alert('Led Error!');
         return false;
      }
    });
}

// 페이지 로드시 자동 실행하는 함수
$(document).ready(function() {
    // SetInterval (주기적 값 갱신용)

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
      if ($("#switch3").is(":checked")){
         Turn_Fan_Out("ON");
      }
      else
      {
         Turn_Fan_Out("OFF");
      }
    });

    // 펌프
    $('#switch4').change(function() {
      if ($("#switch4").is(":checked")){
         Turn_Pump("ON");
      }
      else
      {
         Turn_Pump("OFF");
      }
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

            $('.range-value').html(parseInt(data["LED"]));
            $('.input-range').val(parseInt(data["LED"]));
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
      Set_Led(this.value);
    });
});