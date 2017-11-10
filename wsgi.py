from flask import Flask
from datetime import date
application = Flask(__name__)

@application.route("/")
def hello():
    today=date.today()
    return "Hello World at ", str(today)

if __name__ == "__main__":
    application.run()
