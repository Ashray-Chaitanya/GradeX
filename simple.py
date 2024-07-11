from flask import Flask, render_template

app = Flask(__name__, static_folder="static", static_url_path="/static")
FedCorp = "Nitte Noob"

@app.route("/", methods=["GET"])
def home():
  return render_template("index.html")

@app.route("/login", methods=["GET"])
def login():
  return render_template("login.html")

app.run(port=8000)