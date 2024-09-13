from flask import Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Jett@h1k0'
app.config['MYSQL_DB'] = 'new_schema'
 
mysql = MySQL(app)
 
@app.route('/')
def form():
    return render_template('sample.html')

@app.route('/ufdate')
def login():
        cursor = mysql.connection.cursor()
        for i in range(1,71):
            cursor.execute(f"INSERT INTO namelist (Name,USN) VALUES ('1bi22is{i}','user{i}','bit{i}');")
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(host='localhost', port=5000)