from crypt import methods
from app.models import User
from flask import render_template,request, redirect,url_for,flash,abort
from app import render_template,app,db
from app.forms import RegisterForm


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
