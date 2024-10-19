from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://vinay:dbmsproject469539@host/db_project')
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SQLAlchemy()

class User(db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# db.init_app(app)





# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), nullable=False)
#     email = db.Column(db.String(128), unique=True, nullable=False)
#     password = db.Column(db.String(128), nullable=False)
#     role = db.Column(db.Enum('manager', 'team member', 'admin'), nullable=False)


# class Project(db.Model):
#     __tablename__ = 'projects'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(128), nullable=False)
#     description = db.Column(db.Text)
#     deadline = db.Column(db.Date)
#     manager_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     manager = db.relationship('User', backref='projects')


# class Task(db.Model):
#     __tablename__ = 'tasks'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(128), nullable=False)
#     description = db.Column(db.Text)
#     priority = db.Column(db.Integer)
#     status = db.Column(db.Enum('pending', 'in progress', 'completed'), nullable=False)
#     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
#     project = db.relationship('Project', backref='tasks')
#     assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))
#     assigned_user = db.relationship('User', backref='assigned_tasks')


# class Team(db.Model):
#     __tablename__ = 'teams'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), nullable=False)
#     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
#     project = db.relationship('Project', backref='teams')


# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.Text, nullable=False)
#     task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
#     task = db.relationship('Task', backref='comments')
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship('User', backref='comments')
#     timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
