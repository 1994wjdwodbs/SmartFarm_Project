from flask import Flask, render_template, Response, request, url_for
from flask.helpers import make_response
from camera import Camera
import time, datetime
import json
import serial
import sys
import signal
import os

# SF_machine database 제어용 py
import sf_db
# SF_machine 기계 제어용 py
import sf_sensor

# SF_machine 변수(GLOBAL)
idx = 0
LED = 0 # 0 ~ 100
w_level = 0 # 0 ~ 1024
l_level = 0 # 0 ~ 1024
s_level = 0 # 0 ~ 1024
pump = False
fan_in = False
fan_out = False
temp = 0.0 # 0.0 C (온도)
humi = 0.0 # 0.0 % (습도)

# Thread용 변수(GLOBAL)
temp_humi_flag = True

# sf_sensor 클래스 인스턴스 객체 생성
sf_machine = sf_sensor.Sensors()

# 웹 서버를 위한 Flask 객체 생성
app = Flask(__name__)
# RealTime 출력을 위한 Camera 객체 생성
camera = Camera()

# js,css 파일 캐싱 문제를 해결하기 위한 Static files versioning 
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

# 컨텍스트 프로세서들은 새로운 Value들을 
# 템플릿 컨텍스트에 주입시키기 위해 템플릿이 렌더링되기 전에 실행
@app.context_processor
def override_url_for(): # url_for 오버라이딩
    return dict(url_for=dated_url_for)

# Ctrl+C 핸들러 (카메라 리소스 해제)
def handler(signal, frame):
    print('CTRL-C pressed!')
    camera.close_cam()
    sys.exit(0)

# RealTime 출력을 위한 frame 생성 gen 함수
def gen(camera):
    while True:

        frame = camera.get_frame()
        # now = datetime.datetime.now()
        # print(now.strftime('%H:%M:%S RealTime Frame 생성'))

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# (데코레이터) AJAX 경로 (POST)
@app.route("/ajax_to_py", methods=['post'])
def ajax_to_py():
    print("넘어옴, id : " + request.form['id'])
    resp = app.response_class(
        response=json.dumps({"result":"5678"}),
        status=200,
        mimetype='application/json'
    )
    print(resp)
    return resp

@app.route("/Choco", methods=['post'])
def Choco():
    print("넘어옴, Name : " + request.form['Name'])
    resp = app.response_class(
        response=json.dumps({"result":"Hancom"}),
        status=200,
        mimetype='application/json'
    )
    print(resp)
    return resp
# (데코레이터) AJAX 경로 

# (데코레이터) '/getAllProperty'
@app.route("/getAllProperty", methods=['post'])
def get_AllProperty(): 
    global idx
    global LED 
    global w_level 
    global l_level 
    global s_level 
    global pump 
    global fan_in 
    global fan_out 
    global temp 
    global humi 

    print("getAllProperty 요청, id : " + request.form['id'])
    rec = sf_db.GetAllProperty()

    idx = rec[0]
    LED = rec[1]
    w_level = rec[2]
    l_level = rec[3]
    s_level = rec[4]
    pump = rec[5]
    fan_in = rec[6]
    fan_out = rec[7]
    temp = rec[8]
    humi = rec[9]

    resp = app.response_class(
        response=json.dumps({"idx" : idx, "LED" : LED, "w_level" : w_level, "l_level" : l_level, "s_level" : s_level, "pump" : pump, "fan_in" : fan_in, "fan_out" : fan_out, "temp" : temp, "humi" : humi}),
        status=200,
        mimetype='application/json'
    )
    print(resp)
    return resp

# (데코레이터) '/setProperty'
@app.route("/setProperty", methods=['post'])
def setProperty(): 
    global sf_machine

    COMMAND = request.form['COMMAND']
    
    if COMMAND == 'FAN_IN':
        if request.form['TURN'] == 'ON':
            sf_machine.SetFanIn(True)
            sf_db.SetProperty('fan_in', True)
            resp = app.response_class(
                response=json.dumps({"FAN_IN":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        else:
            sf_machine.SetFanIn(False)
            sf_db.SetProperty('fan_in', False)
            resp = app.response_class(
                response=json.dumps({"FAN_IN":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

# (데코레이터) '/address' 경로
@app.route("/")
def index():
    ip_address = request.remote_addr
    print("<requester IP : " + ip_address + " >")
    print(request.get_data)

    # static/dummy.html 렌더링
    return render_template("dummy.html")
 
@app.route("/login")
def login():
    ip_address = request.remote_addr
    print("<requester IP : " + ip_address + " >")
    print("<Login.html 접근>")
    print(request.get_data)
    # static/Login.html 렌더링
    return render_template("Login.html")

@app.route("/sign_up")
def sign_up():
    ip_address = request.remote_addr
    print("<requester IP : " + ip_address + " >")
    print("<sign_up.html 접근>")
    print(request.get_data)
    # static/sign_up.html 렌더링
    return render_template("sign_up.html")

@app.route("/user_setting")
def user_setting():
    ip_address = request.remote_addr
    print("<requester IP : " + ip_address + " >")
    print("<user_setting.html 접근>")
    print(request.get_data)
    # static/Usersetting.html 렌더링
    return render_template("Usersetting.html")

@app.route("/control")
def control():
    ip_address = request.remote_addr
    print("<requester IP : " + ip_address + " >")
    print("<Control.html 접근>")
    print(request.get_data)
    # static/Control.html 렌더링
    return render_template("Control.html")

# (데코레이터) RealTime 화면 송출을 위한 경로
@app.route('/video_feed')
def video_feed():
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    # 시그널 설정
    signal.signal(signal.SIGINT, handler)
    app.run(host='0.0.0.0', port=8080, threaded=True)

