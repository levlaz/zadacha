"""Auth module for zadacha"""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_security import current_user

import ldclient
# from zadacha.auth.forms import RegistrationForm
from zadacha.core.forms import TaskForm
from zadacha.models.task import Task

core = Blueprint('core', __name__, template_folder='templates')


@core.route('/', methods=('GET', 'POST'))
def index():
    form = TaskForm()
    if form.validate_on_submit():
        Task.add_task(current_user, form)
        return redirect(request.referrer)
    if current_user.is_authenticated:
        ld_user = current_user.get_ld_user()
    else:
        ld_user = {"key": "anon", "anonymous": True}

    show_new_theme = ldclient.get().variation("show-new-theme", ld_user, False)

    if show_new_theme:
        return render_template("home.html", form = form)
    else:
        return render_template("coming_soon.html")