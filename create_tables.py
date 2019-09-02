import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#INTEGER PRIMARY KEY - automatic increament
create_teable = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_teable)

create_teable = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_teable)


connection.commit()
connection.close()

