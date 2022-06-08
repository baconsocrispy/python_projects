# Assignment Requirements
# 1. a page title labeled 'Student Tracking'
# 2. A form to submit student info:
#   inputs: first name, last name, phone, email,
#           current course, submit button
# 3. a section that displays students & above info
# 4. a delete button that deletes selected student

# This minimal exercise allows for inputting student info and
# adding it to a database via a tkinter GUI

# import python modules
from tkinter import *
import tkinter as tk

# import app modules
import functions
import gui

class ParentWindow(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.master = master
    self.master.geometry('{}x{}'.format(800, 500))
    self.master.title('Student Tracker')
    self.master.configure(bg="seagreen")
    self.master.protocol("WM_DELETE_WINDOW", lambda: functions.ask_quit(self))
    gui.load_gui(self)

if __name__ == "__main__":
  root = tk.Tk()
  app = ParentWindow(root)
  root.mainloop()