from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Jett@h1k0'
app.config['MYSQL_DB'] = 'new_schema'
mysql = MySQL(app)

@app.route("/", methods=["GET"])
def home():
  return render_template("index.html")

@app.route("/login", methods=["GET"])
def login():
  return render_template("login.html")

 
@app.route('/login-complete', methods = ['POST', 'GET'])
def login_complete():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        usn = (request.form['USN']).lower()
        print (usn)
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM {usn}")
        mysql.connection.commit()
        data =cursor.fetchall()
        print(data)
        cursor.close()
        return render_template('index.html',students=data)
    
app.run(port=8000)