from flask import Flask, render_template, request, flash, redirect
import os
import psycopg2
from credentials import DB_URL

app = Flask(__name__)

# set os variable locally
#app.config['DB_URL'] = "postgresql://localhost/fastfood_db"
app.config['DB_URL'] = DB_URL
app.config['SECRET_KEY'] = 'asldfkhalsdr9023875934etQAR93123BEIAWUGAFVBEA9ERTHQP4'

def get_db_connection():
    conn = psycopg2.connect(app.config['DB_URL'])
    conn.autocommit = True
    return conn

#  This defines an endpoint for a url
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM fast_food_restaurant;')
    restaurants = cur.fetchall()
    print(restaurants)
    cur.close()
    conn.close()

    # render a template and pass in context (restuarants) to use in the html (see templates index.html for this one)
    return render_template('index.html', restaurants=restaurants)

# this route has the restuarant id passed into the url as a parameter
# we can use this parameter as a function argument and then query for the data
@app.route('/restaurant/<int:id>/menus')
def restaurant_detail(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM menu WHERE fast_food_restaurant_id = %s', \
        (id,))
    menus = cur.fetchall()
    print(menus)
    cur.close()
    conn.close()

    return render_template('menus.html', menus = menus)

# POST REQUEST handling to create a restaurant
@app.route('/create_restaurant', methods=['POST'])
def create_restaurant():
    # "grab" the data from the form
    if request.method == 'POST':
        name = request.form['name']
        rtype = request.form['type']
        location = request.form['location']
        price = request.form['price'].lower()

        # validate all data is present
        if not name or not rtype or not location or not price:
            flash('Must fill in all fields for a new restaurant!')
        elif price != 'low' and price != 'medium' and price != 'high':
            flash('Invalid Price Format!')
        else:
            # create the data with psycopg2 here
            print("create a restuarant here")
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('SELECT COUNT(*) FROM fast_food_restaurant')
            new_id = cur.fetchone()[0] + 1
            print(new_id)
            cur.execute('INSERT INTO fast_food_restaurant VALUES (%s,  %s, %s, %s, %s)', 
            (new_id, name, location, rtype, price))
            cur.close()
            conn.close()

    return redirect('/')



if __name__ == '__main__':
    app.run()