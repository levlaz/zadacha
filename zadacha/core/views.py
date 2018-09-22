"""Auth module for FeedRead"""
from flask import Blueprint, flash, redirect, render_template, request, url_for

from zadacha.factory import ldclient

# from zadacha.auth.forms import RegistrationForm

core = Blueprint('core', __name__, template_folder='templates')


@core.route('/')
def index():
    show_new_theme = ldclient.get().variation("show-new-theme", {"key": "anon"}, False)
    if show_new_theme:
        return render_template("home.html")
    else:
        return render_template("coming_soon.html")
