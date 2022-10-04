from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "hello there"

@app.route("/template")
def template():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run()