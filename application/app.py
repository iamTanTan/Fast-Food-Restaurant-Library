from flask import Flask, render_template, request, flash, redirect
import os
import psycopg2
from credentials import DB_URL

app = Flask(__name__)

# YOU NEED TO ADD THE credentials.py file from google drive
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
    # get menus for restaurant
    cur.execute('SELECT * FROM menu WHERE fast_food_restaurant_id = %s', \
        (id,))
    menus = cur.fetchall()
    # get reviews for restaurant
    cur.execute('SELECT * FROM review WHERE fast_food_restaurant_id = %s', \
        (id,))
    reviews = cur.fetchall()
    # get average rating
    cur.execute('SELECT AVG(rating) FROM review WHERE fast_food_restaurant_id = %s', \
        (id,))
    average_rating = cur.fetchone()
    #get hours for restaurant
    cur.execute('SELECT * FROM hours WHERE fast_food_restaurant_id = %s', \
        (id,))
    hours = cur.fetchall()
    cur.close()
    conn.close()

    context = {
        "menus": menus,
        "hours": hours,
        "reviews": reviews,
        "average_rating": average_rating
    }

    return render_template('restaurant_detail.html', context=context)

# POST REQUEST handling to create a restaurant
@app.route('/create_restaurant', methods=['POST', 'GET'])
def create_restaurant():
    if request.method == 'GET':
        return render_template('create_restaurant.html')
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

# post route to delete a restaurant
# see form action on index.html and input with name="id"
@app.route('/delete_restaurant', methods=['POST'])
def delete_restaurant():
    if request.method == 'POST':
        # grab the id from the request.form information
        id = request.form['id']
        print(id)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM fast_food_restaurant WHERE id = %s', (id,))
        cur.close()
        conn.close()

    return redirect('/')

# UNIMPLEMENTED
#
# PROBABLY MISSING SOME CURRENTLY
#
@app.route('/menu/<int:id>', methods=['GET'])
def menu_detail(id):
    return "Add Stuff like food items on the menu"

@app.route('/create_food_item', methods=['POST', 'GET'])
def create_food_item():
    if request.method == 'POST':
        return "yo"
    elif request.method == 'GET':
        return "ye"
    else:
        return "invalid"

@app.route('/create_menu', methods=['POST'])
def create_menu():
    if request.method == 'POST':
        return "do stuff"
    
    return redirect('/')

@app.route('/create_review', methods=['POST', 'GET'])
def create_review():
    if request.method == 'POST':
        return "yo"
    elif request.method == 'GET':
        return "ye"
    else:
        return "invalid"

# this was a copy paste from restaurant delete with tiny renames
@app.route('/delete_menu', methods=['POST'])
def delete_menu():
    if request.method == 'POST':
        # grab the id from the request.form information
        id = request.form['id']
        print(id)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM menu WHERE id = %s', (id,))
        cur.close()
        conn.close()

    return redirect('/')

@app.route('/delete_food_item', methods=['POST'])
def delete_food_item():
    if request.method == 'POST':
        # grab the id from the request.form information
        id = request.form['id']
        print(id)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM food_item WHERE id = %s', (id,))
        cur.close()
        conn.close()

    return redirect('/')

    


if __name__ == '__main__':
    app.run()