
from flask import Flask, render_template, request

#Import the necessary Python packages
import pandas as pd
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/input')
def input_criteria():
    return render_template('input.html')


@app.route('/output')
def input_criteria():
    return render_template('output.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)