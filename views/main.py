from flask import Blueprint
from flask import render_template, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('about.index'))