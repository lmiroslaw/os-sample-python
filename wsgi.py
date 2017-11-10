from flask import Flask
from datetime import datetime, date
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World at %s", datetime.strftime("%Y-%m-%d %H:%M")

if __name__ == "__main__":
    application.run()
