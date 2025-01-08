from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snails.db'
db = SQLAlchemy(app)

class Abalone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String(1))
    length = db.Column(db.Float)
    diameter = db.Column(db.Float)
    height = db.Column(db.Float)
    whole_weight = db.Column(db.Float)
    shucked_weight = db.Column(db.Float)
    viscera_weight = db.Column(db.Float)
    shell_weight = db.Column(db.Float)
    rings = db.Column(db.Integer)

with app.app_context():
    db.create_all()
@app.route('/')
def hello_world():
    all = Abalone.query.all()
    return render_template('index.jinja', rows=all)

@app.route('/add', methods=['POST'])
def add():



if __name__ == '__main__':
    app.run()
