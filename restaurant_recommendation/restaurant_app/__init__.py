
from flask import Flask, render_template, request

#Import the necessary Python packages
import pandas as pd
import numpy as np
from sklearn import preprocessing

import json

def read_data():
    restaurant_data = pd.read_csv('Restaurants_cleaned.csv')
    return restaurant_data
dat = read_data()
def recommendation_output(city, price_range):
    return dat.loc[(dat['City'] == str(city)) & (dat['Price_Range'] == int(price_range)), ['Name', 'Cuisine_Style']]

#########################################app######################################
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
def output_criteria():
    city, price_range = request.args.get('Select_City'), request.args.get('cost_index')

    restaurants_out = recommendation_output(city, price_range)
    print('city, price_range:', city, price_range, restaurants_out['Name'].values, restaurants_out['Cuisine_Style'].values )
    return render_template('output.html', restaurants_name = restaurants_out['Name'].values, Cuisine_Style = restaurants_out['Cuisine_Style'].values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #res = recommendation_output("Amsterdam", 1)
    #print(res['Name'].values, res['Cuisine_Style'].values)