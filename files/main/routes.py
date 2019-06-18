from flask import render_template, request, Blueprint
from files.models import Post

main = Blueprint('main', __name__)

#Route 1: Home Page #
@main.route("/home")
def home():    
    return render_template('home.html')

#Route 2: Community Page #
@main.route('/community')
def community():
	posts = Post.query.order_by(Post.date_posted.desc())
	return render_template('community.html', posts=posts)

# Route 1: Landing Page #
@main.route('/')
@main.route('/landing_page')
def landing_page():
	return render_template('landing_page.html')
