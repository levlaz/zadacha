"""Auth module for FeedRead"""
from flask import Blueprint, flash, redirect, render_template, request, url_for

# from zadacha.auth.forms import RegistrationForm

core = Blueprint('core', __name__, template_folder='templates')


@core.route('/')
def index():
    return render_template("home.html")