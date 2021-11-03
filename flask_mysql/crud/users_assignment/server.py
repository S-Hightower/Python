from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key='keep is secret, keep it safe'

@app.route('/')
def server_init():
    return "Connected"

if __name__=="__main__":
    app.run(debug=True)