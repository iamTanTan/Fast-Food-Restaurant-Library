from flask import Flask, render_template, request, flash, redirect
import os
import psycopg2
from forms import RestaurantForm, MenuForm, ReviewForm, FoodItemForm, HoursForm
from credentials import DB_URL

app = Flask(__name__)

# YOU NEED TO ADD THE credentials.py file from google drive
app.config['DB_URL'] = DB_URL
app.config['SECRET_KEY'] = 'asldfkhalsdr9023875934etQAR93123BEIAWUGAFVBEA9ERTHQP4'

def get_db_connection():
    conn = psycopg2.connect(app.config['DB_URL'])
    conn.autocommit = True
    return conn

def close_db_connection(conn, cur):
    cur.close()
    conn.close()

##################################################################################################
# ALL OF THE FOLLOWING ARE WORKING ROUTES (see below this section for unimplemented functions etc.)

#  This defines an endpoint for a url. Homepage 
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    # a get request occurs when you type/navigate to a url normally
    if request.method == 'GET':
        cur.execute('SELECT * FROM fast_food_restaurant;')
    # on search an POST request is sent to the server and some other action is done
    if request.method == 'POST':
        # our post is triggered on a form submission with data from the field named "query"
        query = request.form['query']
        cur.execute('SELECT * FROM fast_food_restaurant WHERE name LIKE %(name)s', { 'name': '%{}%'.format(query)})
    restaurants = cur.fetchall()    
    close_db_connection(conn, cur)

    # render a template and pass in context (restuarants) to use in the html 
    # (see templates index.html for this one)
    return render_template('index.html', restaurants=restaurants)



# POST REQUEST handling to create a restaurant
@app.route('/create_restaurant', methods=['POST', 'GET'])
def create_restaurant():
    # create form entity
    form = RestaurantForm()

    # "grab" the data from the form on submit (method also checks for POST request)
    if form.validate_on_submit():
        name = form.name.data
        rtype = form.rtype.data
        location = form.location.data
        price = form.price.data.lower()

        # create the data with psycopg2 here
        conn = get_db_connection()
        cur = conn.cursor()
        # Note: this is the wrong way to insert data. We should use a serial field so that we don't have two
        # clients try to make the same insertion (id val) simultaneously (write conflict)
        cur.execute('SELECT MAX(id) FROM fast_food_restaurant')
        new_id = cur.fetchone()[0] + 1
        print(new_id)
        cur.execute('INSERT INTO fast_food_restaurant VALUES (%s,  %s, %s, %s, %s)', 
        (new_id, name, location, rtype, price))
        close_db_connection(conn, cur)

        # redirect to another endpoint 
        return redirect('/restaurant/' + str(new_id))
    
    return render_template('/create/create_restaurant.html', form=form)

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
        close_db_connection(conn, cur)

    return redirect('/')

# DONE
# this was a copy paste from restaurant delete with tiny renames
@app.route('/restaurant/<int:restaurant_id>/delete_menu', methods=['POST'])
def delete_menu(restaurant_id):
    if request.method == 'POST':
        # grab the id from the request.form information 
        # (Note I didn't create a custom form, this is from the http request value)
        id = request.form['id']
        print(id)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM menu WHERE id = %s', (id,))
        close_db_connection(conn, cur)

    return redirect('/restaurant/' + str(restaurant_id))

# DONE
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete_food_item', methods=['POST'])
def delete_food_item(restaurant_id, menu_id):
    if request.method == 'POST':
        # grab the id from the request.form information
        id = request.form['id']
        print(id)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM food_item WHERE id = %s', (id,))
        close_db_connection(conn, cur)

    return redirect('/restaurant/' + str(restaurant_id) + "/menu/" + str(menu_id))

###################### Detail Pages ######################
# this route has the restuarant id passed into the url as a parameter
# we can use this parameter as a function argument and then query for the data
@app.route('/restaurant/<int:id>/')
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
    close_db_connection(conn, cur)

    # we can pass all this data to be displayed on the template
    context = {
        "menus": menus,
        "hours": hours,
        "reviews": reviews,
        "average_rating": average_rating
    }

    return render_template('restaurant_detail.html', context=context)

# DONE
@app.route('/restaurant/<int:restaurant_id>/menu/<int:id>', methods=['GET'])
def menu_detail(restaurant_id, id):
    conn = get_db_connection()
    cur = conn.cursor()
    # get food for menu
    cur.execute('SELECT * FROM food_item WHERE menu_id = %s', \
        (id,))
    food_items = cur.fetchall()

    return render_template('menu_detail.html', food_items=food_items, menu_id=id)

