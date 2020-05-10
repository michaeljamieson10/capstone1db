from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, DataRequired
from datetime import date

day_date_of_birth_list = []
for i in range(1, 32):
    x = (i,i)
    day_date_of_birth_list.append(x)

year_ = date.today().year
year_date_of_birth_list = []
for i in range(1900, year_):
    x = (i,i)
    year_date_of_birth_list.append(x)

class NewPatientForm(FlaskForm):
    """Create a new patient form."""
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email')
    ethnicity = StringField('Ethnicity')
    gender = StringField('Gender')
    month = SelectField("Date Of Birth", choices=[(1, 'January'), (2,'February'),(3, 'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')], coerce=int) 
    day = SelectField("Day Date Of Birth", choices=day_date_of_birth_list, coerce=int)
    year = SelectField("Year Date Of Birth", choices=year_date_of_birth_list, coerce=int) 

class NewMedicationPatientForm(FlaskForm):
    """Form for adding a song to playlist."""

    patient = SelectField('Patient To Add to Medication', coerce=int)
    doctor = SelectField('Doctor To Add to Medication', coerce=int)
    description = StringField('Why Is this patient taking this medication?')


