# code copied from SQLite3 assignment

import sqlite3

conn = sqlite3.connect('testdb.db')

c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS people (first_name TEXT, last_name TEXT, age INT);')

conn.close()

# utilize the with keyword to shorten code, and better manage exceptions
with sqlite3.connect('testdb.db') as conn:
  c = conn.cursor() 
  c.execute("""INSERT INTO people VALUES ('Jang', 'Ping', 22);""")
conn.close()

# use executescript for multiple sql statements
with sqlite3.connect('testdb.db') as conn:
  c = conn.cursor()
  c.executescript("""DROP TABLE IF EXISTS people;
                     CREATE TABLE people (
                     first_name TEXT,
                     last_name TEXT,
                     age INT);
                     INSERT INTO people VALUES('Ron', 'Obvious', '42')""")

# use executemany to insert many tuples at once
people = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
with sqlite3.connect('testdb.db') as conn:
  c = conn.cursor()
  c.executemany("INSERT INTO people VALUES(?, ?, ?)", people)

# best practice to use ? placeholders and insert user info 
# as a tuple to avoid errors or sql injection attacks

# use cursor.fetchall() to get all results from query
with sqlite3.connect('testdb.db') as conn:
  c = conn.cursor()
  c.execute('SELECT first_name, last_name FROM people WHERE age > 30')
  for row in c.fetchall():
    print(row) #returns each row as a tuple
  
  # cursor.fetchone() gets a single row from the query results
  c.execute('SELECT first_name, last_name FROM people WHERE age > 20')
  while True:
    row = c.fetchone()
    if row is None:
      break
    print(row)

