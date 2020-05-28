from flask import Flask, render_template, request, redirect, jsonify, make_response, session, flash
from models import db, connect_db, Medication, Doctor, Patient, Medication_Given, Nurse
from forms import NewMedicationPatientForm, NewPatientForm
from datetime import date, datetime, timedelta
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow 
import datetime
import requests
import json
import pickle
import hashlib
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///capstone_one_db')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'shh')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()


@app.route("/", methods=["GET", "POST"])
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route("/doctor")
def list_doctor():
    """Will list doctors"""
    d = Doctor.query.all()
    
    return render_template('doctor/list.html',doctors=d)

# ------------------------
# Medication routes
# ------------------------

@app.route("/medications")
def list_medications():
    """Will list medications with patients in side bar menu"""
    patients = Patient.query.all()
    return render_template("medications.html",patients=patients)

@app.route("/medications/get-current-patient/<int:patient_id>")
def get_patient_medications(patient_id):
    """Get current patient medications.
     THIS ROUTE IS SPECIFIC FOR AJAX AXIOS REQUEST getPatientId 
        LOCATED IN API-classes
    """
    p = Patient.query.get(patient_id)
    ml = Medication.query.filter_by(patients_id=patient_id)
    ml_one = [m.as_dict() for m in ml]
    
    return json.dumps(ml_one, default = myconverter)

@app.route("/medications/<int:medication_id>/patients/<int:patient_id>/given",methods=['GET'])
def medications_given_get(medication_id,patient_id):
    """Will get given medications from database"""
    
    mgl = Medication_Given.query.filter_by(medications_id=medication_id,patients_id=patient_id).all()
    # raise
    if len(mgl) == 0 :
        flash("Medication was never given",'error')
        return redirect('/medications')
    return render_template('patient/medication_history.html', mgl=mgl)

@app.route("/medications/<int:medication_id>/patients/<int:patient_id>/given",methods=['POST'])
def medications_given_create(medication_id,patient_id):
    """Will add medication to given medications from database"""
    mg = Medication_Given(nurses_id=1,patients_id=patient_id,medications_id=medication_id,doctors_id=1)
    db.session.add(mg)
    db.session.commit()
    # flash("Medication was given",'success')
    return mg.date_given.strftime("%m/%d/%Y, %H:%M:%S")
    # return json.dumps(ml_one, default = myconverter)
    
@app.route("/medications/search")
def search_medications():
    """Will list all medications from api"""
    
   
    return render_template("medication/search.html")

@app.route("/medications/add", methods=['POST','GET'])
def add_to_db_list_medications():
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
        m = Medication(name=request.args.get('rxterms','None'),description=request.args.get('diagnosis','None'),patients_id=patient,doctors_id=doctor)
        db.session.add(m)
        db.session.commit()
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

# ~~
# Patient List functionality
# ~~

@app.route("/patients/sort/<header>")
def sort_header_patients(header):
    """Will sort patients by first name then list patients in a json object"""
    patients = Patient.query.order_by(header)
    patient_list = [p.as_dict() for p in patients]
    return jsonify(patient_list)

@app.route("/patients/<patient_id>")
def list_patient(patient_id):
    """Will list patient and his/her medication with other dat such as molst form"""
    patient = Patient.query.get_or_404(patient_id)
    
    ml = Medication.query.filter_by(patients_id=patient_id)
    medication_list = [m for m in ml]

    return render_template('patient/detail.html', patient=patient, medication_list=medication_list)

@app.route("/patients/create", methods=["GET","POST"])
def create_pt():
    """Will create patients """
    form = NewPatientForm()
    if form.validate_on_submit():
        fn = form.first_name.data
        ln = form.last_name.data
        yr = form.year.data
        day = form.day.data
        month = form.month.data
        photo = form.photo.data
        date = datetime.date(yr, month, day)
        p = Patient(first_name=fn,last_name=ln, date_of_birth=date, patient_photo=photo)
        db.session.add(p)
        db.session.commit()
        return redirect("/medications/search")
    else:
        return render_template("patient/create.html", form=form)

    