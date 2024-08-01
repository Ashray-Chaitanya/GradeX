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

def get_data():
    cur = mysql.connection.cursor()
    cur.execute('select * from student_marks')
    info = []
    data = cur.fetchall()
    info.append([data])
    column_names = [desc[0] for desc in cur.description]
    info.append(column_names)
    cur.close()
    return info

def get_max_marks(index):
    cur = mysql.connection.cursor()
    cur.execute(f'select * from student_marks where {index} = (SELECT MAX({index}) FROM student_marks)')
    data = cur.fetchall()
    return data

def get_failed(index):
    cur = mysql.connection.cursor()
    cur.execute(f'select count(*) as failed from student_marks where {index} < 60')
    data = cur.fetchall()
    print(data[0][0])
    return data[0]

def process_chart(data,index):
    labels = []
    values = []
    for row in data[0][0]:
        labels.append(row[0])  # Assuming first column is label    
        values.append(row[index])  # Assuming second column is value
    return [{
        'labels': labels,
        'datasets': [{
            'label': data[1][index],
            'data': values,
            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
            'borderColor': 'rgba(255, 99, 132, 1)',
            'borderWidth': 1
        }]
    }]

def get_subcode(index):
    if index == 0:
        return 'BCS301'
    elif index == 1:
        return "BCS302"
    elif index == 2:
        return "BCS303"
    elif index == 3:
        return "BCS304"
    elif index == 4:
        return "BCSL305"
    elif index == 5:
        return "BCS307"
    elif index == 6:
        return "BPEK359"
    elif index == 7:
        return "BCS358D"
    

@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")

@app.route("/about-us", methods=["GET"])
def about():
    return render_template("aboutUs.html")

@app.route("/prof", methods=["GET"])
def prof():
    return render_template("prof.html")

@app.route("/tt", methods=["GET"])
def tt():
    return render_template("tt.html")


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

@app.route('/max/<int:index>',methods=["GET"])
def max(index):
    data = get_data()
    sub_code = get_subcode(index)
    max_marks = get_max_marks(sub_code)
    failed = get_failed(sub_code)
    chart = []
    for i in range(1,6):
        chart.append(process_chart(data,i))
    return render_template('max.html', charts=chart,index=index,max_marks=max_marks[0], sub_code=sub_code, failed=failed[0])


@app.route('/stats/<int:index>', methods=["GET"])
def dashboard(index):
    data = get_data()
    sub_code = get_subcode(index)
    max_marks = get_max_marks(sub_code)
    failed = get_failed(sub_code)
    chart = []
    for i in range(1,6):
        chart.append(process_chart(data,i))
    return render_template('stats.html', charts=chart,index=index,max_marks=max_marks[0], sub_code=sub_code, failed=failed[0])
                           


@app.route('/stats',methods=["GET"])
def stat():
    index=0
    return render_template('stat_nav.html')



webbrowser.open("http://127.0.0.1:8000")
app.run(port=8000, debug=True)




