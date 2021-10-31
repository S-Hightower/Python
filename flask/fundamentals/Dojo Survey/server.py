from flask import Flask, render_template, redirect, session
from flask.globals import request

app = Flask(__name__)
app.secret_key='keep is secret, keep it safe'

@app.route('/')
def server_init():
    return render_template('index.html')

@app.route('/results', methods = ['POST'])
def results():
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        return render_template('results.html', name = request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])

if __name__=="__main__":
    app.run(debug=True)