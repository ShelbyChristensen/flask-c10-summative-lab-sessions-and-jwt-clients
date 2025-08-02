# Flask Notes API – Productivity App Backend

# Project Description

This is a secure Flask API backend for a personal productivity tool that allows users to manage their own notes. It supports full session-based authentication and protects all routes to ensure that users can only access their own data.

# Tech Stack

- Python 3.10
- Flask 2.2.2
- SQLAlchemy 3.0.3
- Flask-Migrate
- Flask-Bcrypt
- Flask-RESTful
- Faker (for seeding)
- Marshmallow (optional for validation)

#  Installation Instructions

Make sure you're using Python 3.10.

# Clone the repository
git clone <your-github-repo-url>
cd backend

# Set up Virtual Envirnoment
pipenv install
pipenv shell

# Initalize the Database
flask db init
flask db migrate -m "Inital migration"
flask db upgrade

# Seed the Database
python -m db.seed

#  Run the Server
flask run


