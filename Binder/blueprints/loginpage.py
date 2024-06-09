from collections.abc import Sequence
from typing import Mapping
from flask import Blueprint, render_template, current_app, url_for, redirect, flash
import Binder.query as query
import requests
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired, NumberRange

import re

from Binder import app, login_manager
from Binder.models import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

loginpage_bp = Blueprint("loginpage", __name__)

class RegisterForm(FlaskForm):
    fullname = StringField(validators=[
                           InputRequired(), Length(min=4, max=20, message='Form of the names is incorrect')], render_kw={"placeholder": "Full name"})
    email = StringField(validators=[
                           InputRequired(), Length(min=4, max=100, message='Too long or too short')], render_kw={"placeholder": "Email"})
    birthDate = DateField('Insert date of birth', format='%Y-%m-%d', validators=[DataRequired()])
    instrument = SelectField('', validators=[DataRequired()], render_kw={"placeholder": "Select instrument"})
    genre = SelectField('', validators=[DataRequired()], render_kw={"placeholder": "Select genre"})
    proficiency = IntegerField('', validators=[DataRequired(), NumberRange(min=1, max=10)], render_kw={"placeholder": "Select proficiency"})
    located_in = SelectField('', validators=[DataRequired()], render_kw={"placeholder": "City of residence"})
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

@loginpage_bp.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        user = query.get_user_class_by_user_name(form.username.data)
        if user and bcrypt.check_password_hash(user['password'], form.password.data):
            login_user(user, remember=True)
            return redirect("/")
        else:
            flash("Something went wrong, please check username and password")
            return redirect("/login")
    return render_template('login/login.html', form=form)

@loginpage_bp.route('/logout')
def logout():
    logout_user()
    return redirect("/")

@loginpage_bp.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    instruments = query.get_instruments()
    genres = query.get_genres()
    cities = query.get_cities()
    form.instrument.choices = [(inst, inst) for inst in instruments]
    form.genre.choices = [(genr, genr) for genr in genres]
    form.located_in.choices = [(cit['city'], cit['city']) for cit in cities]

    genre_instruments_map = {}
    for genre in genres:
        genre_instruments_map[genre] = query.get_typical_instrument_for_genre(genre)

    if form.validate_on_submit():
        username = form.username.data
        name = form.fullname.data
        if query.get_user_class_by_user_name(username):
            flash("This username exists, pick another one")
            return redirect("/register")
        if not form.instrument.data in query.get_typical_instrument_for_genre(form.genre.data):
            flash("Genre and instrument incompatible") 
            return redirect("/register")
        if not re.search(r"[a-zA-Z0-9ÆØÅæøå]*\.?[a-zA-Z0-9ÆØÅæøå]*@[a-zA-ZÆØÅæøå]+\.[a-zA-ZÆØÅæøå]+", form.email.data):
            flash("Email syntax not correct") 
            return redirect("/register")
        if not re.search(r"[A-ZÆØÅ][a-zaæøå]+ ([A-ZÆØÅ][a-zaæøå]+ )*[A-ZÆØÅ][a-zaæøå]+", name):
            flash("Name is not correct Syntax") 
            return redirect("/register")
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        query.insert_user(name, username, hashed_password, form.birthDate.data, form.located_in.data, form.instrument.data, form.proficiency.data, form.genre.data)
        
        return redirect("/login")
    
    return render_template("login/register.html", form=form, genre_instruments_map=genre_instruments_map)
