import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId  # this will allow to use code to
# ... access the data on docs
# below, for authentication Werkzeug
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# building the connection
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# creating an instance of pymongo. constructor method
# ... "app" is the same as the above app = Flask(...).
mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
# def hello():
#     return "Hello World ... again!"
def get_tasks():
    tasks = mongo.db.tasks.find()
    # .tasks. = collection
    return render_template("tasks.html", tasks=tasks)
    # tasks=tasks. first "task" = template .html will use
    # ... second "tasks" is the var tasks = mongo.db.tasks.fin...


@app.route("/register", methods=["GET", "POST"])
def register():  # name the function the same as the url from line above
    if request.method == "POST":
        # a check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put newly created user into session vasiable/
        # ...session coockie -> session["coockie"] = ...value...
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exist in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session['user'] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # invalid password match
                flash("incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # invalid username match
            flash("incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # ...["usename"] at the end of the line,
    # ...means that onely user name key is being
    # ...taken from the database
    return render_template("profile.html", username=username)
    # first username is from html page,
    # ...the second is the variable 2 lines above


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# import os
# from flask import Flask
# # env.py is not pushed therefore we
# # ... need to load manually through this
# # ... following code.
# # ... this prevent the env from been public in github
# if os.path.exists("env.py"):
#     import env


# # creating an instance of flask
# app = Flask(__name__)


# # make sure the app is properly configured
# # ... by creating test function.
# @ app.route("/")
# def hello():
#     return "Hello World ... gain!"


# # telling the app where to run
# app.run(host=os.environ.get("IP"),
#         port=int(os.environ.get("PORT")),
#         debug=True)
# # end of test function
