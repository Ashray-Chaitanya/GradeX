
from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Jett@h1k0'
app.config['MYSQL_DB'] = 'new_schema'
mysql = MySQL(app)

@app.route('/login-complete', methods = ['POST', 'GET'])
def login_complete():
    for i in range (1,71):
        cursor = mysql.connection.cursor()
        d = cursor.execute(f"Create table Student_details 1bi22is{i} WHERE total < 30;")
        mysql.connection.commit()

    cursor.close()

app.run(port=8000)