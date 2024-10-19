from flask import Flask, render_template, flash, redirect, url_for
from models import db, User
from webforms import LoginForm, SignupForm

app = Flask(__name__)

# Consider storing configuration details in a separate file (config.py)
app.config['SECRET_KEY'] = 'dbmsproject469539'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vinay:dbmsproject469539@host/db_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Home page - Index
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])

def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/signup", methods=["GET", "POST"])

def signup():
    form = SignupForm()
    
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        existing_email = User.query.filter_by(email=form.email.data).first()
        
        if existing_user:
            flash('Username already exists!')
        elif existing_email:
            flash('Email already exists!')
        else:
            user = User()
            user.username = form.username.data
            user.email = form.email.data
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            flash('Signup successful! Please login.')
            return redirect(url_for('login'))
    
    return render_template('signup.html', form=form)

# Auto Server running
if __name__ == '__main__':
    app.run(debug=True)










# from flask import Flask, render_template, flash, redirect, url_for
# from models import User, Project, Task, Team, Comment
# from webforms import LoginForm, SignupForm
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'dbmsproject469539'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vinay:dbmsproject469539@host/user'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # Recommended for performance

# db = SQLAlchemy(app)

# # Home page - Index
# @app.route("/")
# def index():
#     return render_template('index.html')



# @app.route("/login", methods=["GET", "POST"])

# def login():
#     form = LoginForm()
#     return render_template("login.html", 
#                            form=form)

# @app.route("/signup", methods=["GET", "POST"])

# def signup():
#     form = SignupForm()
    
#     if form.validate_on_submit():
#         existing_user = User.query.filter_by(username=form.username.data).first()
#         existing_email = User.query.filter_by(email=form.email.data).first()
        
#         if existing_user:
#             flash('Username already exists!')
#         elif existing_email:
#             flash('Email already exists!')
#         else:
#             user = User()
#             user.username = form.username.data
#             user.email = form.email.data
#             user.set_password(form.password.data)
#             db.session.add(user)
#             db.session.commit()

#             flash('Signup successful! Please login.')
#             return redirect(url_for('login'))
        
#     return render_template('signup.html', form=form)
#     # form = SignupForm()
#     # return render_template("signup.html",
#     #                        form=form)


# # Auto Server running
# if __name__ == '__main__':
#     app.run(debug=True)