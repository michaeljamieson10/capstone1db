from flask import Flask, render_template, request, redirect, jsonify, make_response, session
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
app.config["SECRET_KEY"] = "SSHH SECRETO"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///capstone_one_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()


@app.route("/", methods=["GET", "POST"])
def homepage():
    """Show homepage."""
    # # url = "https://www.googleapis.com/calendar/v3/users/me/calendarList"
    # # res = requests.get(url)
    # scopes = ['https://www.googleapis.com/auth/calendar']
    # flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    # credentials = flow.run_console()
    # pickle.dump(credentials, open("token.pkl", "wb"))
    # # raise
    # credentials = pickle.load(open("token.pkl", 'rb'))
    # service = build("calendar", "v3", credentials=credentials)
    # result = service.calendarList().list().execute()
    # calendar_id = result['items'][1]['id']
    # result2 = service.events().list(calendarId=)
    # result2 = service.events().list(calendarId='michaeljamieson10@gmail.com').execute()
    # start_time = datetime.datetime(2020, 5, 12, 19, 30, 0)
    # end_time = start_time + timedelta(hours=4)
    # timezone = "US/Eastern"
    # Refer to the Python quickstart on how to setup the environment:
    # https://developers.google.com/calendar/quickstart/python
    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
    # stored credentials.

    # event = {
    # 'summary': 'Do springboard software capstone',
    # 'location': '2 Toni Place Central Islip',
    # 'description': 'A chance to hear more about Google\'s developer products.',
    # 'start': {
    #     'dateTime': start_time.strftime('%Y-%m-%dT%H:%M:%S'),
    #     'timeZone': timezone,
    # },
    # 'end': {
    #     'dateTime': end_time.strftime('%Y-%m-%dT%H:%M:%S'),
    #     'timeZone': timezone,
    # },
  
    # 'reminders': {
    #     'useDefault': False,
    #     'overrides': [
    #     {'method': 'email', 'minutes': 24 * 60},
    #     {'method': 'popup', 'minutes': 10},
    #     ],
    # },
    # }

    
    # print 'Event created: %s' % (event.get('htmlLink'))

    return render_template("index.html")

@app.route("/authorize", methods=["GET", "POST"])
def authorize():
    """Show homepage."""
    # url = "https://www.googleapis.com/calendar/v3/users/me/calendarList"
    # res = requests.get(url)
    scopes = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    credentials = flow.run_console()
    pickle.dump(credentials, open("token.pkl", "wb"))
    # raise
    return render_template("index.html")

@app.route("/token", methods=["GET", "POST"])
def token_page():
    """Show homepage."""
    # Ensure that the request is not a forgery and that the user sending
    # this connect request is the expected user.
    if request.args.get('state', '') != session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # url = 'https://oauth2.googleapis.com/token'   
    
    response = requests.post('https://oauth2.googleapis.com/token', data={
        'code': request.args.get('code'),
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://127.0.0.1:5000/token',
        'client_id': '.apps.googleusercontent.com',
        'client_secret': '',
    }) 
    response.raise_for_status()
    data = response.json()
    # Save these in your database associated with the user
    session['access_token'] =  data['access_token']
    session['refresh_token'] =  data['refresh_token']
    raise
    return redirect("/")

@app.route("/authorized", methods=["GET", "POST"])
def authorized():
    """Show login page."""
    CLIENT_ID = 'apps.googleusercontent.com'
    
    state = hashlib.sha256(os.urandom(1024)).hexdigest()
    session['state'] = state
    # Set the client ID, token state, and application name in the HTML while
    # serving it.
    response = make_response(
        render_template('index.html',
                        CLIENT_ID=CLIENT_ID,
                        STATE=state,
                        APPLICATION_NAME='Capstone1'))

    uri = 'https://accounts.google.com/o/oauth2/v2/auth?'
    redirect_uri = 'http://127.0.0.1:5000/token'
    lala = 'https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id='
    
    response_two = requests.get(f"{uri}response_type=code&client_id={CLIENT_ID}&scope=openid%email&redirect_uri={redirect_uri}&state={state}")

    return redirect(f"{uri}response_type=code&client_id={CLIENT_ID}&scope=openid%20profile%20email&redirect_uri={redirect_uri}&state={state}")

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

@app.route("/medications-add", methods=['POST','GET'])
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
        m = Medication(name=request.args['rxterms'],description=request.args['diagnosis'],patients_id=patient,doctors_id=doctor)
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
    medication_list = [m for m in ml]
    # medication_list = [m.as_dict() for m in ml]
    # medication_list = json.dumps(ml_one, default = myconverter)
    # medication_list = (ml_one, default = myconverter)
    #    player.update({'weightKilograms': '111.1'})
    # [m.update({'date_prescribed': m['date_prescribed'].strftime("%m/%d/%Y, %H:%M:%S")}) for m in medication_list]
    # [m['date_prescribed'] = m['date_prescribed'].strftime("%m/%d/%Y, %H:%M:%S") for m in ml_one]

    # raise
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

    