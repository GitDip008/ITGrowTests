import sqlite3

# Create/connect to a SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Insert data
cursor.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', ('Alice', 'alice@example.com'))
cursor.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', ('Bob', 'bob@example.com'))
conn.commit()

# Retrieve data
cursor.execute('''SELECT * FROM users''')
rows = cursor.fetchall()
print("Retrieved data:")
for row in rows:
    print(row)

# Update data
cursor.execute('''UPDATE users SET email = ? WHERE name = ?''', ('charlie@example.com', 'Bob'))
conn.commit()

# Delete data
cursor.execute('''DELETE FROM users WHERE name = ?''', ('Alice',))
conn.commit()

# Close the connection
conn.close()

"""
Explanation for SQLite:

SQLite is used as it's lightweight, serverless, and suitable for small-scale applications.
A table 'users' is created with columns for id (primary key), name, and email.
CRUD operations are performed: Insertion, Retrieval, Update, and Deletion.

Explanation for Database Structure Choice:

For the SQL (SQLite) database,
a relational structure with tables and columns was chosen because the data has a clear structure (name and email).
"""