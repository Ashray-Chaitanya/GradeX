from flask import Flask, render_template, request,jsonify
from flask_mysqldb import MySQL
import webbrowser

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Jett@h1k0"
app.config["MYSQL_DB"] = "new_schema"
leftmymark = "Shreyas"
mysql = MySQL(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")


@app.route("/about-us", methods=["GET"])
def about():
    return render_template("aboutUs.html")


@app.route("/home", methods=["GET", "POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    cursor = mysql.connection.cursor()
    try:
        cursor.execute(
            f"select USERNAME from credentials where USERNAME = '{username}'"
        )
        if cursor.fetchone() == None:
            raise Exception
        else:
            cursor.execute(
                f"select PASS from credentials where USERNAME = '{username}'"
            )
            latest_entry = cursor.fetchone()
            if latest_entry[0] == password:
                print("success")
            else:
                raise Exception
    except Exception:
        return "WRONG INFO"
    mysql.connection.commit()
    cursor.close()
    return render_template("index.html")


@app.route("/login-complete", methods=["POST", "GET"])
def login_complete():
    if request.method == "GET":
        return "Login via the login Form"

    if request.method == "POST":
        try:
            data = request.get_json()
            usn = data['USN'].lower()
            cursor = mysql.connection.cursor()
            cursor.execute(f"SELECT * FROM {usn}")
            data = cursor.fetchall()
            cursor.close()


            return jsonify(success=True, students=data)
        except Exception as e:
            return jsonify(success=False, error=str(e))


@app.route("/calc", methods=["GET"])
def calc():
    return render_template("calci.html")


webbrowser.open("http://127.0.0.1:8000")
app.run(port=8000)
