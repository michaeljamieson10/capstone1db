"""SEED FOR CAPSTONE"""
from models import db, connect_db, Medication, Doctor, Patient, Nurse, Medication_Given
from app import app
import datetime

# Create Tables
db.drop_all()
db.create_all()

d1 = Doctor(first_name="mikey",last_name="jamie",office_phone="555-5555")
d2 = Doctor(first_name="Jun",last_name="Folkan",office_phone="555-5555")
d3 = Doctor(first_name="Moke",last_name="NightRyder",office_phone="555-5555")
d4 = Doctor(first_name="Miguel",last_name="Sabado",office_phone="555-5555")

db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.add(d4)
#  datetime.date(yr, month, day)
p1 = Patient(first_name="koopa",last_name="posha",date_of_birth= datetime.date(1999,1,19),patient_photo="https://www.thelocal.se/userdata/images/article/6d67730d16af04f3f956389d4cc244af808b8381c23b1e3d218ecd792de14fa8.jpg")
p2 = Patient(first_name="musha",last_name="shqarm",date_of_birth= datetime.date(2001,4,21),patient_photo="https://www.itl.cat/pngfile/big/11-111594_indian-beautiful-girl-images-wallpaper-pictures-download-indian.jpg")
p3 = Patient(first_name="Gibber",last_name="Nimmerman",date_of_birth= datetime.date(1973,1,9),patient_photo="https://www.vosizneias.com/wp-content/uploads/2019/04/jpeg.jpg")
p4 = Patient(first_name="Andy",last_name="Rudoph",date_of_birth= datetime.date(1973,1,9),patient_photo="")
p5 = Patient(first_name="Bob",last_name="James",date_of_birth= datetime.date(1973,1,9),patient_photo="")
p6 = Patient(first_name="Catherine",last_name="Hackson",date_of_birth= datetime.date(1985,4,5),patient_photo="")
p7 = Patient(first_name="Douglas",last_name="Nickerson",date_of_birth= datetime.date(1902,12,24),patient_photo="")
p8 = Patient(first_name="Enith",last_name="Thorth",date_of_birth= datetime.date(1800,2,12),patient_photo="")
p9 = Patient(first_name="Frank",last_name="Gord",date_of_birth= datetime.date(2000,3,2),patient_photo="")
p10 = Patient(first_name="Gordon",last_name="Ramsuckle",date_of_birth= datetime.date(1989,6,19),patient_photo="")
p11 = Patient(first_name="Henry",last_name="Shoowickle",date_of_birth= datetime.date(1999,3,20),patient_photo="")
p12 = Patient(first_name="Isaac",last_name="Newton",date_of_birth= datetime.date(1995,4,29),patient_photo="")
p13 = Patient(first_name="John",last_name="Hazzlesmith",date_of_birth= datetime.date(1992,4,16),patient_photo="")
p14 = Patient(first_name="Ken",last_name="Zenith",date_of_birth= datetime.date(1959, 8,4),patient_photo="")
p15 = Patient(first_name="Lewis",last_name="Apple",date_of_birth= datetime.date(1964,5,21),patient_photo="")

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.add(p6)
db.session.add(p7)
db.session.add(p8)
db.session.add(p9)
db.session.add(p10)
db.session.add(p11)
db.session.add(p12)
db.session.add(p13)
db.session.add(p14)
db.session.add(p15)

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
mg1 = Medication_Given(nurses_id=1, patients_id=1,doctors_id=1,medications_id=1)
mg2 = Medication_Given(nurses_id=1, patients_id=2,doctors_id=1,medications_id=2)

db.session.add(mg1)
db.session.add(mg2)
db.session.commit()

