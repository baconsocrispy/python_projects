from tkinter import *
from tkinter.filedialog import askdirectory

import functions

class ParentWindow(Frame):
  def __init__(self, master, *args, **kwargs):
    Frame.__init__(self)
    self.master = master 
    self.master.title("\U0001FAB6 Transfer Modified Files")
    self.master.geometry("{}x{}".format(500, 150))
    self.master.resizable(False, False)
    # source folder input widgets
    self.btn_source = Button(self.master, text="Source", command=lambda: get_folder(self.source_input))
    self.btn_source.grid(row=0, column=0, pady=(17.5, 0), padx=15, ipadx=13)
    self.source_input = Entry(self.master)
    self.source_input.grid(row=0, column=1, pady=(17.5, 0), padx=15, ipadx=70)
    # destination folder input widgets
    self.btn_destination = Button(self.master, text="Destination", command=lambda: get_folder(self.destination_input))
    self.btn_destination.grid(row=1, column=0, pady=(15, 0), padx=15)
    self.destination_input = Entry(self.master)
    self.destination_input.grid(row=1, column=1, pady=(15, 0), padx=15, ipadx=70)
    # transfer files button
    self.btn_transfer = Button(self.master, text="Transfer", command=lambda: transfer_files())
    self.btn_transfer.grid(row=2, column=0, pady=(15, 0), padx=15, ipadx=9)
    # launches directory dialog box and updates input fields
    def get_folder(entry_widget):
      directory = askdirectory(mustexist=True)
      entry_widget.delete(0, END)
      entry_widget.insert(0, directory)
    # gets file path info from inputs and executes transfer
    def transfer_files():
      a = self.source_input.get()
      b = self.destination_input.get()
      functions.transfer_modified_files(a, b)

if __name__ == "__main__":
  root = Tk()
  app = ParentWindow(root)
  app.mainloop()