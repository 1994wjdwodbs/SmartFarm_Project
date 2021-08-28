import threading
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
# idx = 0
# LED = 0 # 0 ~ 100
# w_level = 0 # 0 ~ 1024
# l_level = 0 # 0 ~ 1024
# s_level = 0 # 0 ~ 1024
# pump = False
# fan_in = False
# fan_out = False
# temp = 0.0 # 0.0 C (온도)
# humi = 0.0 # 0.0 % (습도)

# Thread용 변수(GLOBAL)
temp_humi_flag = True
check_level_flag = True
shutdown_flag = False

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

def ShutDown_SF():
    # shutdown 플래그일때만 작동
    while not shutdown_flag:
        pass
    
    time.sleep(3)

    camera.close_cam()
    sf_machine.close()
    sig = getattr(signal, "SIGKILL", signal.SIGTERM)
    os.kill(os.getpid(), sig)

# Ctrl+C 핸들러 (카메라 리소스 해제)
def handler(signal, frame):
    print("[Server shutdown 요청]")
    shutdown_flag = True
    ShutDown_SF()

# RealTime 출력을 위한 frame 생성 gen 함수
def gen(camera):
    while True:

        frame = camera.get_frame()
        # now = datetime.datetime.now()
        # print(now.strftime('%H:%M:%S RealTime Frame 생성'))

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# 센서 DB 저장값으로 셋팅 초기화
def Init_Sensor():
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

    sf_machine.SetFanIn(fan_in)
    sf_machine.SetFanOut(fan_out)
    sf_machine.SetPump(pump)
    sf_machine.SetLedLight(LED)

# (데코레이터) AJAX 경로 (POST)
@app.route("/shutdown", methods=['post'])
def shutdown():
    global shutdown_flag

    ip_address = request.remote_addr
    print("[Client shutdown 요청, ip : " + ip_address + "]")
    resp = app.response_class(
        response=json.dumps({"result":"10초 후 Smart Farm 서버가 종료됩니다."}),
        status=200,
        mimetype='application/json'
    )
    shutdown_flag = True
    return resp

# (데코레이터) '/getAllProperty'
@app.route("/getAllProperty", methods=['post'])
def get_AllProperty(): 

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
        print("FAN_IN")
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

    if COMMAND == 'FAN_OUT':
        print("FAN_OUT")
        if request.form['TURN'] == 'ON':
            sf_machine.SetFanOut(True)
            sf_db.SetProperty('fan_out', True)
            resp = app.response_class(
                response=json.dumps({"FAN_OUT":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        else:
            sf_machine.SetFanOut(False)
            sf_db.SetProperty('fan_out', False)
            resp = app.response_class(
                response=json.dumps({"FAN_OUT":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

    if COMMAND == 'PUMP':
        print("PUMP")
        if request.form['TURN'] == 'ON':
            sf_machine.SetPump(True)
            sf_db.SetProperty('pump', True)
            resp = app.response_class(
                response=json.dumps({"PUMP":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        else:
            sf_machine.SetPump(False)
            sf_db.SetProperty('pump', False)
            resp = app.response_class(
                response=json.dumps({"PUMP":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

    if COMMAND == 'LED':
        print("LED")
        
        sf_machine.SetLedLight(int(request.form['LED']))
        sf_db.SetProperty('led', int(request.form['LED']))
        resp = app.response_class(
            response=json.dumps({"LED":request.form['LED']}),
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
    
    print("[센서 초기 설정 중...]")
    Init_Sensor()
    # 센서 초기화 시간
    time.sleep(1)
    print("[센서 설정 완료]")
    
    print("[스레드 초기 설정 중...]")
    check_level_t = threading.Thread(target=sf_machine.CheckLevel, args=(3,))
    check_level_t.start()
    temp_humi_t = threading.Thread(target=sf_machine.CheckTempHumi, args=(3,))
    temp_humi_t.start()
    # 유저 종료 전용 스레드
    SF_DOWN = threading.Thread(target=ShutDown_SF)
    SF_DOWN.start()
    # 스레드 초기화 시간
    time.sleep(3.1)
    print("[스레드 설정 완료]")
    
    print("[스마트팜 가동 시작]")
    app.run(host='0.0.0.0', port=8080, threaded=True)

