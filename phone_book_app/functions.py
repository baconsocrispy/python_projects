# importing python modules
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3


# import app modules
import main
import gui


def center_window(self, width, height):
  # gets user's screen dimensions
  screen_width = self.master.winfo_screenwidth()
  screen_height = self.master.winfo_screenheight()
  # calculates x & y coordinates and places window center screen
  x = int((screen_width / 2) - (width / 2))
  y = int((screen_height / 2) - (height / 2))
  center_self = self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
  return center_self

# catches if user clicks on 'X' in the top corner
def ask_quit(self):
  if messagebox.askokcancel('Exit Program', 'Okay to exit program?'):
    self.master.destroy()
    os._exit(0)

# creates the database for the app
def create_db(self):
  conn = sqlite3.connect('band_phonebook.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS band_phonebook ( \
                    id INTEGER PRIMARY KEY AUTOINCREMENT, \
                    first_name TEXT, \
                    last_name TEXT, \
                    full_name TEXT, \
                    phone TEXT, \
                    email TEXT \
                    );')
    conn.commit()
  conn.close()
  first_run(self)

# Seeds the database with one entry on creation to ensure it works properly
def first_run(self):
  data = ('David', 'Byrne', 'David Byrne', '626-578-9000', 'david.byrne@talkingheads.com')
  conn = sqlite3.connect('band_phonebook.db')
  with conn:
    cursor = conn.cursor()
    cursor, count = count_records(cursor)
    if count < 1:
      cursor.execute('INSERT INTO band_phonebook (first_name, last_name, full_name, phone, email) \
                      VALUES (?, ?, ?, ?, ?)', (data))
      conn.commit()
  conn.close()

# gets a count of the number of records in the db
def count_records(cursor):
  count = ''
  cursor.execute("""SELECT COUNT(*) FROM band_phonebook""")
  count = cursor.fetchone()[0]
  return cursor, count

# gets information from person selected in list box
def on_select(self, event):
  list = event.widget
  select = list.curselection()[0]
  value = list.get(select)
  conn = sqlite3.connect('band_phonebook.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute("""SELECT first_name, last_name, phone, email FROM band_phonebook WHERE full_name = (?)""", [value])
    body = cursor.fetchall()
    for data in body:
      self.input_first_name.delete(0, END)
      self.input_first_name.insert(0, data[0])
      self.input_last_name.delete(0, END)
      self.input_last_name.insert(0, data[1])
      self.input_phone.delete(0, END)
      self.input_phone.insert(0, data[2])
      self.input_email.delete(0, END)
      self.input_email.insert(0, data[3])

# adds a new person to the list
def add_to_list(self):
  first_name = self.input_first_name.get()
  last_name = self.input_last_name.get()
  first_name = first_name.strip()
  last_name = last_name.strip()
  first_name = first_name.title()
  last_name = last_name.title()
  full_name = ("{} {}".format(first_name, last_name))
  print('full_name: {}'.format(full_name))
  phone = self.input_phone.get().strip()
  email = self.input_email.get().strip()
  if not "@" or not "." in email:
    print('Incorrect email format')
  if (len(first_name) > 0) and (len(last_name) > 0) and (len(phone) > 0) and (len(email) > 0):
    conn = sqlite3.connect('band_phonebook.db')
    with conn:
      cursor = conn.cursor()
      cursor.execute("""SELECT COUNT(full_name) FROM band_phonebook WHERE full_name = '{}'""".format(full_name))
      count = cursor.fetchone()[0]
      check_name = count
      if check_name == 0:
        print('check_name: {}'.format(check_name))
        cursor.execute("""INSERT INTO band_phonebook (first_name, last_name, full_name, phone, email) \
                          VALUES (?, ?, ?, ?, ?)""", (first_name, last_name, full_name, phone, email))
        self.list_1.insert(END, full_name)
        on_clear(self)
      else:
        messagebox.showerror("Name Error", "'{}' already exists in the data base. Please choose another name.".format(full_name))
        on_clear(self)
    conn.commit()
    conn.close()
  else:
    messagebox.showerror("Missing Text Error", "Please ensure there is data in all four fields")

# deletes a name selected in the list box
def on_delete(self):
  select = self.list_1.get(self.list_1.curselection())
  conn = sqlite3.connect('band_phonebook.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute("""SELECT COUNT(*) FROM band_phonebook""")
    count = cursor.fetchone()[0]
    if count > 1:
      confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with {}\nWill be permanently deleted".format(select))
      if confirm:
        conn = sqlite3.connect('band_phonebook.db')
        with conn:
          cursor = conn.cursor()
          cursor.execute("""DELETE FROM band_phonebook WHERE full_name = '{}'""".format(select))
        on_deleted(self)
        conn.commit()
    else:
      confirm = messagebox.showerror("Last Record Error", "{} is the last record in the database and cannot be deleted at this time".format(select))
  conn.close()

# clears input text boxes and removes name from list box
def on_deleted(self):
  self.input_first_name.delete(0, END)
  self.input_last_name.delete(0, END)
  self.input_email.delete(0, END)
  self.input_phone.delete(0, END)
  try:
    index = self.list_1.curselection()[0]
    self.list_1.delete(index)
  except IndexError:
    pass

#  clears input text boxes
def on_clear(self):
  self.input_first_name.delete(0, END)
  self.input_last_name.delete(0, END)
  self.input_email.delete(0, END)
  self.input_phone.delete(0, END)

# refreshes the names in the list box
def on_refresh(self):
  self.list_1.delete(0, END)
  conn = sqlite3.connect('band_phonebook.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute("""SELECT COUNT(*) FROM band_phonebook""")
    count = cursor.fetchone()[0]
    i = 0
    while i < count:
      cursor.execute("""SELECT full_name FROM band_phonebook""")
      list = cursor.fetchall()[i]
      for item in list:
        self.list_1.insert(0, str(item))
        i += 1
  conn.close()

# updates phone/email info for selected person
def on_update(self):
  try:
    select = self.list_1.curselection()[0]
    value = self.list_1.get(select)
  except:
    messagebox.showinfo("Missing Selection", "No name was selected from the list box.")
    return
  phone = self.input_phone.get().strip()
  email = self.input_email.get().strip()
  if (len(phone) > 0) and (len(email) > 0):
    conn = sqlite3.connect('band_phonebook.db')
    with conn:
      cursor = conn.cursor()
      cursor.execute("""SELECT COUNT(phone) FROM band_phonebook WHERE phone = '{}'""".format(phone))
      count = cursor.fetchone()[0]
      print(count)
      cursor.execute("""SELECT COUNT(email) FROM band_phonebook WHERE email = '{}'""".format(email))
      count2 = cursor.fetchone()[0]
      print(count2)
      if count == 0 or count2 == 0:
        response = messagebox.askokcancel("Update Request", "The following changes {} and {} will be implemented for {}".format(phone, email, value))
        print(response)
        if response:
          with conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE band_phonebook SET phone = '{0}', email = '{1}' WHERE full_name = '{2}'""".format(phone, email, value))
            on_clear(self)
            conn.commit()
        else:
          messagebox.showinfo("Cancel Request", "No changes have been made to {}").format(value)
      else:
        messagebox.showinfo("No changes detected", "Both {} and {} \nalready exist in the database for this name.")
      on_clear(self)
    conn.close()
  else:
    messagebox.showerror("Missing Information", "Please select a name from the list. \nThen edit the phone or email information.")
  on_clear(self)


if __name__ == "__main__":
  pass