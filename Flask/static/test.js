var sensor_timer;

// 센서별 수치 리프레시 함수
function refresh_sensor() {
   $.ajax({
      type:'POST',
      dataType:'JSON',
      url:'getAllProperty',
      data:{"id" : "All"},
      success : function(data) {
         console.log(data);
         // 스위치 값 변경
         $('#switch2').prop('checked', parseInt(data["fan_in"]));
         $('#switch3').prop('checked',parseInt(data["fan_out"]));
         $('#switch4').prop('checked',parseInt(data["pump"]));

         // 수치 값 변경
         $('#p_temp').text("현재온도 : " + data["temp"] + "℃");
         $('#p_humi').html("현재습도 : " + data["humi"] + "%<br/>토양습도 : " + parseInt((parseInt(data["s_level"],10)/1024)*100) + "%");
         $('#p_lux').text("현재조도 : " + parseInt(((1024-parseInt(data["l_level"],10))/1024)*100) + "lx");
         $('#p_water').text("현재수위 : " + parseInt((parseInt(data["w_level"],10)/1024)*100) + "%");
         $('.range-value').html(parseInt(data["LED"]));
         $('.input-range').val(parseInt(data["LED"]));
      },
      error : function(e) {
         alert('Error!');
         return false;
      }
   });
}

// 스마트팜 Server, Machine 종료 요청 함수
function SF_ShutDown() {
   clearInterval(sensor_timer);
   $.ajax({
      type:'POST',
      dataType:'JSON',
      url:'shutdown',
      data:{},
      success : function(data) {
         alert(data["result"]);
        },
      error : function(e) {
         alert('Shutdown Error!');
         return false;
      }
    });
}

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
    refresh_sensor();
    // SetInterval (주기적 값 갱신용)
    sensor_timer = setInterval(refresh_sensor, 3000);
    
    // socketio chat
    var socket_chat = io.connect("http://210.119.12.78:13640/chat")
    socket_chat.on('message', function(msg){
      $("#chat_area").val(msg.message + '\n' + $("#chat_area").val());
    });
    $('#send_text').keypress(function(e) {
      if(e.keyCode == 13) {
         socket_chat.emit('message', {'type' : 'normal', 'message' : $('#send_text').val()})
         $('#send_text').val("");
      }
    });
    $('#send_btn').click(function() {
      socket_chat.emit('message', {'type' : 'normal', 'message' : $('#send_text').val()})
      $('#send_text').val("");
   });

    // socketio log
    var socket_log = io.connect("http://210.119.12.78:13640/log")
    socket_log.on('logs', function(msg){
      $("#log_area").val(msg.message + '\n' + $("#log_area").val());
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

    // Refresh 설정
    $("#refresh_sf").click(function(){
      refresh_sensor();
    });
    
    // Shutdown 설정
    $("#PowerOff").click(function(){
      SF_ShutDown();
    });

   //  LED Range 설정
    $('.input-range').on('input', function () {
      $(this).next('.range-value').html(this.value);
      Set_Led(this.value);
    });
});