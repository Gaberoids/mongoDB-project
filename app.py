import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# this will allow to use code to
# ... access the data on docs
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
