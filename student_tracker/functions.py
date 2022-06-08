from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

import gui
import main

# create the database
def create_db(self):
  conn = sqlite3.connect('students.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS students ( \
                    id INTEGER PRIMARY KEY AUTOINCREMENT, \
                    first_name TEXT, \
                    last_name TEXT, \
                    phone TEXT, \
                    email TEXT, \
                    current_course TEXT \
                    );')
    conn.commit()
  conn.close()

# add student to database
def add_student(self):
  create_db(self)
  first_name = self.input_first_name.get()
  last_name = self.input_last_name.get()
  first_name = first_name.strip()
  last_name = last_name.strip()
  first_name = first_name.title()
  last_name = last_name.title()
  phone = self.input_phone.get()
  email = self.input_email.get()
  current_course = self.input_current_course.get()
  formatted = "{}, {}: {} ({}/{})".format(last_name, first_name, current_course, phone, email)
  if (len(first_name) > 0) and (len(last_name) > 0) and (len(phone) > 0) and (len(email) > 0) and (len(current_course) > 0):
    conn = sqlite3.connect('students.db')
    with conn:
      cursor = conn.cursor()
      cursor.execute("""INSERT INTO students (first_name, last_name, phone, email, current_course) \
                        VALUES (?, ?, ?, ?, ?)""", (first_name, last_name, phone, email, current_course))
      self.student_list.insert(END, formatted)
      on_clear(self)
      conn.commit()
    conn.close()
  else:
    messagebox.showerror('Missing Text', 'All inputs must contain information')
  on_refresh(self)

def delete_student(self):
  select = self.student_list.get(self.student_list.curselection())
  email_extract = select.split('/')[-1]
  email_clean = email_extract[0:-1]
  print(email_clean)
  conn = sqlite3.connect('students.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM students WHERE email = '{}';""".format(email_clean))
    conn.commit()
  conn.close()
  on_refresh(self)

def ask_quit(self):
  if messagebox.askokcancel('Exit Program', 'Okay to exit?'):
    self.master.destroy()
    os._exit(0)

# resets inputs
def on_clear(self):
  self.input_first_name.delete(0, END)
  self.input_last_name.delete(0, END)
  self.input_phone.delete(0, END)
  self.input_email.delete(0, END)
  self.input_current_course.delete(0, END)

def on_refresh(self):
  self.student_list.delete(0, END)
  conn = sqlite3.connect('students.db')
  with conn:
    cursor = conn.cursor()
    cursor.execute("""SELECT COUNT(*) FROM students""")
    count = cursor.fetchone()[0]
    i = 0
    while i < count:
      cursor.execute("""SELECT * FROM students""")
      student = cursor.fetchall()[i]
      formatted = "{}, {}: {} ({}/{})".format(student[2], student[1], student[5], student[3], student[4])
      self.student_list.insert(0, formatted)
      i += 1
  conn.close()




if __name__ == "__main__":
  pass