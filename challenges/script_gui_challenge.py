# script recreates an exact copy of GUI from lesson

# Python Version: 3.10.4

# import modules
from tkmacosx import *
from tkinter import *
import tkinter as tk


# create parent window that inherits from tkinter Frame class
class ParentWindow(Frame):
  def __init__(self, master, *args, **kwargs):
    Frame.__init__(self, highlightbackground='seagreen', highlightthickness=2)
    self.master = master
    # set window size to 500w x 200h
    self.master.geometry('{}x{}'.format(500, 180))
    self.master.resizable(False, False)
    # add title to window, including feather emoji
    self.master.title('\U0001FAB6 Check Files')
    
    load_gui_content(self)

# create and position widgets for the master window
def load_gui_content(frame):
  frame.btn_browse_1 = Button(frame.master, text='Browse...')
  frame.btn_browse_1.grid(row=0, column=0, padx=15, pady=(30, 0), ipadx=21)

  frame.btn_browse_2 = Button(frame.master, text='Browse...')
  frame.btn_browse_2.grid(row=1, column=0, padx=15, pady=7, ipadx=21)

  frame.btn_check_files = Button(frame.master, text='Check for files...')
  frame.btn_check_files.grid(row=2, column=0, padx=15, pady=0, ipady=10)

  frame.btn_check_files = Button(frame.master, text='Close Program')
  frame.btn_check_files.grid(row=2, column=1, padx=15, pady=0, ipady=10, sticky=E)

  frame.input_1 = Entry(frame.master)
  frame.input_1.grid(row=0, column=1, padx=15, pady=(30, 0), ipadx=55)

  frame.input_2 = Entry(frame.master)
  frame.input_2.grid(row=1, column=1, padx=15, pady=(7, 0), ipadx=55)

if __name__ == "__main__":
  root = Tk()
  app = ParentWindow(root)
  app.mainloop()