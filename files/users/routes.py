from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from files import db, bcrypt
from files.models import User
from files.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from files.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)


# Route 1: Registration #
@users.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = RegistrationForm()

    #Validates and creates user if the account was created successfully
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created!', 'success')
		return redirect(url_for('users.login'))
	return render_template('register.html', title='Register', form=form)

# Route 2: Login #
@users.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = LoginForm()

	#Validates if user put in their info to sign in correctly
	#Sees if user exists, then if user exists and their database password is what they typed in
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('main.home'))
		else:
			flash('Login unsuccessful, please check email and password.', 'danger')
	return render_template('login.html', title='Login', form=form)

# Route 3: Logout #
@users.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.landing_page'))

# Route 4: Account #
@users.route('/account', methods=['GET', 'POST'])
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
		return redirect(url_for('users.account'))
#Populates the form with whatever the username and email values are
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	return render_template('account.html', title='Account', image_file=image_file, form=form)


# Route 5: Where they enter email to get password sent  #
@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = RequestResetForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		send_reset_email(user)
		flash('An email has been sent with instructions to reset your password.', 'info')
		return redirect(url_for('users.login'))
	return render_template('reset_request.html', title='Reset Password', form=form)

# Route 6: Actually to reset the password  #
@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
