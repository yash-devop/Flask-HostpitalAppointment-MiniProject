from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import os

# app = Flask(_name_)

TEMPLATE_DIR = os.path.abspath('G:/Python project/techtim/templates')
STATIC_DIR = os.path.abspath('G:/Python project/techtim/static')

# app = Flask(_name_) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route("/index", methods=['POST'])
def move_forward():
    return render_template("index.html")          #Moving forward code

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=['POST','GET'])
def book():
    return render_template("book.html")          #Moving forward code

@app.route("/appointment", methods=['POST','GET'])
def appointment():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form.get
        Name = userDetails('full_name')
        Gender = userDetails('radio')
        PhoneNumber = userDetails('phone')
        Dateofbirth = userDetails('dob')
        Department = userDetails('dept')
        FirstVisit = userDetails('visit')
        Appointment_DT = userDetails('appointment_time')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO form(Name, Gender,PhoneNumber,Dateofbirth,Department,FirstVisit,Appointment_DT) VALUES(%s,%s,%s,%s,%s,%s,%s)",(Name, Gender,PhoneNumber,Dateofbirth,Department,FirstVisit,Appointment_DT))
        mysql.connection.commit()
        cur.close()
        return redirect('/medform')
    return render_template("appointment.html")


@app.route('/medform')
def medform():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM form")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('medform.html',userDetails=userDetails)





@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form.get
        Name = userDetails('full_name')
        Gender = userDetails('radio')
        AadharNumber = userDetails('aadhar')
        Address = userDetails('address')
        PhoneNumber = userDetails('phone')
        Pincode = userDetails('pincode')
        Fever = userDetails('fever')
        LossOfSmellandTaste = userDetails('lossofsmelltaste')
        Other = userDetails('other')
        MedicalHistory = userDetails('medical')
        AppointmentDate = userDetails('appointmentdate')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(Name, Gender, AadharNumber, Address, PhoneNumber, Pincode, Fever, LossOfSmellandTaste, Other, MedicalHistory, AppointmentDate) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Name, Gender, AadharNumber, Address, PhoneNumber, Pincode, Fever, LossOfSmellandTaste, Other, MedicalHistory, AppointmentDate))
        mysql.connection.commit()
        cur.close()
        return redirect('/user')
    return render_template("register.html")

@app.route('/user')
def user():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('user.html',userDetails=userDetails)



if __name__ == '_main_':
    app.run(debug=True)