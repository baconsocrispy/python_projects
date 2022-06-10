from tkinter import *
import tkinter as tk
from tkmacosx import *

import functions
import main


# create and position labels
def load_gui(self):
  self.lbl_first_name = Label(self.master, text='First Name:')
  self.lbl_first_name.grid(row=0, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.lbl_last_name = Label(self.master, text='Last Name:')
  self.lbl_last_name.grid(row=2, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.lbl_phone = Label(self.master, text='Phone:')
  self.lbl_phone.grid(row=4, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.lbl_email = Label(self.master, text='Email:')
  self.lbl_email.grid(row=6, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.lbl_current_course = Label(self.master, text='Current Course')
  self.lbl_current_course.grid(row=8, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  
  # create and position inputs
  self.input_first_name = Entry(self.master, text='')
  self.input_first_name.grid(row=1, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.input_last_name = Entry(self.master, text='')
  self.input_last_name.grid(row=3, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.input_phone= Entry(self.master, text='')
  self.input_phone.grid(row=5, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.input_email = Entry(self.master, text='')
  self.input_email.grid(row=7, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.input_current_course = Entry(self.master, text='')
  self.input_current_course.grid(row=9, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)

  # create and position list box and scroll-bar
  self.list_scrollbar = Scrollbar(self.master, orient=VERTICAL)
  self.student_list = Listbox(self.master, width=40, exportselection=0, yscrollcommand=self.list_scrollbar.set)
  self.list_scrollbar.config(command=self.student_list.yview)
  self.list_scrollbar.grid(row=1, column=6, rowspan=7, columnspan=1, padx=(0, 0), pady=(0, 0), sticky=NS)
  self.student_list.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0, 0), pady=(0, 0), sticky=N+E+S+W)

  # create submit button 
  self.btn_submit = Button(self.master, text='Add', command=lambda: functions.add_student(self), borderless=1)
  self.btn_submit.grid(row=11, column=1, padx=(15, 0), pady=(15, 0), sticky=EW)

  # create a delete button
  self.btn_submit = Button(self.master, text='Delete', command=lambda: functions.delete_student(self), borderless=1)
  self.btn_submit.grid(row=11, column=2, padx=(15, 0), pady=(15, 0), sticky=EW)

  functions.on_refresh(self)

if __name__ == "__main__":
  pass