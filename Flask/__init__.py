from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route("/")
def home():
    ip_address = request.remote_addr
    print("Requester IP: " + ip_address)
    return "Hi"
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True)