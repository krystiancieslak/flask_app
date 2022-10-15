from crypt import methods
from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "hello there"

@app.route("/template")
def template():
    return render_template("index.html")

@app.route("/getname", methods=["GET"])
def getname():
    name = request.args.get('name', default = "Test", type = str)
    surname = request.args.get('surname', default = "Testing", type = str)
    return f"Hello {name} {surname}"

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        a=random.randint(0,9)
        b=random.randint(0,9)
        c=a+b
        print(c)
        print(f"{a}+{b}=")
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        verify = request.form.get('verify')
        print(verify)
        if (username == "admin") and (password == "admin") and (int(verify)==c):
            error = None
            return redirect("/")
        else:
            error = "Invalid credentials"
            return error
    else:
        return render_template("login.html", a=a, b=b)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')