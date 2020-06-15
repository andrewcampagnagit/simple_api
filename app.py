from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home_page():
	return "Hello new-app!"


@app.route("/env")
def env_page():
	return os.environ["MESSAGE"]
	

if __name__=="__main__":
	app.run(host="0.0.0.0", port=8080)