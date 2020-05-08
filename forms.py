from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired

# 


# class UserAddForm(FlaskForm):
#     """Form for adding users."""

#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('E-mail', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[Length(min=6)])
#     image_url = StringField('(Optional) Image URL')


# class UserEditForm(FlaskForm):
#     """Form for adding users."""

#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('E-mail', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[Length(min=6)])
#     image_url = StringField('(Optional) Image URL')
#     header_image_url = StringField('(Optional) header_image_url')
#     bio = StringField('(Optional) Enter your biography here')

# class LoginForm(FlaskForm):
#     """Login form."""

#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[Length(min=6)])
class NewMedicationPatientForm(FlaskForm):
    """Form for adding a song to playlist."""

    patient = SelectField('Patient To Add to Medication', coerce=int)
    doctor = SelectField('Doctor To Add to Medication', coerce=int)

