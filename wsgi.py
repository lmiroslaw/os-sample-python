from flask import Flask
import datetime 
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World at " 

if __name__ == "__main__":
    application.run()
