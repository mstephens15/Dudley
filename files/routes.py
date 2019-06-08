from flask import render_template, url_for, flash, redirect
from files import app
from files.forms import RegistrationForm, LoginForm
from files.models import User

# Route 1: Home #
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

# Route 2: Registration #
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()

    #Validates if the account was created successfully
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

# Route 3: Login #
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	#Validates if user put in their info to sign in correctly
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessful, please try again.', 'danger')
	return render_template('login.html', title='Login', form=form)
