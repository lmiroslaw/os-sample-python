from flask import Flask
from datetime import date
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World at " + str(date.datetime.today())

if __name__ == "__main__":
    application.run()
