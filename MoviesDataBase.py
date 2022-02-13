#importing sqlite to connect database
import sqlite3

#Creating new SQLite database
connection = sqlite3.connect("myDatabase.db")

cursor = connection.cursor()

#creating a new table (Movies)
myQuery_1 = ''' CREATE TABLE Movies(
                  Movie Name TEXT,
                  Actor TEXT,
                  Actress TEXT,
                  Director TEXT,
                  ReleaseYear TEXT
                  );
            '''
# Execute the Query
cursor.execute(myQuery_1)

# Records
Records=[ ("Iron Man 1"                        ,"Robert Downey Jr","Gwyneth Paltrow","Jon Favreau"    ,"2008"),
          ("The Incredible Hulk"               ,"Edward Norton"   ,"Liv Tyler"      ,"Louis Leterrier","2008"),
          ("Iron Man 2"                        ,"Robert Downey Jr","Gwyneth Paltrow","Jon Favreau"    ,"2010"),
          ("Thor"                              ,"Chris Hemsworth" ,"Natalie Portman","Kenneth Branagh","2011"),
          ("Captain America: The First Avenger","Chris Evans"     ,"Hayley Atwell"  ,"Joe Johnston"   ,"2011") ]

# Query to Inserting data into Movies Table
cursor.executemany('INSERT INTO Movies VALUES(?,?,?,?,?);',Records);

connection.commit()
connection.close()