from flask import Flask, render_template, request
from app import users,database
from datetime import datetime

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def home():
  if request.method == "POST":
    account = request.form['account']
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    gender = request.form['gender']
    users.register(account,email,name,password,gender)
    return f"Thanks for signing up, email with details has been sent to {email}<br><a href='/'>Go home</a>"
  else:
    return render_template('registration.html')

@app.route('/api/createnote',methods=["GET","POST"])
def note():
    if "DART" not in request.headers:
      #This is for web-based
      if request.method == "POST":
        post = {'user':"cgill033",'datePosted':datetime.now(),'note':request.form['note'],"tags":request.form['tags'].replace(" ", "")}
        posted = database.createPost(post)
        return posted
      else:
        return render_template('note.html')
    else:
      #This is for Flutter app
      return {"data":"App based"}
    
  

@app.route('/signupperks')
def perks():
  return "Our perks our currently being finalised"

@app.route('/privacy-policy')
def privacy():
  return "Our policy is currently being finalised"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)