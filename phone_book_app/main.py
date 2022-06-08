# Python Version: 3.10.4
# Author: Carter Bacon
# Purpose: Learning Tkinter & SQLite3 DB integration

# module importation
from tkinter import *
# from tkinter import messagebox
import tkinter as tk

import gui
import functions

class ParentWindow(Frame):
  def __init__(self, master, *args, **kwargs):
    Frame.__init__(self, master, *args, **kwargs)

    # define master frame configuration
    self.master = master
    self.master.minsize(1000, 500) 
    self.master.maxsize(1000, 500)
    # center_window centers app on user's screen
    functions.center_window(self, 500, 300)
    # sets the title in the window header bar
    self.master.title('Band Phonebook')
    # sets background color of master frame
    self.master.configure(bg='seagreen')
    # built-in tkinter protocal method catches if user clicks close button 'X'
    self.master.protocol("WM_DELETE_WINDOW", lambda: functions.ask_quit(self))
    arg = self.master
    # load GUI widgets from the GUI module
    gui.load_gui(self)

if __name__ == "__main__":
  root = tk.Tk()
  App = ParentWindow(root)
  # keeps the window open and persisted on screen
  root.mainloop()