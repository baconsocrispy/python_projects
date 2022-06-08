# import tkinter
from tkinter import *
import tkinter as tk

# import app modules
import main
import functions

def load_gui(self):
  # creates and positions the labels for inputs
  self.lbl_first_name = tk.Label(self.master, text='First Name:')
  self.lbl_first_name.grid(row=0, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)
  self.lbl_last_name = tk.Label(self.master, text='Last Name:')
  self.lbl_last_name.grid(row=2, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)
  self.lbl_phone = tk.Label(self.master, text='Phone Number:')
  self.lbl_phone.grid(row=4, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)
  self.lbl_email = tk.Label(self.master, text='Email:')
  self.lbl_email.grid(row=6, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)
  self.lbl_user = tk.Label(self.master, text='User:')
  self.lbl_user.grid(row=0, column=2, padx=(0, 0), pady=(10, 0), sticky=N+W)

  # creates inputs for user info
  self.input_first_name = tk.Entry(self.master, text='')
  self.input_first_name.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N+E+W)
  self.input_last_name = tk.Entry(self.master, text='')
  self.input_last_name.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N+E+W)
  self.input_phone = tk.Entry(self.master, text='')
  self.input_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N+E+W)
  self.input_email = tk.Entry(self.master, text='')
  self.input_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30, 40), pady=(0, 0), sticky=N+E+W)

  # creates a list box and scroll bar and places them on the master frame
  self.scrollbar_1 = Scrollbar(self.master, orient=VERTICAL)
  self.list_1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar_1.set)
  self.list_1.bind('<<ListboxSelect>>', lambda event: functions.on_select(self, event))
  self.scrollbar_1.config(command=self.list_1.yview)
  self.scrollbar_1.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0, 0), pady=(0, 0), sticky=N+E+S)
  self.list_1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=N+E+S+W)
  
  # creates and places buttons on master frame
  self.btn_add = tk.Button(self.master, width=12, height=2, text='Add', command=lambda: functions.add_to_list(self))
  self.btn_add.grid(row=8, column=0, padx=(25, 0), pady=(45, 10), sticky=W)
  self.btn_update = tk.Button(self.master, width=12, height=2, text='Update', command=lambda: functions.on_update(self))
  self.btn_update.grid(row=8, column=1, padx=(15, 0), pady=(45, 10), sticky=W)
  self.btn_delete = tk.Button(self.master, width=12, height=2, text='Delete', command=lambda: functions.on_delete(self))
  self.btn_delete.grid(row=8, column=2, padx=(15, 0), pady=(45, 10), sticky=W)
  self.btn_close = tk.Button(self.master, width=12, height=2, text='Close', command=lambda: functions.ask_quit(self))
  self.btn_close.grid(row=8, column=4, padx=(15, 0), pady=(45, 10), sticky=E)

  functions.create_db(self)
  functions.on_refresh(self)

  if __name__ == "__main__":
    pass