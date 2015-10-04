from flask import Flask
from flask import render_template
import models

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('Homepage.html')

@app.route("/start")
def start():
    return render_template('Locations.html')

@app.route("/results")
def results():
    return render_template('Results.html')

@app.route("/hop/<query>")
def hop(query):
    a = models.Location('42.360082', '-71.058880')
    b = models.Location('42.525656', '-71.095289')

    g = models.Graph(a, b)
    print g.get_paths()

if __name__ == "__main__":
    app.run()