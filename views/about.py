from flask import Blueprint
from flask import render_template, redirect, url_for

about = Blueprint('about', __name__)

@about.route('/')
def index():
  return render_template("about.html", title="about")
