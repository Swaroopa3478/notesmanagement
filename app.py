from flask import Flask,render_template,redirect,request,flash
from flask_mysqldb import MySQL
import mysql.connector
from flask import session
app = Flask(__name__)
app.config['SESSION_TYPE']='filesystem'
app.config['SECRET_KEY']='ists-flask_short@terminternship12345'
mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='ists')

#link rel="stylesheet"type="text/css"href="{{url_for('static',filename='style.css)}}">
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/registration",methods=['GET','POST'])
def register():
 if request.method=='POST':
   name = request.form['name']
   ph_number = request.form['phone_number']
   email = request.form['email']
   password = request.form['password']
   cursor = mydb.cursor(bufffered=True)
   cursor.execute("INSERT INTO registration(name,ph_number,email,password)VALUES(%s,%s,%s,%s)",(name,ph_number,email,password))
   mydb.commit()
   cursor.close()
   flash("your account is created")
   return  redirect(url_for('home'))
   

 else:
    return render_template("registration.html")
 @app.route('/login',methods=['GET','POST'])
 def login():
  if request.method=="POST":
   email = request.form['email']
 password = request.form['password']
cursor = mydb.cursor(buffered=True)
cursor.execute('select count(*) from registration where email=%s and password=%s',[email,password])
count = cursor.fetchone()[0]
cursor.close()
if count==1:
  session['email'] =email
  flash("sucessfully login")
  return redirect(url_for('home'))
else:
  flash('invalid crenditials')
  return  redirect(url_for('home'))
return  render_template("login.html")

@app.route('/logout')
def logout():
  if session.get('email'):
   session.pop('email')
   flash("sucessfully loged out")
   return  render_template("login.html")
#----------------------------notes management - crud operations
#-------To create notes
@app.route('/createnotes',methods=['GET','POST'])
def createnotes():
 if session.get('email'):
  if request.method=="POST":
   email = session['email']
   title = request.form['title']
   notes = request.form['notes']
   cursor = mydb.cursor(buffered=True)
   cursor.execute('insert into notes(email,title,notes) values (%s,%s,%s)',[email,title,notes])
   mydb.commit()
   cursor.close()
   flash('notes creted sucessfully')
   return render_template('cretenotes.html')
  else:
    return render_template('login.html')


  










  app.run(use_reloader=True,debug=True)









 