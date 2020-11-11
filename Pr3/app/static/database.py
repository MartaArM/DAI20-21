from flask_sqlalchemy import SQLAlchemy;
from flask import Flask;

app = Flask(__name__);


db_name = 'users.db';
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name;
db = SQLAlchemy(app);

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True;


# Database

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username