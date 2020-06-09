# Set up

Use `pip install` to get required packages:

`pip install flask`

`pip install sqlalchemy`

`pip install flask-alchemy`

`pip install flask-bcrypt`

`pip install pymysql`

`pip install flask-login`

To establish connecttion to MySQL, current database url on line 9 in `blog_project/__init__.py` is set to: `mysql+pymysql://root:root1234@localhost`.

Modify `user` (currently set to `root`) and `password` (currenttly set to `root1234`) in the database url according to your system.

Database name is currently set to `my_database` on line 10 in `blog_project/__init__.py`.

Assume system is running MySQL.


# Description

All main components are in `blog_project` folder:

`__init__.py`: import project dependencies and set up MySQL database

`models.py`: data schema for User, Post, PostLike, GoogleUser (inherit from User), FacebookUser (inherit from User)

`routes.py`: API endpoints

/

/home

/login

/logout

/signup/facebook

/signup/google

/posts

/posts/new

/posts/<int:post_id>

/posts/<int:post_id>/like

/posts/<int:post_id>/unlike

/posts/<int:post_id>/number_of_likes

/posts/<int:post_id>/likes

/account

Note: I didn't have 2 endpoints `http://127.0.0.1:5000/login/facebook` (to login using Facebook) and `http://127.0.0.1:5000/login/google` (to login using Google) because those would involve client id and key access in order to make calls to Google and Facebook login APIs. For now, user can login using email and password through `http://127.0.0.1:5000/login`


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

To create a Facebook user account:

```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"email":"abcd@gmail.com", "password":"1234", "username":"B"}' http://127.0.0.1:5000/signup/facebook
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
Date: Mon, 08 Jun 2020 10:29:47 GMT
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

To update occupation number (for Google user):

```
$ curl --cookie "session=<encoded session>" -i -H "Content-Type: application/json" -X PUT -d '{"occupation":"student"}' http://127.0.0.1:5000/account/update
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

To create a new post:

```
$ curl --cookie "session=<encoded session>" -i -H "Content-Type: application/json" -X POST -d '{"title":"a title", "content":"some content"}' http://127.0.0.1:5000/posts/new
```

To like a post (similar for unlike):

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/posts/<int:post_id>/like
```

To get list of users who like a post:

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/posts/<int:post_id>/likes
```

To get the number of people who liked a post:

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/posts/<int:post_id>/number_of_likes
```

To logout

```
$ curl --cookie "session=<encoded session>" http://127.0.0.1:5000/logout
```

To see how data is updated, run queries on python shell or run mySQL commands to display data:

![](data.png)
