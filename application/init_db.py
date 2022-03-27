import os
import psycopg2
from credentials import DB_URL
# DB_URL = 'postgresql://localhost/fastfood_db'

# Note: DB_URL is provided by Tanner in a file called credentials.py
conn = psycopg2.connect(DB_URL)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command sql file
cur.execute(open("schema.sql", "r").read())

conn.commit()

cur.close()
conn.close()