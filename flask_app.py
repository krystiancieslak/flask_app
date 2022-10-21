from crypt import methods
from flask import Flask, render_template, request, redirect, session
import random
import uuid

app = Flask(__name__)
app.config["SECRET_KEY"] = uuid.uuid4().hex

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
    print("-------------------------------NEW REQUEST------------------------------")
    if request.method == "POST":
        print("This is POST flow")
    if request.method == "GET":
        print("This is GET flow")
        session["a"] = random.randint(0,9)
        session["b"] = random.randint(0,9)

    print("This is happening every time")

    a=session["a"]
    b=session["b"]
    username=session.get("username", "Username")

    print("Current values used for checking:")
    print(f"current value of a: {a}")
    print(f"current value of b: {b}")
    print(f"current value of username: {username}")
    try:
        print(f"current value of desired_value: {desired_value}")
    except Exception as e:
        print (f"Cannot print desired_value, error: {e}")

    if request.method == "POST":
        print("This is happening only in POST")
        desired_value = a + b
        
        print("Getting username, password and verify value...")
        username = request.form.get('username')
        session["username"] = username
        password = request.form.get('password')
        verify = request.form.get('verify')

        print("Current values used for checking:")
        print(f"current value of a: {a}")
        print(f"current value of b: {b}")
        print(f"current value of username: {username}")
        try:
            print(f"current value of desired_value: {desired_value}")
        except Exception as e:
            print (f"Cannot print desired_value, error: {e}")
        print(f"current value of verify: {verify}")

        if (username == "admin") and (password == "admin") and (int(verify) == desired_value):
            print("Credentials are correct")
            error = None
            return redirect("/")
        else:
            error = "Invalid credentials"
            return redirect("/login")
    else:
        return render_template("login.html", a=a, b=b, username=username)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')