import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')

# Open and read the SQL file
with open('new_db.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

conn.executescript(sql_script)

conn.commit()
conn.close()
