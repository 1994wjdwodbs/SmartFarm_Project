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
    $('#switch5').change(function() {
        $.ajax({
          type:'POST',
          dataType:'JSON',
          url:'Choco',
          data:{"Name" : "coco"},
          success : function(data) {
             if ($("#switch5").is(":checked")){
                alert("On")
             }
             else
             {
                alert("Off")
             }
            },
        });
    });
    $('#switch6').change(function() {
        $.ajax({
          type:'POST',
          dataType:'JSON',
          url:'Choco',
          data:{"Name" : "coco"},
          success : function(data) {
             if ($("#switch6").is(":checked")){
                alert("On")
             }
             else
             {
                alert("Off")
             }
            },
        });
    });
    $('#switch7').change(function() {
        $.ajax({
          type:'POST',
          dataType:'JSON',
          url:'Choco',
          data:{"Name" : "coco"},
          success : function(data) {
             if ($("#switch7").is(":checked")){
                alert("On")
             }
             else
             {
                alert("Off")
             }
            },
        });
    });
});