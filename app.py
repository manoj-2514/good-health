from flask import Flask, render_template, request
from models import db, HealthRecord

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = int(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    lifestyle = request.form['lifestyle']
    stress = request.form['stress']

    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 2)

    if bmi < 18.5:
        bmi_status = "Underweight"
        color = "blue"
        advice = "Increase calorie intake with nutritious food."
    elif bmi < 25:
        bmi_status = "Normal"
        color = "green"
        advice = "Maintain your healthy routine."
    elif bmi < 30:
        bmi_status = "Overweight"
        color = "orange"
        advice = "Exercise regularly and control diet."
    else:
        bmi_status = "Obese"
        color = "red"
        advice = "Consult a healthcare professional."

    record = HealthRecord(
        name=name,
        age=age,
        height=height,
        weight=weight,
        bmi=bmi,
        bmi_status=bmi_status,
        lifestyle=lifestyle,
        stress=stress
    )

    db.session.add(record)
    db.session.commit()

    return render_template(
        'report.html',
        record=record,
        advice=advice,
        color=color
    )

@app.route('/records')
def records():
    all_records = HealthRecord.query.order_by(HealthRecord.created_at.desc()).all()
    return render_template('records.html', records=all_records)

if __name__ == '__main__':
    app.run(debug=True)
