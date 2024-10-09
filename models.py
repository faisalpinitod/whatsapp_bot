from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'
