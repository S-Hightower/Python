from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def hello_world():
    return 'Hello World!'