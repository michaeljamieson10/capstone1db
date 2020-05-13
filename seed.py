"""SEED FOR CAPSTONE"""
from models import db, connect_db, Medication, Doctor, Patient, Nurse, Medication_Given
from app import app
import datetime

# Create Tables
db.drop_all()
db.create_all()

d1 = Doctor(first_name="mikey",last_name="jamie")

db.session.add(d1)
#  datetime.date(yr, month, day)
p1 = Patient(first_name="koopa",last_name="posha",date_of_birth= datetime.date(1999,1,19),patient_photo="https://www.thelocal.se/userdata/images/article/6d67730d16af04f3f956389d4cc244af808b8381c23b1e3d218ecd792de14fa8.jpg")
p2 = Patient(first_name="musha",last_name="shqarm",date_of_birth= datetime.date(2001,4,21),patient_photo="https://www.itl.cat/pngfile/big/11-111594_indian-beautiful-girl-images-wallpaper-pictures-download-indian.jpg")
p3 = Patient(first_name="Gibber",last_name="Nimmerman",date_of_birth= datetime.date(1973,1,9),patient_photo="https://www.vosizneias.com/wp-content/uploads/2019/04/jpeg.jpg")

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

m1 = Medication(name="tylenol 325mg",description="for pain",doctors_id=1,patients_id=1)    
m2 = Medication(name="turmeric 500mg",description="anti-oxidant",doctors_id=1,patients_id=2)    
m3 = Medication(name="caffeine tablets",description="for focus",doctors_id=1,patients_id=2)    
m4 = Medication(name="vitamin c",description="immune support",doctors_id=1,patients_id=2)    
m5 = Medication(name="hydralazine 50mg",description="blood pressure",doctors_id=1,patients_id=3)    
m6 = Medication(name="hydrophor to bilateral heels",description="Dry Skin",doctors_id=1,patients_id=3)    
m7 = Medication(name="labetalol 25mg",description="blood pressure",doctors_id=1,patients_id=3)    
m8 = Medication(name="crestor 75mg",description="hyperlipidemia, cholesterol",doctors_id=1,patients_id=3)    
m9 = Medication(name="vancomycin PO",description="C Diff",doctors_id=1,patients_id=3)    

db.session.add(m1)
db.session.add(m2)
db.session.add(m3)
db.session.add(m4)
db.session.add(m5)
db.session.add(m6)
db.session.add(m7)
db.session.add(m8)
db.session.add(m9)

n1 = Nurse(first_name="Michael",last_name="Jamieson")

db.session.add(n1)

db.session.commit()
# mg1 = Medication_Given(nurses_id=1, doctors_id=1, patients_id=1)

# db.session.add(mg1)
db.session.commit()

