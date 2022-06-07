import sqlite3

# variable holds connection to sqlite3 database
conn = sqlite3.connect('test.db')

# cursor() function gets set to a variable 
# call execute() on that variable to send commands to the database
with conn:
  cursor = conn.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS persons ( \
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
    fname TEXT, \
    lname TEXT, \
    email TEXT \
    )')
  conn.commit()
conn.close()

# conn = sqlite3.connect('test.db')
# with conn:
#   cursor = conn.cursor()
#   cursor.execute('INSERT INTO persons (fname, lname, email) \
#     VALUES (?, ? , ?)', ('Tina', 'Weymouth', 'Tina.Weymouth@talkingheads.com'))
#   cursor.execute('INSERT INTO persons (fname, lname, email) \
#     VALUES (?, ? , ?)', ('Chris', 'Frantz', 'Chris.Frantz@talkingheads.com'))
#   cursor.execute('INSERT INTO persons (fname, lname, email) \
#     VALUES (?, ? , ?)', ('Jerry', 'Harrison', 'Jerry.Harrison@talkingheads.com'))
#   conn.commit()
# conn.close()

conn = sqlite3.connect('test.db')
with conn:
  cursor = conn.cursor()
  cursor.execute('SELECT fname, lname, email FROM persons WHERE fname = "Tina"')
  head = cursor.fetchall()
  for data in head:
    msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(data[0], data[1], data[2])
  print(msg)
