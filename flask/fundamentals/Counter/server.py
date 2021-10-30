from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key='keep is secret, keep it safe'

@app.route('/')
def server_init():
    if 'count' not in session:
        session['count']=0
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/destroy_session')
def destroy_session():
    return 

@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)