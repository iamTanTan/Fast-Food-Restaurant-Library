from flask import Flask, render_template
import os
import psycopg2
from credentials import DB_URL

app = Flask(__name__)

# set os variable locally
#app.config['DB_URL'] = "postgresql://localhost/fastfood_db"
app.config['DB_URL'] = DB_URL

print(app.config)

def get_db_connection():
 
    conn = psycopg2.connect(app.config['DB_URL'])
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