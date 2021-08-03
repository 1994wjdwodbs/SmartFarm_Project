function sayHello() {
    alert("Hello world");
}

function ajaxTest() {
    $.ajax({
        type : "POST",
        url : "ajax_to_py",
        data : {"id" : "1234"},
        dataType : "json", // xml, json, html, text ..
        async : false,
        success : function(data) {
            // alert(data.dup);
            
            // $('#id_duplicate').val(data.dup);
            // #("label[for='label_ID']").text('');
            $("label[for='btn1']").text(data.result)
        },
        error : function(e) {
            alert('Error!');
            return false;
        }
    });
}

// 페이지 로드시 자동 실행하는 함수
$(document).ready(function() {
    // JQuery Test
    $('input[id=btn1]').val('button1');
	sayHello();
});