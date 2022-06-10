# create a Python script that will automatically generate an html file
# the script should open the file in a new tab
# a tkinter GUI should allow users to enter and update the html body text

from tkinter import *
import tkinter as tk
import web_page_generator

class ParentWindow(Frame):
  def __init__(self, master, *args, **kwargs):
    Frame.__init__(self)
    # initializes master from and sizes it
    self.master = master
    self.master.geometry("{}x{}".format(500, 150))
    self.master.resizable(False, False)
    # creates and positions entry label
    self.lbl_text_entry = Label(self.master, text='Enter New Text:')
    self.lbl_text_entry.grid(row=0, column=0, pady=(30, 0), padx=15)
    # creates and positions text entry
    self.input_text = Entry(self.master)
    self.input_text.grid(row=0, column=1, pady=(30, 0), padx=15)
    # creates and positions update button
    self.btn_update = Button(self.master, text='Update:', command=lambda: web_page_generator.write_and_open('./html/main.html', self.get_text()))
    self.btn_update.grid(row=1, column=1, pady=(15, 0), padx=15, sticky=W)

  # helper to grab text from text entry
  def get_text(self):
    text = self.input_text.get()
    return text

if __name__ == "__main__":
  root = Tk()
  app = ParentWindow(root)
  app.mainloop()

