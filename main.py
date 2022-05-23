from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('registration.html')

@app.route('/signupperks')
def perks():
  return "Our perks our currently being finalised"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)