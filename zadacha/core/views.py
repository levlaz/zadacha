"""Auth module for zadacha"""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_security import current_user

import ldclient
# from zadacha.auth.forms import RegistrationForm

core = Blueprint('core', __name__, template_folder='templates')


@core.route('/')
def index():
    if current_user.is_authenticated:
        ld_user = current_user.get_ld_user()
    else:
        ld_user = {"key": "anon", "anonymous": True}

    show_new_theme = ldclient.get().variation("show-new-theme", ld_user, False)

    if show_new_theme:
        return render_template("home.html")
    else:
        return render_template("coming_soon.html")
