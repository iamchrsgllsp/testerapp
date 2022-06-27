from flask import Flask, render_template, request
from app import users

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

@app.route('/note',methods=["GET","POST"])
def note():
    if request.method == "POST":
      print(request.form['description'])
      with open("note.txt","w") as note:
        note.write(request.form['description'])
      return "note"
    else:
      return render_template('note.html')
  

@app.route('/signupperks')
def perks():
  return "Our perks our currently being finalised"

@app.route('/privacy-policy')
def privacy():
  return "Our policy is currently being finalised"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)