from flask import Flask
import datetime 
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World at ", datetime.datetime.now()

if __name__ == "__main__":
    application.run()
