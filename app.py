from files import create_app, db
from files.models import User, Role, Post
from flask_migrate import Migrate

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Post=Post)

migrate = Migrate(app, db)