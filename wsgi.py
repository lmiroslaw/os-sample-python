from flask import Flask
from datetime import datetime, date
application = Flask(__name__)

@application.route("/")
def hello():
    d = datetime.datetime.now()
    return "Hello World at "

if __name__ == "__main__":
    application.run()
