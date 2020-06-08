# Set up

Use `pip install` to get the following packages:

`flask`

`sqlalchemy`

`flask-alchemy`

`flask-bcrypt`

`pymysql`

`flask-login`

To establish connecttion to MySQL, current database url on line 9 in `blog_project/__init__.py` is set to: `mysql+pymysql://root:root1234@localhost`.

Modify `user` (currently set to `root`) and `password` (currenttly set to `root1234`) in the database url according to your system.

Database name is currently set to `blog_database` on line 10 in `blog_project/__init__.py`



# Description

All main components are in `blog_project` folder:

`__init__.py`: import project dependencies and set up database

`models.py`: data schema

`routes.py`: API endpoints

Note: I didn't have `login/facebook` and `login/google` (although I'm supposed to have) because those involve client id and key access in order to function. So no setting up for Google and Facebook login APIs.


# Run

```
$ export FLASK_APP=run.py
```

```
$ flask run
```

By default, service will be running on `http://127.0.0.1:5000/`

# Test

Use curl command to test endpoint:

Ex:

To create a Google user account:

```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"email":"abc@gmail.com", "password":"1234", "username":"A"}' http://127.0.0.1:5000/signup/google
```

To test endpoints that require user login, provide `--cookie "session=<encoded session>" ` option in your `curl` command

Ex:

You get a session encoded string when logging in:

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

Provide that encoded string in subsequent calls until logging out:

Ex:

To get user information:

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/account
```

To update phone number (for Facebook user):

```
$ curl --cookie "session=<encoded session>" -i -H "Content-Type: application/json" -X PUT -d '{"phone_number":"111"}' http://127.0.0.1:5000/account/update
```

To get all posts (home page):

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/
```

To see current user posts:

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/posts
```

To see a particular post:

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/posts/<int:post_id>
```

To create a new post

```
$ curl --cookie "session=<encoded session>" -i -H "Content-Type: application/json" -X POST -d '{"title":"a title", "content":"some content"}' http://127.0.0.1:5000/posts/new
```

To like a post (similar for unlike)

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/posts/<int:post_id>/like
```

To get list of users who like a post

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/posts/<int:post_id>/get_likes
```

To logout

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/logout
```

To see how data is updated, run queries on python shell or run mySQL commands to display data

![](data.png)