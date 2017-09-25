from flask import Flask, render_template, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']
    text = str(text)
    encrypted_text = rotate_string(text, rot)
    return render_template('index.html', encrypted_text=encrypted_text)


app.run()
