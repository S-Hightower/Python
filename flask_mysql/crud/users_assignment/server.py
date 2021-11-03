from flask import Flask, render_template, redirect, session

from users import User

app = Flask(__name__)
app.secret_key='keep is secret, keep it safe'

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", all_users = users)

if __name__=="__main__":
    app.run(debug=True)