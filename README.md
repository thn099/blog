# Set up

Run `cd` to `blog` folder

Run `source env/bin/activate` to activate virtualenv

To establish connecttion to MySQ, current database url on line 9 `__init__.py` is set to: 'mysql+pymysql://root:root1234@localhost'.

Modify user (currently set to `root`) and password (currenttly set to `root1234`) according to your system

Modify database name `blog_database` if there is existing duplicate.



# Description

All main components are in `blog_project` folder

`__init__.py`: import project dependencies and set up database

`models.py`: data schema

`routes.py`: API endpoints


# Run

`export FLASK_APP=run.py`

`flask run`

By default, service will be running on http://127.0.0.1:5000/

# Test

Use curl command to test endpoint:

Ex: `curl -i -H "Content-Type: application/json" -X POST -d '{"email":"abc@gmail.com", "password":"1234", "username":"A"}' http://127.0.0.1:5000/signup/google
