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

cur.execute("INSERT INTO comments (post_id, content) VALUES (?, ?)",
            (1, 'text for second comment')
            )

cur.execute("INSERT INTO comments (post_id, content) VALUES (?, ?)",
            (1, 'text for second comment')
            )

cur.execute("INSERT INTO comments (post_id, content) VALUES (?, ?)",
            (2, 'text for third comment')
            )

cur.execute("INSERT INTO comments (post_id, content) VALUES (?, ?)",
            (1, 'fawefawefewfawef')
            )

connection.commit()
connection.close()