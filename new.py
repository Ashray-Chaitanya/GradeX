from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "new_schema"

mysql = MySQL(app)


@app.route("/")
def form():
    return render_template("sample.html")


@app.route("/ufdate")
def login():
    username = request.form["username"]
    password = request.form["password"]
    cursor = mysql.connection.cursor()
    try:

        cursor.execute(f"select USERNAME from credentials where USERNAME = {username} ")
        cursor.execute(f"select PASS from credentials where USERNAME = {username} ")
        latest_entry = cursor.fetchone()
        if latest_entry == password:
            print("success")
    except Exception:
        print("Username doesnt exist")

    mysql.connection.commit()
    cursor.close()
    return f"Done!!"


