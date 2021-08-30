import threading
from flask import Flask, render_template, Response, request, url_for, session
from flask.helpers import make_response
from camera import Camera
import time, datetime
import json
import serial
import sys
import signal
import os
import datetime

# 웹소켓 (SocketIO 전용 라이브러리 추가)
from flask_socketio import SocketIO, emit, send

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
shutdown_flag_2 = True

# sf_sensor 클래스 인스턴스 객체 생성
sf_machine = sf_sensor.Sensors()

# 채팅, 로그용 리스트 변수
chat_list = []
log_list = []

# 웹 서버, 소켓IO를 위한 Flask, SocketIO 객체 생성
app = Flask(__name__)
app.secret_key = "temp_key"
# socketio = SocketIO(app)
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
    global shutdown_flag
    global shutdown_flag_2

    # shutdown 플래그일때만 작동
    while not shutdown_flag and shutdown_flag_2:
        pass
    print('셧다운 가동')
    shutdown_flag_2 = False

    time.sleep(3)

    camera.close_cam()
    sf_machine.close()

    # 로그 파일 작성
    print('로그 파일 작성 중...')
    f = open('log' + datetime.datetime.now().strftime('%y%m%d_%H%M%S') + '.txt', 'wt')
    for i in log_list:
        f.write(i + '\n')
    f.close()
    print('로그 파일 작성 완료')

    sig = getattr(signal, "SIGKILL", signal.SIGTERM)
    os.kill(os.getpid(), sig)

# Ctrl+C 핸들러 (카메라 리소스 해제)
def handler(signal, frame):
    global shutdown_flag
    # global socketio

    now = datetime.datetime.now().strftime('(%H:%M:%S)')

    print("[Server shutdown 요청]")
    InputLog(f' [{now} Server] Smart Farm Shutdown (Power-Off)')
    # socketio 호출을 이용한 외부에서 socket emit
    # socketio.emit("logs", {'message' : f' [{now} Server] Smart Farm Shutdown 명령', 'type' : 'cmd'}, namespace='/log', broadcast=True)

    shutdown_flag = True

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

# 채팅 입력 동시 접근 방지
mutex_chat = threading.Lock()

def InputChat(msg):
    global chat_list
    print('msg : ' + msg)
    mutex_chat.acquire()
    if len(chat_list) >= 10:
        del chat_list[9]
        chat_list.insert(0, msg)
    else:
        chat_list.insert(0, msg)
    mutex_chat.release()

def OutputChat():
    global chat_list
    
    str = ''
    for i in chat_list:
        str = str + i + '\n'
        print('chat : ' + i)

    return str

# 로그 입력 동시 접근 방지
mutex_log = threading.Lock()

def InputLog(msg):
    global log_list
    print('log : ' + msg)
    mutex_log.acquire()
    log_list.insert(0, msg)
    mutex_log.release()

def OutputLog():
    global log_list
    
    str = ''
    for i in log_list:
        str = str + i + '\n'
        print('log : ' + i)

    return str

# 세션 아이디 부여 동시 접근 방지
mutex_session = threading.Lock()

# app 첫 리퀘스트 전 (요청 페이지에 대한 세션 설정)
@app.before_first_request
def before_first_request():
    session.clear()

