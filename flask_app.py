from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "hello there"

@app.route("/template")
def template():
    return render_template("index.html")

@app.route("/getname", methods=["GET"])
def login():
    name = request.args.get('name', default = 1, type = str)
    surname = request.args.get('surname', default = 1, type = str)
    return f"Hello {name} {surname}"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')