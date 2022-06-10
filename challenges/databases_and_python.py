# Requirements
# 1. create a database in RAM named 'roster' that includes
#    fields 'name', 'species', 'iq'
# 2. populate the table with the following:
#     a. Jean-Baptiste Zorg, Human, 122
#     b. Korben Dallas, Meat Popcicle, 100
#     c. Ak'not, Mangalore, -5
# 3. update the species of Korban Dallas to be Human
# 4. display the names and iqs of everyone in the table who is human

# import sqlite3
import sqlite3

# creates the roster db
def create_roster_db():
  with sqlite3.connect('roster.db') as conn:
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS roster ( \
               id INTEGER PRIMARY KEY AUTOINCREMENT, \
               name TEXT, \
               species TEXT, \
               iq INT \
               );')
# adds element to roster
def add_to_roster(name, species, iq):
  create_roster_db()
  with sqlite3.connect('roster.db') as conn:
    c = conn.cursor()
    c.execute('INSERT INTO roster (name, species, iq) \
               VALUES (?, ?, ?)', (name, species, iq))

# displays names & iqs of humans
def display_humans():
  with sqlite3.connect('roster.db') as conn:
    c = conn.cursor()
    c.execute("SELECT name, iq FROM roster WHERE species = 'human'")
    humans = c.fetchall()
    for human in humans:
      print('{} has an iq of {}'.format(human[0], human[1]))

if __name__ == "__main__":
  add_to_roster('zorg', 'human', 122)
  add_to_roster('korben', 'meat popsicle', 100)
  add_to_roster('ak\'not', 'mangalore', -5)

  # update korben species to human
  with sqlite3.connect('roster.db') as conn:
    c = conn.cursor()
    c.execute("UPDATE roster SET species = 'human' WHERE name = 'korben';")
  
  display_humans()

