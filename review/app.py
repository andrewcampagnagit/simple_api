import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return os.environ["API_MESSAGE"]

@app.route("/secret")
def secrets():
	return os.environ["API_SECRET"]


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)