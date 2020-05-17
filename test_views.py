"""Message View tests."""

# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_views.py


import os
import datetime
from unittest import TestCase

from models import db, Doctor, Patient, Medication, Nurse, Medication_Given


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
            
    def test_patient_show(self):
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
            
# This test is currently not working
    def test_add_patient(self):
        """Can use add a patient? POST REQUEST"""
        with self.client as c:
            d = {'fn': "Jack",'ln':"Joonson",'yr':"1990",'day':"31",'month':"10"}
            resp = c.post("/patients/create", data=d)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 302)
            # self.assertIn('Jack',html)
            # pt = Patient.query.get(3)
            # import pdb 
            # pdb.set_trace()
            # self.assertEqual(pt.text, "Jack")

# - - - - - 
# Medication views
# - - - - - 

    def test_medication_emr(self):
        """Emr main page will load"""
        with self.client as c:
            resp = c.get('/medications')
            self.assertEqual(resp.status_code, 200)

