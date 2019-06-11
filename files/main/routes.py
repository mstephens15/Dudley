from flask import render_template, Blueprint, request
from files.models import User

main = Blueprint('main', __name__)

# Route 1: Home #
@main.route('/')
@main.route('/home')
def home():
	return render_template('home.html')
