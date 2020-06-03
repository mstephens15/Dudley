# Dudley
Website

### Version 1.11
>Added Role model and debugged

### Version 1.12 
>requirements.txt
	-this just shows all of the pip3 installs I have had when I want to do testing
>tests folder
>config.py
	-added some testing configurations for different parts of app
>messed around a lot with databases, deleted all and creating new users

### Version 1.13 
>Deleted roles model
	-I only have two roles, admin and player, so I don't need a whole class. Keep it simple.
>added is.admin to User model

### Version 1.14 (Closed 11/4/19)
>Added a Controller Model
>Added admin page and features that only I can get into

### Version 1.15 (Closed 11/18/19 -- Still running, additions that break code are commented out currently)
>Added Flask Security from (Intro to Flask-Security)
>Added security folder with login_user.html


### Version 1.16 (Closed 2/3/20) ###
>Added follows class
>Added followed/follwers to User class


## --Pending issues -- ##
>>how to automatically assign roles when people sign up for the website
>>how to override login page of flask security with my own
>>follow is now on the page, however when I click it it gives me an error still, check it out...

    models.py
    routes.py
    user_posts.html

### Version 1.17 (Closed 4/14/20)
>Recreating "home" to be more simple like my Beta 1.0 workflow drawings
>Editing mainly workout.html and betaone.html
>Added new CSS page, general.css 
>Cleaned up CSS; made classes like real classes i.e. can be used many times, id for specific

### Version 1.18 (Closed 4/14/20)
>Streak and total not updating


### Version 1.19 (Open 6/3/20)
>Was able to get streak and total working; have been moving on to making the game now

<!--- {% if user != current_user %}
        {% if not current_user.is_following(user) %}
        <a href="{{ url_for('.follow', username=user.username) }}"
            class="btn btn-default">Follow</a>
        {% else %}
        <a href="{{ url_for('.unfollow', username=user.username) }}"
            class="btn btn-default">Unfollow</a>
        {% endif %}
    {% endif %}
    <a href="{{ url_for('.followers', username=user.username) }}">
        Followers: <span class="badge">{{ user.followers.count() }}</span>
    </a>
    <a href="{{ url_for('.followed_by', username=user.username) }}">
        Following: <span class="badge">{{ user.followed.count() }}</span>
    </a>
    {% if current_user.is_authenticated and user != current_user and user.is_following(current_user) %}
        <span class="label label-default">Follows you</span>
    {% endif %}

    --->