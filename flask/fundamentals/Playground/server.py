from flask import Flask

app = Flask(__name__)

@app.route('/play')
def hello_world():
    return 'Hello World!'