from flask import Flask
from flask import request

sample = Flask(__name__)

@sample.route("/")
def main():
    return "You are calling me from "+ request.remote_addr

if __name__ == "__main__":
    sample.run(port=8080, host="0.0.0.0")