# (데코레이터) AJAX 경로 (POST)
@app.route("/shutdown", methods=['post'])
def shutdown():
    # global socketio
    global shutdown_flag

    user_id = session['user-id']
    now = datetime.datetime.now().strftime('(%H:%M:%S)')

    ip_address = request.remote_addr
    print("[Client shutdown 요청, ip : " + ip_address + "]")
    InputLog(f' [{now} {user_id}] Smart Farm Shutdown (Power-Off)')
    # socketio 호출을 이용한 외부에서 socket emit
    # socketio.emit("logs", {'message' : f' [{now} {user_id}] SmartFarm Shutdown 명령', 'type' : 'cmd'}, namespace='/log', broadcast=True)
    
    shutdown_flag = True

    resp = app.response_class(
        response=json.dumps({"result":"10초 후 Smart Farm 서버가 종료됩니다."}),
        status=200,
        mimetype='application/json'
    )
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
    # global socketio

    user_id = session['user-id']
    now = datetime.datetime.now().strftime('(%H:%M:%S)')
    COMMAND = request.form['COMMAND']
    
    if COMMAND == 'FAN_IN':
        print("FAN_IN")
        
        if request.form['TURN'] == 'ON':
            sf_machine.SetFanIn(True)
            sf_db.SetProperty('fan_in', True)
            InputLog(f' [{now} {user_id}] Fan-In : On')
            resp = app.response_class(
                response=json.dumps({"FAN_IN":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            # socketio 호출을 이용한 외부에서 socket emit
            # socketio.emit("logs", {'message' : f' [{now} {user_id}] Fan-In : On 명령', 'type' : 'cmd'}, namespace='/log', broadcast=True)
            return resp
        else:
            sf_machine.SetFanIn(False)
            sf_db.SetProperty('fan_in', False)
            InputLog(f' [{now} {user_id}] Fan-In : Off')
            resp = app.response_class(
                response=json.dumps({"FAN_IN":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            # socketio 호출을 이용한 외부에서 socket emit
            # socketio.emit("logs", {'message' : f' [{now} {user_id}] Fan-In : Off 명령', 'type' : 'cmd'}, namespace='/log', broadcast=True)
            return resp

    if COMMAND == 'FAN_OUT':
        print("FAN_OUT")
        if request.form['TURN'] == 'ON':
            sf_machine.SetFanOut(True)
            sf_db.SetProperty('fan_out', True)
            InputLog(f' [{now} {user_id}] Fan-Out : On')
            resp = app.response_class(
                response=json.dumps({"FAN_OUT":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            # socketio 호출을 이용한 외부에서 socket emit
            # socketio.emit("logs", {'message' : f' [{now} {user_id}] Fan-Out : On 명령', 'type' : 'cmd'}, namespace='/log', broadcast=True)
            return resp
        else:
            sf_machine.SetFanOut(False)
            sf_db.SetProperty('fan_out', False)
            InputLog(f' [{now} {user_id}] Fan-Out : Off')
            resp = app.response_class(
                response=json.dumps({"FAN_OUT":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            # socketio 호출을 이용한 외부에서 socket emit
            # socketio.emit("logs", {'message' : f' [{now} {user_id}] Fan-Out : Off 명령', 'type' : 'cmd'}, namespace='/log', broadcast=True)
            return resp

    if COMMAND == 'PUMP':
        print("PUMP")
        if request.form['TURN'] == 'ON':
            sf_machine.SetPump(True)
            sf_db.SetProperty('pump', True)
            InputLog(f' [{now} {user_id}] Pump : On')
            resp = app.response_class(
                response=json.dumps({"PUMP":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            # socketio 호출을 이용한 외부에서 socket emit
            # socketio.emit("logs", {'message' : f' [{now} {user_id}] Pump : On 명령', 'type' : 'cmd'}, namespace='/log', broadcast=True)
            return resp
        else:
            sf_machine.SetPump(False)
            sf_db.SetProperty('pump', False)
            InputLog(f' [{now} {user_id}] Pump : Off')
            resp = app.response_class(
                response=json.dumps({"PUMP":"ON"}),
                status=200,
                mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*'
            # socketio 호출을 이용한 외부에서 socket emit
            # socketio.emit("logs", {'message' : f' [{now} {user_id}] Pump : Off 명령', 'type' : 'cmd'}, namespace='/log', broadcast=True)
            return resp

    if COMMAND == 'LED':
        print("LED")
        
        sf_machine.SetLedLight(int(request.form['LED']))
        sf_db.SetProperty('led', int(request.form['LED']))
        InputLog(f' [{now} {user_id}] LED : ' + request.form['LED'] + ' 조절')
        resp = app.response_class(
            response=json.dumps({"LED":request.form['LED']}),
            status=200,
            mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        # socketio 호출을 이용한 외부에서 socket emit
        # socketio.emit("logs", {'message' : f' [{now} {user_id}] LED : ' + request.form['LED'] + ' 조절', 'type' : 'cmd'}, namespace='/log', broadcast=True)
        return resp

# (데코레이터) '/chat'
@app.route("/chat", methods=['post'])
def chats(): 
    global sf_machine
    global clients
    # global socketio

    user_id = session['user-id']
    now = datetime.datetime.now().strftime('(%H:%M:%S)')
    COMMAND = request.form['COMMAND']
    
    if COMMAND == 'IN':
        print("[CHAT IN]")

        mutex2.acquire()
        clients += 1
        mutex2.release()

        InputChat(f' {now} {user_id}가 입장하였습니다. [전체 {clients}명 접속 중]')
        resp = app.response_class(
            response=json.dumps({"messages":OutputChat()}),
            status=200,
            mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
        
    if COMMAND == 'SEND':
        print("[CHAT SEND]")
        
        InputChat(' ' + now + ' ' + user_id + ' : ' + request.form['MSG'])
        resp = app.response_class(
            response=json.dumps({"messages":OutputChat()}),
            status=200,
            mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    if COMMAND == 'RECV':
        print("[CHAT RECV]")
        
        resp = app.response_class(
            response=json.dumps({"messages":OutputChat()}),
            status=200,
            mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    if COMMAND == 'OUT':
        print("[CHAT OUT]")

        mutex2.acquire()
        clients -= 1
        mutex2.release()

        InputChat(f' {now} {user_id}가 퇴장하였습니다. [전체 {clients}명 접속 중]')
        resp = app.response_class(
            response=json.dumps({"MSG":OutputChat()}),
            status=200,
            mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

# (데코레이터) '/chat'
@app.route("/log", methods=['post'])
def logs(): 
    global sf_machine
    global clients
    # global socketio

    user_id = session['user-id']
    now = datetime.datetime.now().strftime('(%H:%M:%S)')
    COMMAND = request.form['COMMAND']

    if COMMAND == 'RECV':
        print("[LOG RECV]")
        
        resp = app.response_class(
            response=json.dumps({"messages":OutputLog()}),
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
    global user_num
    global clients

    if not ('session' in session and 'user-id' in session):
        mutex_session.acquire()
        session['session'] = os.urandom(24)
        session['user-id'] = 'user' + str(user_num)
        user_num += 1
        mutex_session.release()

    user_id = session['user-id']
    now = datetime.datetime.now().strftime('(%H:%M:%S)')

    mutex2.acquire()
    clients += 1
    mutex2.release()

    InputChat(f' {now} {user_id}가 입장하였습니다. [전체 {clients}명 접속 중]')

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

# socket_io 부분
user_num = 1
clients = 0 # 전체 접속자 수

mutex2 = threading.Lock()

# socket_io 채팅 영역
# @socketio.on('connect', namespace='/chat')
# def connect():
#     print('[socket:/chat 첫 접속]')
#     global clients

#     mutex2.acquire()
#     clients += 1
#     mutex2.release()
    
#     user_id = session['user-id']
#     now = datetime.datetime.now().strftime('(%H:%M:%S)')
#     emit("message", {'message' : f' {now} {user_id}가 입장하였습니다. [전체 {clients}명 접속 중]', 'type' : 'chat'}, broadcast=True)
# @socketio.on('disconnect', namespace='/chat')
# def disconnect():
#     print('[socket:/chat 접속 해제]')
#     global clients

#     mutex2.acquire()
#     clients -= 1
#     mutex2.release()
    
#     user_id = session['user-id']
#     now = datetime.datetime.now().strftime('(%H:%M:%S)')
#     emit("message", {'message' : f' {now} {user_id}가 퇴장하였습니다. [전체 {clients}명 접속 중]', 'type' : 'chat'}, broadcast=True)
#     session.clear() # 세션 초기화
# @socketio.on("message", namespace='/chat')
# def request_chat(User):
#     print("[recv] message from " + session['user-id'] + " : " + User['message'])
#     to_client = dict()
#     user_id = session['user-id']
#     now = datetime.datetime.now().strftime('(%H:%M:%S)')
#     to_client['message'] = ' ' + now + ' ' + user_id + ' : ' + User['message']
#     to_client['type'] = 'chat'
#     # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
#     send(to_client, broadcast=True)

# socket_io 로그 영역
# @socketio.on('connect', namespace='/log')
# def connect():
#     pass
# @socketio.on('disconnect', namespace='/log')
# def disconnect():
#     pass
# @socketio.on("logs", namespace='/log')
# def request_log(SF_Mach):
#     global clients
#     print("[recv] message from " + session['user-id'] + " : " + SF_Mach['message'])
#     to_client = dict()
#     user_id = session['user-id']
#     now = datetime.datetime.now().strftime('(%H:%M:%S)')
#     to_client['message'] = ' ' + now + ' ' + user_id + ' : ' + SF_Mach['message']
#     to_client['type'] = 'cmd'
#     # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
#     send(to_client, broadcast=True)

if __name__ == "__main__":

    InputLog('################')
    now = datetime.datetime.now().strftime('(%H:%M:%S)')
    InputLog(f' [{now} Server] Smart Farm 시작 (Power-On)')

    # 시그널 설정
    signal.signal(signal.SIGINT, handler)
    
    now = datetime.datetime.now().strftime('(%H:%M:%S)')
    InputLog(f' [{now} Server] Smart Farm 센서 설정 중...')
    print("[센서 초기 설정 중...]")
    Init_Sensor()
    # 센서 초기화 시간
    time.sleep(1)
    now = datetime.datetime.now().strftime('(%H:%M:%S)')
    InputLog(f' [{now} Server] Smart Farm 센서 설정 완료')
    print("[센서 설정 완료]")

    now = datetime.datetime.now().strftime('(%H:%M:%S)')
    InputLog(f' [{now} Server] Smart Farm 스레드 설정 중...')
    print("[스레드 초기 설정 중...]")
    check_level_t = threading.Thread(target=sf_machine.CheckLevel, args=(3,))
    check_level_t.start()
    temp_humi_t = threading.Thread(target=sf_machine.CheckTempHumi, args=(3,))
    temp_humi_t.start()
    shutdown_t = threading.Thread(target=ShutDown_SF)
    shutdown_t.start()
    # 스레드 초기화 시간
    time.sleep(3.1)
    now = datetime.datetime.now().strftime('(%H:%M:%S)')
    InputLog(f' [{now} Server] Smart Farm 스레드 설정 완료')
    print("[스레드 설정 완료]")

    now = datetime.datetime.now().strftime('(%H:%M:%S)')
    InputLog(f' [{now} Server] Smart Farm 동작')
    print("[스마트팜 가동 시작]")
    InputLog('################')
    # socketio.run(app, host='0.0.0.0', port=8080)
    app.run(host='0.0.0.0', port=8080, threaded=True)

