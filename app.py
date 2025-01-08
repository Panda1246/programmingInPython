from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snails.db'
db = SQLAlchemy(app)
atributes = ['sex', 'length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight',
             'rings']


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


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        for i in atributes:  # value veryfication
            if i not in request.form:
                pass  # return error missing value
            value_of_arg = request.form[i]
            if i == 'sex':
                if value_of_arg not in ['M', 'F', 'I']:
                    pass  # return error wrong value
            elif i == 'rings':
                if not value_of_arg.isdigit():
                    pass
            else:
                try:
                    float(value_of_arg)
                except ValueError:
                    pass
        abalone = Abalone(sex=request.form['sex'], length=request.form['length'], diameter=request.form['diameter'], height=request.form['height'],
                          whole_weight=request.form['whole_weight'], shucked_weight=request.form['shucked_weight'], viscera_weight=request.form['viscera_weight'],
                          shell_weight=request.form['shell_weight'], rings=request.form['rings'])
        try:
            db.session.add(abalone)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Database connection failed: {str(e)}" #return error
    else:
        return render_template('add.jinja')
@app.route('/delete/<int:id>')
def delete(id):
    try:
        db.session.delete(Abalone.query.get_or_404(id))
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"Database connection failed: {str(e)}"  # return error


if __name__ == '__main__':
    app.run()
