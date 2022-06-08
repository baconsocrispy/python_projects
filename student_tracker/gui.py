from tkinter import *
import tkinter as tk

# create and position labels
def load_gui(self)
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
  self.input_first_name = tk.Entry(self.master, text='')
  self.input_first_name.grid(row=1, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.input_last_name = tk.Entry(self.master, text='')
  self.input_last_name.grid(row=3, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.input_phone= tk.Entry(self.master, text='')
  self.input_phone.grid(row=5, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.input_email = tk.Entry(self.master, text='')
  self.input_email.grid(row=7, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)
  self.input_current_course = tk.Entry(self.master, text='')
  self.input_current_course.grid(row=9, column=0, padx=(15, 0), pady=(15, 0), sticky=EW)

  # create submit button
  self.btn_submit = tk.Button(self.master, text='Add', command=lambda: functions.add_student(self))
  self.btn_submit.grid(row=11, column=1, padx=(15, 0), pady=(15, 0), sticky=EW)



