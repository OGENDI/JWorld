from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from app.models import User


class RegisterForm(FlaskForm):

    def validate_username(self,check_username):
        user = User.query.filter_by(username=check_username.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
    
    def validate_email(self,check_email):
        email_adress = User.query.filter_by(email=check_email.data).first()
        if email_adress:
            raise ValidationError('Email adress already exists! Please try a different email adress')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Adress:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')