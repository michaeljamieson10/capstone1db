from flask import Flask, render_template, request, redirect, jsonify, make_response, session
from models import db, connect_db, Medication, Doctor, Patient
from forms import NewMedicationPatientForm, NewPatientForm
from datetime import date
import datetime
import requests
import json
app = Flask(__name__)
app.config["SECRET_KEY"] = "SSHH SECRETO"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///capstone_one_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

def header_create():
    access_token = session['access_token']
    headers={
    'Authorization':'Bearer %s' %access_token,
    'Content-type':"application/json"
    }
    return headers

def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()


@app.route("/", methods=["GET", "POST"])
def homepage():
    """Show homepage."""
    
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def loginpage():
    """Show homepage."""
    
    return render_template("login.html")

@app.route("/authorized", methods=["POST"])
def authorization():
    """Show homepage."""
    redirect_uri = 'http://127.0.0.1:5000/token'
    client_id = 'IvnxhWMo16B9BQBVs89XfvEWYgDrPch5ZGnwCBvK'
    url = f"https://drchrono.com/o/authorize/?redirect_uri={redirect_uri}&response_type=code&client_id={client_id}"
    res = requests.get(url)
    return redirect(url)

@app.route("/token", methods=["GET", "POST"])
def token():
    """redirec to token page."""

    response = requests.post('https://drchrono.com/o/token/', data={
        'code': request.args.get('code'),
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://127.0.0.1:5000/token',
        'client_id': 'IvnxhWMo16B9BQBVs89XfvEWYgDrPch5ZGnwCBvK',
        'client_secret': 'BHHd5xFV1arUnXykMl5CRiSKu8q6GFNCEcgKVyYMZktalOo2VE3dZlG8z94QJoaUT9RuMCf8OWehrKz0Vj4ShrXLmA6GHCBwGUJdqP0dUiJbf9xKhAVwuDEltTz4n3qw',
    })
    response.raise_for_status()
    data = response.json()
    # Save these in your database associated with the user
    session['access_token'] =  data['access_token']
    session['refresh_token'] =  data['refresh_token']
    return redirect("/")

@app.route("/doctor")
def list_doctor():
    """Will list doctors"""
    d = Doctor.query.all()
    
    return redirect('/')

# ------------------------
# Medication routes
# ------------------------

@app.route("/medications")
def list_medications():
    """Will list medications with patients in side bar menu"""
    patients = Patient.query.all()
    return render_template("medications.html",patients=patients, access_token=session['access_token'])

@app.route("/medications/get-current-patient/<int:patient_id>")
def get_patient_medications(patient_id):
    """Get current patient medications"""
    p = Patient.query.get(patient_id)
    ml = Medication.query.filter_by(patients_id=patient_id)
    ml_one = [m.as_dict() for m in ml]
    
    return json.dumps(ml_one, default = myconverter)
    
@app.route("/medications-search")
def search_medications():
    """Will list all medications from the rxnav database"""
    """ajax axios page"""
    
    return render_template("medication/search.html")

@app.route("/medications-add/<medication_name>", methods=['POST','GET'])
def add_to_db_list_medications(medication_name):
    """Will create a form  medications with patients in side bar menu"""
    
    form = NewMedicationPatientForm()
    patients = Patient.query.all()
    pl = [(patient.id ,patient.first_name + " " + patient.last_name +  " " + patient.date_of_birth.strftime('%Y-%m-%d')) for patient in patients]
    form.patient.choices = pl 
    d = Doctor.query.all()
    dl = [(doctor.id, doctor.last_name + " " + doctor.first_name)for doctor in d]
    form.doctor.choices = dl
    if form.validate_on_submit():
        patient = form.patient.data
        doctor = form.doctor.data
        description = form.description.data
        m = Medication(name=medication_name,description=description,patients_id=patient,doctors_id=doctor)
        db.session.add(m)
        db.session.commit()
        # raise
        return redirect("/medications")

    return render_template("medication/create.html", form=form)

# ------------------------
# Patient routes
# ------------------------

@app.route("/patients")
def list_patients():
    """Will list patients"""
    patients = Patient.query.all()
    return render_template("patient/list.html", patients=patients)


@app.route("/patients/<patient_id>")
def list_patient(patient_id):
    """Will list patient and his/her medication with other dat such as molst form"""
    patient = Patient.query.get(patient_id)
    ml = Medication.query.filter_by(patients_id=patient_id)
    ml_one = [m.as_dict() for m in ml]
    medication_list = json.dumps(ml_one, default = myconverter)
    return render_template('patient/detail.html', patient=patient, medication_list=medication_list)

@app.route("/patient_create", methods=["GET","POST"])
def create_pt():
    """Will create patients """
    form = NewPatientForm()
    if form.validate_on_submit():
        fn = form.first_name.data
        ln = form.last_name.data
        em = form.email.data
        eth = form.ethnicity.data
        gen = form.gender.data
        yr = form.year.data
        day = form.day.data
        month = form.month.data
        date = datetime.date(yr, month, day)
        p = Patient(first_name=fn,last_name=ln, email=em,ethnicity=eth,gender=gen, date_of_birth=date)
        db.session.add(p)
        db.session.commit()
        raise
        return redirect("/patients")
    else:
        return render_template("patient/create.html", form=form)

    