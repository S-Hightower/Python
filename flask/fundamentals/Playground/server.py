from flask import Flask

app = Flask(__name__)

@app.route('/play')
def hello_world():
    return 'Main Project Page'

if __name__=="__main__":
    app.run(debug=True)