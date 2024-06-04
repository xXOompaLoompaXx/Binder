from flask import Blueprint, render_template, current_app, url_for, redirect, flash
import query
import requests
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError





loginpage_bp = Blueprint("loginpage", __name__ )


class RegisterForm(FlaskForm):
    fullname = StringField(validators=[
                           InputRequired(), Length(min=4, max=20, message='Form of the names is incorrect')], render_kw={"placeholder": "Your full name"})

    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20, message='Form of the username is incorrect')], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20, message='Form of the password is incorrect')], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    



@loginpage_bp.route('/login')
def login():
    return render_template("login.html")



@loginpage_bp.route('/register', methods= ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        if query.getUserByUsername(username):
            flash("This username exists, pick another one")
            return redirect("/register")
        hashed_password = current_app.config["bcrypt"].generate_password_hash(form.password.data).decode('utf-8') 
        name = form.fullname.data
        query.insert_user(name, username, hashed_password)
        return redirect("/")
    
    return render_template("register.html", form = form)