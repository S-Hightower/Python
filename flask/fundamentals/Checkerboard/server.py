from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def server_init():
    return render_template('index.html', across = 8, down = 8)

@app.route('/<num>')
def step_two(num):
    return render_template('index.html', across = 8, down = int(num))

@app.route('/<x>/<y>')
@app.route('/<x>/<y>/<colora>/<colorb>')
def step_three(x,y, colora='red', colorb='black'):
    return render_template('index.html', across = int(x), down =int(y), colora=colora, colorb=colorb)

if __name__=="__main__":
    app.run(debug=True)