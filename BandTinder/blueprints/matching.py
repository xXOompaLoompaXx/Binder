from flask import Blueprint, render_template, flash, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import BandTinder.query as query
import requests
from apscheduler.schedulers.background import BackgroundScheduler

matching_bp = Blueprint("matching", __name__ )


def scheduled_task():
    pass

scheduled_task()
scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_task, trigger="interval", seconds=60)
scheduler.start()

@matching_bp.route('/matcher')
def matcher():
    pass

# @matching_bp.route('/demo')
# def demo():
# scheduled_task()