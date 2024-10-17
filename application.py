from flask import Flask, render_template, flash
from models import User, Project, Task, Team, Comment
from webforms import LoginForm, SignupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dbmsproject469539'

# Home page - Index
@app.route("/")
def index():
    return render_template('index.html')



@app.route("/login")

def login():
    form = LoginForm()
    return render_template("login.html", 
                           form=form)

@app.route("/signup")

def signup():
    form = SignupForm()
    return render_template("signup.html",
                           form=form)


# Auto Server running
if __name__ == '__main__':
    app.run(debug=True)