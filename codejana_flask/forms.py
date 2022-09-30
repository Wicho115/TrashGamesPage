from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField(label = 'Username', validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(),Length(min=6,max=20)])
    confirm_password= PasswordField(label= 'Confirm Password', validators =[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Sign Up')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(),Length(min=6,max=20)])
    submit = SubmitField(label='Login')
