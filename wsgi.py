from flask import Flask
import datetime 
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World at " + time.strftime("%Y-%m-%d %H:%M")

if __name__ == "__main__":
    application.run()
