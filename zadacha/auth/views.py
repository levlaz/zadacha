"""Auth module for FeedRead"""
from flask import Blueprint, flash, redirect, render_template, request, url_for

from zadacha.models.user import User
# from zadacha.auth.forms import RegistrationForm

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/')
def index():
    return 'auth route'