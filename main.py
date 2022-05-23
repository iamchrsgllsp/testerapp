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
    return "Thanks"
  else:
    return render_template('registration.html')

@app.route('/signupperks')
def perks():
  return "Our perks our currently being finalised"

@app.route('/privacy-policy')
def privacy():
  return "Our policy is currently being finalised"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)