# Set up

Use `pip install` to get the following packages:

`flask`

`sqlalchemy`

`flask-alchemy`

`flask-bcrypt`

`pymysql`

`flask-login`

To establish connecttion to MySQ, current database url on line 9 in `blog_project/__init__.py` is set to: `mysql+pymysql://root:root1234@localhost`.

Modify user (currently set to `root`) and password (currenttly set to `root1234`) according to your system.

Database name is currently set to `blog_database` on line 10 in `blog_project/__init__.py`



# Description

All main components are in `blog_project` folder:

`__init__.py`: import project dependencies and set up database

`models.py`: data schema

`routes.py`: API endpoints


# Run

`export FLASK_APP=run.py`

`flask run`

By default, service will be running on `http://127.0.0.1:5000/`

# Test

Use curl command to test endpoint:

Ex: `curl -i -H "Content-Type: application/json" -X POST -d '{"email":"abc@gmail.com", "password":"1234", "username":"A"}' http://127.0.0.1:5000/signup/google`

To test endpoints that require user login, provide `--cookie "session=<encoded session>" ` option in your `curl` command

Ex:

```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"email":"abc@gmail.com", "password":"1234"}' http://127.0.0.1:5000/login
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 24
Vary: Cookie
Set-Cookie: session=<encoded session>; HttpOnly; Path=/
Server: Werkzeug/1.0.1 Python/3.6.0
Date: Mon, 08 Jun 2020 12:29:47 GMT
```

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/logout
```

Run `deactive` to exit virtualenv
