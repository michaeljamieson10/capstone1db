# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_models.py


import os
import datetime
from unittest import TestCase

from models import db, Doctor, Patient, Medication, Nurse, Medication_Given

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///capstone-one-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False

class UserModelTestCase(TestCase):
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

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res


    def test_doctor_model(self):
        """Does basic model work?"""
        d = Doctor(
            first_name="John",
            last_name="Fulcan",
            office_phone="555-5555"
        )
        db.session.add(d)
        db.session.commit()

        """Doctor should have no patients & no medications"""
        self.assertEqual(len(d.medications), 0)
        self.assertEqual(len(d.medications_given), 0)

    def test_patient_model(self):
        """Does basic model work?"""
        p = Patient(
            first_name="Nonkoff",
            last_name="Jegrold",
            date_of_birth=datetime.date(1999,1,19)
        )
        db.session.add(p)
        db.session.commit()

        """Doctor should have no patients & no medications"""
        self.assertEqual(len(p.medications), 0)
        self.assertEqual(len(p.medications_given), 0)

    def test_nurse_model(self):
        """Does basic model work?"""
        n = Nurse(
            first_name="Mikey",
            last_name="Jamie"
        )
        db.session.add(n)
        db.session.commit()

        """Nurse should no medications given"""
        self.assertEqual(len(n.medications_given), 0)

    ####
    #
    # Medication add to patient tests
    #
    ####

    def test_medication(self):
        """Test Patient Medication"""
        self.assertEqual(len(self.p1.medications),0)

        m1 = Medication(name="Plaquenil",doctors_id=1,patients_id=1,description="U07.1 - COVID-19")

        db.session.add(m1)
        db.session.commit()

        self.assertEqual(len(self.p1.medications),1)
        self.assertEqual(len(self.p2.medications), 0)

        self.assertEqual(self.p1.medications[0].id, m1.id)

    def test_medication_given(self):
        m1 = Medication(name="Plaquenil",doctors_id=1,patients_id=1,description="U07.1 - COVID-19")
        db.session.add(m1)
        db.session.commit()
        mg = Medication_Given(nurses_id=1,doctors_id=1,patients_id=1, medications_id=1)
        db.session.add(mg)
        db.session.commit()
        self.assertEqual(len(self.p1.medications_given),1)
        self.assertEqual(len(self.p2.medications_given),0)
        self.assertEqual(len(self.d1.medications_given),1)
        self.assertEqual(len(self.d2.medications_given),0)
        self.assertEqual(len(self.n1.medications_given),1)
        self.assertEqual(len(self.n2.medications_given),0)

