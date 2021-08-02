from flask import Flask, render_template, request
app = Flask(__name__)

# (데코레이터) '/' 경로
@app.route("/")
def index():
    ip_address = request.remote_addr
    print("Requester IP: " + ip_address)
    # static/dummy.html 렌더링
    return render_template("dummy.html")
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True)