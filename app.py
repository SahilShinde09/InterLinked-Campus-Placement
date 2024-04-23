from flask import Flask, render_template, request, redirect, abort, session, url_for
from models import db, EmployeeModel
from flask_sqlalchemy import SQLAlchemy
# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/campus"


class User(db.Model):
    __tablename__ = "user"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(80) )


from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

# app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.secret_key = "adi"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'campus'

mysql = MySQL(app)


@app.route('/')
def firstpage():
    return render_template('HomePage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM login WHERE username = % s AND password = % s', (username, password ))
        user = cursor.fetchone()
        if user:
            # session['loggedin'] = True
            # session['userid'] = user['userid']
            session['name'] = user['name']
            session['username'] = user['username']
            msg = 'Logged in successfully !'
            return render_template('user.html')
        else:
            msg = 'Please enter correct username / password !'
    return render_template('sign_in.html')
    # return render_template('sign_in.html')


@app.route('/home')
def user_home():
    if (db.select == stud):
        return render_template('student_view_jobs.html')
    elif (db.select == tnp):
        return render_template('tnp_home.html')
    elif (db.select == admin):
        return render_template('admin_home.html')


@app.route('/signup' , methods=['GET', 'POST'] )
def signup():
    if(request.method=='POST'):
        un = request.form.get('username')
        pw = request.form.get('password')
        entry = User(  username = un , password=pw)
        db.session.add(entry)
        db.session.commit()
    return render_template('sign_up.html')


app.run(host='localhost', port=5000)
