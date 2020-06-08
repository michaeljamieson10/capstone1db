"""Models for capstone1 app"""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Doctor(db.Model):
    """Doctor"""
    __tablename__ = "doctors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    office_phone = db.Column(db.Text, nullable=True, default=None)
    medications = db.relationship('Medication', backref='doctor')
    medications_given = db.relationship('Medication_Given', backref='doctor')
    patients =  db.relationship('Patient', secondary='medications', backref='doctor')

class Patient(db.Model):
    """patient"""
    __tablename__ = "patients"
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
      
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    date_of_birth = db.Column(db.DateTime)
    patient_photo = db.Column(db.Text, nullable=True, default="/images/silhouette.jpeg")
    medications = db.relationship('Medication', backref='patient')
    medications_given = db.relationship('Medication_Given', backref='patient')

class Nurse(db.Model):
    """Nurse """
    __tablename__ = "nurses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    medications_given = db.relationship('Medication_Given', backref='nurse')

class Medication(db.Model):
    """medication."""
    __tablename__ = "medications"
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_prescribed = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now) 
    medications_given = db.relationship('Medication_Given', backref='medications')
    doctors_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patients_id = db.Column(db.Integer, db.ForeignKey('patients.id'))


class Medication_Given(db.Model):
    """Medication given"""
    __tablename__ = "medication_given"
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nurses_id =  db.Column(db.Integer, db.ForeignKey('nurses.id'))
    doctors_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patients_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    medications_id = db.Column(db.Integer, db.ForeignKey('medications.id')) 
    date_given = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now) 
