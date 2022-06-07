# Requirements:
# 1.  Script must use Python3 & sqlite3 module
# 2.  DB requires 2 fields: autoincrement primary int & string field
# 3.  Script must read from filelist and determine which are .txts
# 4.  It should add .txts to database in string column
# 5.  It should print (legibly) the text files to the console
# 6.  Add comments throughout

# Python3 Version: 3.10.4
# SQLite3 Version: 3.32.3

# import sqlite3 & os module
import sqlite3
import os

# main program function
def get_store_and_print_txts_from_folder(target_folder):
  create_txt_table()
  path = folder_path(target_folder)
  txts = get_txts(path)
  add_txts_to_db(txts)
  print_txts(txts)

# create 2 column table to store file names
def create_txt_table():
  conn = sqlite3.connect('db_assign.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS txt_files ( \
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
                    txt_file TEXT)')
    conn.commit()
  conn.close()

# create path for target folder
def folder_path(target_folder):
  abs_path = os.path.abspath(target_folder)
  return abs_path

# finds .txt files and returns them as tuple
def get_txts(path):
  txts = []
  all_files = os.listdir(path)
  for file in all_files:
    if '.txt' in file:
      txts.append(file)
  return tuple(txts)

# function to add txt file_names to database
def add_txts_to_db(txts):
  for txt in txts:
    insert_txt(txt)

# function excutes SQL insertion
def insert_txt(txt):
  conn = sqlite3.connect('db_assign.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO txt_files (txt_file) \
                    VALUES (?)', (txt,))
    conn.commit()
  conn.close()

# iterates through tuple of txts and prints each one
def print_txts(txts):
  for txt in txts:
    print(txt)

if __name__ == "__main__":
  get_store_and_print_txts_from_folder('txts')