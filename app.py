from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#Create lite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '2ea91db6b60bffa7dc5d1fc3c5d26223'

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(20), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default = 'default.jpg')
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


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

if __name__ == '__main__':
	app.run(debug=True)