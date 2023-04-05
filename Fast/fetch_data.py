import sqlite3

def get_db_data(query):
    # Connect to the database
    conn = sqlite3.connect('Database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve data from a table
    cursor.execute(query)

    my_list=[]
    # Fetch the results and print them
    results = cursor.fetchall()
    for row in results:
        my_list.append(list(row))

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return my_list
