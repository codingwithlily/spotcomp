# manage.py

from flask_script import Manager
from app import app

manager = Manager(app)

@manager.command
def runserver():
    """Starts the Flask development server."""
    app.run(debug=True)

@manager.command
def test():
    """Runs the unit tests."""
    # Write your test logic here
    print("Running unit tests...")

if __name__ == "__main__":
    manager.run()
