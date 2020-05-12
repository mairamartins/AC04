from flask import Flask, render_template
app = Flask(__name__)


@app.route('/inicio')
@app.route('/')
def hello_world():
    return render_template('inicio.html')


@app.route('/login')
def contato():
    return render_template('login.html')
