from flask import render_template, Blueprint, request
from files.models import User

main = Blueprint('main', __name__)

# Route 1: Home #
@main.route('/')
@main.route('/landing_page')
def landing_page():
	return render_template('landing_page.html')

# Route 2: Home #
@main.route('/home')
def home():
	return render_template('home.html')