###################### Food Item ######################
#DONE 
# displays the create food item html page with the form 
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/create_food_item', methods=['POST', 'GET'])
def create_food_item(restaurant_id, menu_id):
    form = FoodItemForm()
    if form.validate_on_submit():
        price = form.price.data
        name = form.name.data
        # do sql stuff
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT MAX(id) FROM food_item;')
        new_id = cur.fetchone()[0] + 1
        print(new_id)
        cur.execute('INSERT INTO food_item VALUES (%s,  %s, %s, %s)', 
        (new_id, name, price, menu_id))
        close_db_connection(conn, cur)

        return redirect('/restaurant/' + str(restaurant_id) + "/menu/" + str(menu_id))
    return render_template('create/create_food_item.html', form=form, heading="create")

# displays the create food item html page with the form 
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit_food_item/<int:food_id>', methods=['POST', 'GET'])
def edit_food_item(restaurant_id, menu_id, food_id):
    # get current food
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM food_item WHERE id = %s', (food_id,))
    food = cur.fetchone()
    close_db_connection(conn, cur)

    form = FoodItemForm(data={'price': food[2], 'name': food[1]})
    
    if form.validate_on_submit():
        price = form.price.data
        name = form.name.data
        # do sql stuff
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE food_item SET price = %s, name = %s WHERE id = %s', (price, name, food_id))
        close_db_connection(conn, cur)
        return redirect('/restaurant/' + str(restaurant_id) + "/menu/" + str(menu_id))
    return render_template('create/create_food_item.html', form=form, heading='edit')

###################### Menu ######################
# DONE
# displays the create menu html page with the form 
@app.route('/restaurant/<int:restaurant_id>/create_menu', methods=['POST', 'GET'])
def create_menu(restaurant_id):
    form = MenuForm()
    if form.validate_on_submit():
        rtype = form.menu_type.data
        # do sql stuff
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT MAX(id) FROM menu;')
        new_id = cur.fetchone()[0] + 1
        
        cur.execute('INSERT INTO menu VALUES (%s,  %s, %s)', 
        (new_id, restaurant_id, rtype))
        close_db_connection(conn, cur)

        return redirect('/restaurant/' + str(restaurant_id))
    return render_template('create/create_menu.html', form=form)

###################### Review (no edit function needed) ######################
# DONE
# displays the create review html page with the form 
@app.route('/restaurant/<int:restaurant_id>/create_review/', methods=['POST', 'GET'])
def create_review(restaurant_id):
    form = ReviewForm()
    if form.validate_on_submit():
        # do sql stuff
        name = form.name.data
        description = form.description.data
        rating = form.rating.data

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT MAX(id) FROM review;')
        new_id = cur.fetchone()[0] + 1

        cur.execute('INSERT INTO review VALUES (%s,  %s, %s, %s, %s)', 
        (new_id, restaurant_id, name, description, rating))
        close_db_connection(conn, cur)
        return redirect('/restaurant/' + str(restaurant_id))
    return render_template('create/create_review.html', form=form)

###################### HOURS ######################
# DONE
# displays the create hours html page with the form 
@app.route('/restaurant/<int:restaurant_id>/create_hours', methods=['POST', 'GET'])
def create_hours(restaurant_id):
    form = HoursForm()
    if form.validate_on_submit():
        day_of_week = form.day_of_week.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        # do sql create stuff
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO hours VALUES (%s,  %s, %s, %s)', 
        (day_of_week, open_time, close_time, restaurant_id))
        close_db_connection(conn, cur)
        return redirect('/restaurant/' + str(restaurant_id))
    return render_template('create/create_hours.html', form=form, heading="Add")

# EDIT ROUTES are the same as create but with the forms pre populated
@app.route('/restaurant/<int:restaurant_id>/edit_hours/<string:weekday>', methods=['POST', 'GET'])
def edit_hours(restaurant_id, weekday):
  
    conn = get_db_connection()
    cur = conn.cursor()
    day_of_week = weekday
    cur.execute('SELECT * FROM hours WHERE day_of_week = %s AND fast_food_restaurant_id = %s', (day_of_week, restaurant_id))
    hour = cur.fetchone()
    close_db_connection(conn, cur)
        
    # this is how we will prepopulate the data for our forms on the frontend
    form = HoursForm(data = {'previous_day':day_of_week, 'day_of_week':day_of_week, 'open_time':hour[1], 'close_time':hour[2]})

    if form.validate_on_submit():
        new_day = form.day_of_week.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        previous_day = form.previous_day.data

        # add update sql stuff based on pervious day and restaurant id
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE hours SET day_of_week = %s, open_time = %s, close_time = %s WHERE day_of_week = %s AND fast_food_restaurant_id = %s',
         (new_day, open_time, close_time, previous_day, restaurant_id))
        close_db_connection(conn, cur)
        
        return redirect('/restaurant/' + str(restaurant_id))

    return render_template('create/create_hours.html', form=form, heading="Edit")

############# RESET ######################

@app.route('/reset')
def reset():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM fast_food_restaurant;')
    cur.execute(open("schema.sql", "r").read())
    close_db_connection(conn, cur)

    return redirect('/')


###########################################################################################################################
if __name__ == '__main__':
    app.run(debug=True)