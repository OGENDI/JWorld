from crypt import methods
from app.models import User
from flask import render_template,request, redirect,url_for,flash,abort
from flask_login import login_user,logout_user,login_required,current_user
from app import render_template,app,db
from app.forms import RegisterForm,LoginForm


@app.route('/',methods=['GET','POST'])
def home_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome to Jworld and experience gaming like never before',category='success')
    if form.errors != {}:
        for error_message in form.errors.values():
            flash(f'There was an error with creating a user: {error_message}',category='danger')
    return render_template('landing.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.username}',category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Username and password do not match! Please try again',category='danger')
    return render_template('login.html',form=form)
