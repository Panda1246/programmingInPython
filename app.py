from flask import Flask, render_template, request, redirect,  abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snails.db'
db = SQLAlchemy(app)
atributes = ['sex', 'length', 'diameter', 'rings']


class Abalone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String(1))
    length = db.Column(db.Float)
    diameter = db.Column(db.Float)
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
                abort(400)
            value_of_arg = request.form[i]
            if i == 'sex':
                if value_of_arg not in ['M', 'F', 'I']:
                    pass  # return error wrong value
            elif i == 'rings':
                if not value_of_arg.isdigit():
                    abort(400)
            else:
                try:
                    float(value_of_arg)
                except ValueError:
                    abort(400)
        abalone = Abalone(sex=request.form['sex'], length=request.form['length'], diameter=request.form['diameter'], rings=request.form['rings'])
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
        db.session.delete(Abalone.query.get(id))
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return abort(404)  # return error

@app.errorhandler(400)
def bad_request(error):
    return render_template('400.jinja'), 400
@app.errorhandler(404)
def bad_request(error):
    return render_template('404.jinja'), 404
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.jinja'), 500

if __name__ == '__main__':
    app.run()
