# Assignment Requirements
# 1. a page title labeled 'Student Tracking'
# 2. A form to submit student info:
#   inputs: first name, last name, phone, email,
#           current course, submit button
# 3. a section that displays students & above info
# 4. a delete button that deletes selected student

# import python modules
from tkinter import *
import tkinter as tk
import sqlite3 

# import app modules
import functions.py

class ParentWindow(Frame):
  def __init__(self, master)
    Frame.__init__(self, master)
    self.master = master
    self.master.minsize = (700, 500)
    self.master.maxsize = (700, 500)
    self.master.title('Student Tracker')
    self.master.configure(bg="seagreen")
    self.master.protocol("WM_DELETE_WINDOW", lambda: functions.ask_quit(self))
    arg = self.master
    gui.load_gui(self)

if __name__ == "__main__":
root = tk.Tk()
app = ParentWindow(root)
root.mainloop()