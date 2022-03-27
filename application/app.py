from flask import Flask, render_template
import os
import psycopg2
from credentials import DB_URL

app = Flask(__name__)

# set os variable locally
#app.config['DB_URL'] = "postgresql://localhost/fastfood_db"
app.config['DB_URL'] = DB_URL

def get_db_connection():
    conn = psycopg2.connect(app.config['DB_URL'])
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

if __name__ == '__main__':
    app.run()