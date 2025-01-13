from flask import Flask, render_template, request, redirect,  abort, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snails.db'
db = SQLAlchemy(app)
ATTRIBUTES = ['sex', 'length', 'diameter', 'rings']


class Abalone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.String(1))
    length = db.Column(db.Float)
    diameter = db.Column(db.Float)
    rings = db.Column(db.Integer)

def validate_abalon(sex, length, diameter, rings):
    if sex not in ['M', 'F', 'I'] and float(length) < 0 and float(diameter) < 0 and float(rings) < 0:
        return False
    return True



with app.app_context():
    db.create_all()


@app.route('/')
def all_data():
    abalones = Abalone.query.all()
    return render_template('index.jinja', rows=abalones)


@app.route('/add', methods=['POST', 'GET'])
def add():
    atributes = {}
    if request.method == 'POST':
        for i in ATTRIBUTES:
            if i not in request.form:
                abort(400)
            value_of_arg = request.form[i]
            if i == 'rings':
                if not value_of_arg.isdigit():
                    abort(400)
            else:
                if not value_of_arg.isdigit:
                    abort(400)

            atributes[i] = value_of_arg
        if not validate_abalon(**atributes):
            abort(400)
        else:
            abalone = Abalone(sex=request.form['sex'], length=request.form['length'], diameter=request.form['diameter'], rings=request.form['rings'])
            try:
                db.session.add(abalone)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                abort(500)
    else:
        return render_template('add.jinja')
@app.route('/delete/<int:id>')
def delete(id):
    try:
        db.session.delete(Abalone.query.get(id))
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return abort(404)

@app.route('/api/data', methods=['GET'])
def get_all_data():
    abalones = Abalone.query.all()

    result_json =[]
    for abalone in abalones:
        result_json.append({
            'id': abalone.id,
            'sex': abalone.sex,
            'length': abalone.length,
            'diameter': abalone.diameter,
            'rings': abalone.rings
        })
    return jsonify(result_json)

@app.route('/api/data', methods=['POST'])
def add_new_data():
    form = request.json
    sex = form['sex']
    length = form['length']
    diameter = form['diameter']
    rings = form['rings']
    if validate_abalon(sex, length, diameter, rings):
        abalon = Abalone(sex, length, diameter, rings)
        db.session.add(abalon)
        db.session.commit()
        response = {
            'messege': 'Record added',
            'id': abalon.id
        }
        return jsonify(response)
    else:
        return jsonify({'messege': 'Invalid data'}), 400

@app.route('/api/data/<int:id>', methods=['DELETE'])
def delete_data(record_id):
    abalone = Abalone.query.get(record_id)
    if abalone:
        db.session.delete(abalone)
        db.session.commit()
        return jsonify({'messege': 'Record deleted'})
    else:
        return jsonify({'messege': 'Record not found'}), 404





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
