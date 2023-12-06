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
