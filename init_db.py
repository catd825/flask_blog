import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
    
cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Third post', 'Content for the third post')
            )

cur.execute("INSERT INTO comments (post_id, content) VALUES (?, ?)",
            (1, 'first comment for first post')
            )

cur.execute("INSERT INTO comments (post_id, content) VALUES (?, ?)",
            (1, 'second comment for first post')
            )

cur.execute("INSERT INTO comments (post_id, content) VALUES (?, ?)",
            (2, 'first comment for second post')
            )

cur.execute("INSERT INTO comments (post_id, content) VALUES (?, ?)",
            (1, 'third comment for first post')
            )

connection.commit()
connection.close()