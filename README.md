# Install Dependencies

Use `pip install` to get the following packages:

`flask`

`sqlalchemy`

`flask-alchemy`

`flask-bcrypt`

`flask-login`

Install python3

Install mysql

Database engine url: 'mysql+pymysql://root:root1234@localhost/blog_database'


# Description

`__init__.py`: import project dependencies and set up database

`models.py`: data schema

`routes.py`: API endpoints


# Run

cd to flask_blog folder

Run: flask run


# Test

Use curl command to test endpoint:

Ex: `curl -i -H "Content-Type: application/json" -X POST -d '{"email":"abc@gmail.com", "password":"1234", "username":"A"}' http://127.0.0.1:5000/signup/google`
