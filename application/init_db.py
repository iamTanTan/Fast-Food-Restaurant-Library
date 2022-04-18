import environ
import psycopg2
from credentials import DB_URL
# DB_URL = 'postgresql://localhost/fastfood_db'

env = environ.Env()
if env.get('DATABASE_URL') is not None:
    DB_URL = env.get('DATABASE_URL')
# Note: DB_URL is provided by Tanner in a file called credentials.py
print(DB_URL)
conn = psycopg2.connect(DB_URL)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command sql file
cur.execute(open("schema.sql", "r").read())

conn.commit()

cur.close()
conn.close()