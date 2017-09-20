from flask import Flask, render_template
from caesar input rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

app.run()
