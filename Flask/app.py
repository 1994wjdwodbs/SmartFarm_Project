from flask import Flask, render_template, request
app = Flask(__name__)

# (데코레이터) '/' 경로
@app.route("/")
def index():
    ip_address = request.remote_addr
    print("<Requester IP : " + ip_address + " >")
    print(request.data)
    # static/dummy.html 렌더링
    return render_template("dummy.html")
 
@app.route("/login")
def login():
    
    # static/Login.html 렌더링
    return render_template("Login.html")

@app.route("/sign_up")
def sign_up():

    # static/sign_up.html 렌더링
    return render_template("sign_up.html")

@app.route("/user_setting")
def user_setting():

    # static/Usersetting.html 렌더링
    return render_template("Usersetting.html")

@app.route("/control")
def control():

    # static/Control.html 렌더링
    return render_template("Control.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True)