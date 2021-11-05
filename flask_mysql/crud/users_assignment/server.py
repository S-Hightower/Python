from flask.globals import request

from flask_app import app
from flask_app.controllers import controller

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("flask_app.templates.read(all).html", all_users = users)

@app.route('/new')
def add_user(data):
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