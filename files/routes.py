import secrets
import os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from files import app, db, bcrypt
from files.forms import RegistrationForm, LoginForm, UpdateAccountForm
from files.models import User
from flask_login import login_user, current_user, logout_user, login_required

# Route 1: Home #
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

# Route 2: Registration #
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()

    #Validates and creates user if the account was created successfully
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

# Route 3: Login #
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()

	#Validates if user put in their info to sign in correctly
	#Sees if user exists, then if user exists and their database password is what they typed in
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login unsuccessful, please check email and password.', 'danger')
	return render_template('login.html', title='Login', form=form)

# Route 4: Logout #
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))

#form_picture is the file that the user submits
# _ is normally 'f_name', represents the file without the extension
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

#Resize photo
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# Route 5: Account #
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()

#If user submits a valid form to change their username and email, it will change	
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been updated!', 'success')
		return redirect(url_for('account'))
#Populates the form with whatever the username and email values are
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	return render_template('account.html', title='Account', image_file=image_file, form=form)
