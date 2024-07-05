from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(_name_)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')