import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
	plants = ["Snake Plant", "Peace Lily", "Pothos"]
	return render_template('index.html', utc_dt=datetime.datetime.utcnow(), plants=plants)
