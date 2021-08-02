from flask import Flask, render_template, request
app = Flask(__name__)

# (데코레이터) '/' 경로
@app.route("/")
def index():
    ip_address = request.remote_addr
    print("<Requester IP : " + ip_address + " >")
    print(request.get_data)
    # static/dummy.html 렌더링
    return render_template("dummy.html")
 
@app.route("/login")
def login():
    ip_address = request.remote_addr
    print("<Requester IP : " + ip_address + " >")
    print("<Login.html 접근>")
    print(request.get_data)
    # static/Login.html 렌더링
    return render_template("Login.html")

@app.route("/sign_up")
def sign_up():
    ip_address = request.remote_addr
    print("<Requester IP : " + ip_address + " >")
    print("<sign_up.html 접근>")
    print(request.get_data)
    # static/sign_up.html 렌더링
    return render_template("sign_up.html")

@app.route("/user_setting")
def user_setting():
    ip_address = request.remote_addr
    print("<Requester IP : " + ip_address + " >")
    print("<user_setting.html 접근>")
    print(request.get_data)
    # static/Usersetting.html 렌더링
    return render_template("Usersetting.html")

@app.route("/control")
def control():
    ip_address = request.remote_addr
    print("<Requester IP : " + ip_address + " >")
    print("<Control.html 접근>")
    print(request.get_data)
    # static/Control.html 렌더링
    return render_template("Control.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True)