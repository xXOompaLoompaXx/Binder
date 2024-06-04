from flask import Blueprint, render_template, current_app, url_for, redirect, flash
import BandTinder.query as query
import requests
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from BandTinder import app, login_manager
from BandTinder.models import User

bcrypt = Bcrypt(app)

loginpage_bp = Blueprint("loginpage", __name__ )


class RegisterForm(FlaskForm):
    fullname = StringField(validators=[
                           InputRequired(), Length(min=4, max=20, message='Form of the names is incorrect')], render_kw={"placeholder": "Your full name"})

    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20, message='Form of the username is incorrect')], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20, message='Form of the password is incorrect')], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@loginpage_bp.route('/login', methods= ["GET", "POST"])
def login():
    if current_user.is_authenticated:
            return redirect("/")
    form = LoginForm()

    if form.validate_on_submit():
        if form.validate_on_submit():
            user = query.get_user_by_user_name(form.username.data)
            if user and bcrypt.check_password_hash(user['password'], form.password.data):
                login_user(user, remember=True)
                return redirect("/")
            else:
                flash("Something Went wrong, please check username and password")
                return redirect("/login")
                
    return render_template('login.html', form=form)

            
    return render_template('login.html', form=form)

@loginpage_bp.route('/logout')
def logout():
    logout_user()
    return redirect("/")

@loginpage_bp.route('/register', methods= ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        if query.get_user_by_user_name(username):
            flash("This username exists, pick another one")
            return redirect("/register")
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') 
        name = form.fullname.data
        query.insert_user(name, username, hashed_password)
        
        return redirect("/login")
    
    return render_template("register.html", form = form)