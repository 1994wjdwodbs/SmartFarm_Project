from flask import Flask, render_template, Response, request
from camera import Camera
import time
import serial
import sys
import signal

# 웹 서버를 위한 Flask 객체 생성
app = Flask(__name__)
# RealTime 출력을 위한 Camera 객체 생성
camera = Camera()

# Ctrl+C 핸들러 (카메라 리소스 해제)
def handler(signal, frame):
    print('CTRL-C pressed!')
    camera.close_cam()
    sys.exit(0)

# RealTime 출력을 위한 frame 생성 gen 함수
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

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
    app.run(host='0.0.0.0', port=8080, threaded=True)
    # 시그널 설정
    signal.signal(signal.SIGINT, handler)