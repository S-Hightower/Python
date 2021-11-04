from flask import Flask, render_template, redirect, session
from flask.globals import request

from models.users import User

app = Flask(__name__)
app.secret_key='keep is secret, keep it safe'

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", all_users = users)

@app.route('/new')
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return render_template("create.html")

    return redirect('/')
    
if __name__=="__main__":
    app.run(debug=True)