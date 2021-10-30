from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def server_init():
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    return 

# @app.route('/count')
# def server_count():
#     return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)