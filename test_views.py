"""Message View tests."""

# run these tests like:
#
#    FLASK_ENV=production python3 -m unittest test_views.py


import os
import datetime
from unittest import TestCase

from models import db, Doctor, Patient, Medication, Nurse, Medication_Given

os.environ['DATABASE_URL'] = "postgresql:///capstone-one-test"

# Now we can import app


from app import app

# # Create our tables (we do this here, so we only create the tables
# # once for all tests --- in each test, we'll delete the data
# # and create fresh new clean test data

db.create_all()

# # Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False


class ViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        d1 = Doctor(first_name="John",last_name="Fulcan")
        d2 = Doctor(first_name="Mike",last_name="NightRider")
        
        db.session.add(d1)
        db.session.add(d2)
        
        p1 = Patient(first_name="Blub",last_name="Booper",date_of_birth=datetime.date(1999,1,19))
        p2 = Patient(first_name="Jak",last_name="Alomaty",date_of_birth=datetime.date(2001,3,21))

        db.session.add(p1)
        db.session.add(p2)

        n1 = Nurse(first_name='Marko',last_name="jamie")
        n2 = Nurse(first_name='Jimbo',last_name="Kilayin")

        db.session.add(n1)
        db.session.add(n2)

        m1 = Medication(name="hydralazine 50mg",description="blood pressure",doctors_id=1,patients_id=2)    

        db.session.add(m1)

        db.session.commit()

        d1 = Doctor.query.get(1)
        d2 = Doctor.query.get(2)
        p1 = Patient.query.get(1)
        p2 = Patient.query.get(2)

        self.d1 = d1
        self.d2 = d2
        self.p1 = p1
        self.p2 = p2
        self.n1 = n1
        self.n2 = n2

        self.client = app.test_client()

# - - - - - 
# Patient views
# - - - - - 
    def test_patients_show(self):
        with self.client as c:
            resp = c.get('/patients')
            self.assertEqual(resp.status_code, 200)
            
    def test_patients_list(self):
        with self.client as c:
            resp = c.get('/patients/sort/id')
            self.assertEqual(resp.status_code, 200)
            resp = c.get('/patients/sort/date_of_birth')
            self.assertEqual(resp.status_code, 200)
            resp = c.get('/patients/sort/first_name')
            self.assertEqual(resp.status_code, 200)
            resp = c.get('/patients/sort/last_name')
            self.assertEqual(resp.status_code, 200)
    
            
    def test_patient_id_show(self):
        with self.client as c:
            resp = c.get(f'/patients/{self.p1.id}')
            self.assertEqual(resp.status_code, 200)

    def test_invalid_patients_show(self):
        with self.client as c:
            resp = c.get('/patients/55')
            self.assertEqual(resp.status_code, 404)

    def test_add_patient_form(self):
        """Can use add a patient? GET REQUEST """
        with self.client as c:
            resp = c.get("/patients/create")
            html = resp.get_data(as_text=True)
            self.assertIn('<label for="first_name">First Name</label>',html)
            
    def test_add_patient(self):
        """Can use add a patient? POST REQUEST"""
        with self.client as c:
            d = {'fn': "Jack",'ln':"Joonson",'yr':"1990",'day':"31",'month':"10"}
            resp = c.post("/patients/create", data=d)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            
            # self.assertIn('Jack',html)
            # import pdb 
            # pdb.set_trace()

# - - - - - 
# Medication views
# - - - - - 

    def test_medication_emr(self):
        """Emr main page will load"""
        with self.client as c:
            resp = c.get('/medications')
            self.assertEqual(resp.status_code, 200)

    def test_medication_search(self):
        """Emr medication search will load"""
        with self.client as c:
            resp = c.get('/medications/search')
            self.assertEqual(resp.status_code, 200)

    def test_medication_get_current_patient(self):
        """Emr will get current patient page load"""
        with self.client as c:
            resp = c.get('/medications/get-current-patient/1')
            self.assertEqual(resp.status_code, 200)

    def test_medication_get_current_patient_no_given(self):
        """Get given medication, since nothing in list will redirect 302"""
        with self.client as c:
            resp = c.get('/medications/1/patients/1/given')
            self.assertEqual(resp.status_code, 302)

    def test_medication_get_current_patient_given_with_given_get(self):
        """Get given medication, since something in list will return response 200"""
        with self.client as c:
            mg = Medication_Given(nurses_id=1,patients_id=1,medications_id=1,doctors_id=1)
            db.session.add(mg)
            db.session.commit()
            resp = c.get('/medications/1/patients/1/given')
            self.assertEqual(resp.status_code, 200)

    def test_medication_get_current_patient_given_with_given_post(self):
        """Post given medication, since something in list will return response 200"""
        with self.client as c:
            mg = Medication_Given(nurses_id=1,patients_id=1,medications_id=1,doctors_id=1)
            db.session.add(mg)
            db.session.commit()
            resp = c.post('/medications/1/patients/1/given')
            self.assertEqual(resp.status_code, 200)

    def test_medication_add(self):
        """Add medication"""
        with self.client as c:
            resp = c.get('/medications/add')
            self.assertEqual(resp.status_code, 200)

    def test_medication_add(self):
        """Add medication"""
        with self.client as c:
            resp = c.post('/medications/add')
            self.assertEqual(resp.status_code, 200)