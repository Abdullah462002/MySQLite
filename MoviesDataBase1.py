import sqlite3

connection = sqlite3.connect("myDatabase.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Movies")

# Print the Records from Movies Table

data = cursor.fetchall()

for Row in data:
    print("")
    for record in range(len(Row)):
        print(Row[record], end=" | ")