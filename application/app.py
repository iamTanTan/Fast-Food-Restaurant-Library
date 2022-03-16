from flask import Flask, render_template
import os
import psycopg2

app = Flask(__name__)

# set os variable locally
DB_URL = os.eviron['DATABASE_URL']

def get_db_connection():
    conn = psycopg2.connect(DB_URL)
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run()