from flask import render_template, request, Blueprint
from files.models import Post, User
from flask_login import login_user, logout_user
from flask_security import roles_required

main = Blueprint('main', __name__)

# Route 1: Landing Page #
@main.route('/')
@main.route('/landing_page')
def landing_page():
	return render_template('landing_page.html')

#Route 2: Home Page #
@main.route("/home")
def home():    
    return render_template('home.html')

#Route 3: Community Page #
@main.route('/community')
def community():
	posts = Post.query.order_by(Post.date_posted.desc())
	return render_template('community.html', posts=posts)

#Route 4: Announcements #
@main.route("/announcements")
def announcements():    
    return render_template('announcements.html')

#Route 5: Challenge #
@main.route("/challenge")
def challenge():
	return render_template('challenge.html')

#Route 6: Admin Login #
@main.route("/adminpage")
def admin():
	user = User.query.get(1)
	login_user(user)
	return "YAYYY"
