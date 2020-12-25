import os
from flask import Flask
# env.py is not pushed therefore we
# ... need to load manually through this
# ... following code.
# ... this prevent the env from been public in github
if os.path.exists("env.py"):
    import env


# creating an instance of flask
app = Flask(__name__)


# make sure the app is properly configured
# ... by creating test function.
@ app.route("/")
def hello():
    return "Hello World ... gain!"


# telling the app where to run
app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
# end of test function
