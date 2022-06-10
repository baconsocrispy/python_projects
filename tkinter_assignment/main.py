# copied code here per assignment

from tkinter import *

# creates basic window with no content
win1 = Tk()
win2 = Tk()

# creates buttons within window 'win1' from the Button class of tkinter
# buttons will not display until positioned
b1 = Button(win1, text='One')
b2 = Button(win1, text='Two')

b3 = Button(win1, text='Three')
b4 = Button(win1, text='Four')

b5 = Button(win1, text='Five')
b6 = Button(win1, text='Six')

b7 = Button(win1, text='Seven')
b8 = Button(win1, text='Eight')

# widget positioning using pack() geometry manager
# packing left puts items in a horizontal row starting from the left
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
# pack right arranges items horizontally starting rom the right
b3.pack(side=RIGHT, padx=10)
b4.pack(side=RIGHT, padx=10)
# pack bottom arranges items from the bottom up
b5.pack(side=BOTTOM, padx=10)
b6.pack(side=BOTTOM, padx=10)
# pack top (default), arranges items from the top down
b7.pack(side=TOP, padx=10)
b8.pack(side=TOP, padx=10)
# window will automatically collapse to the size of its content

# creates buttons within window 'win2'
btn1 = Button(win2, text='1')
btn2 = Button(win2, text='2')

# widget positioning using grid() geometry manager
# positions widgets according to rows and columns
# adds button to row 0, column 0 (top left) in 2 x 2 grid
btn1.grid(row=0, column=0)
# adds button to row 1, col 1 (bottom right) in 2 x 2 grid
btn2.grid(row=1, column=1)

# creates a text label from the Label class of tkinter
l = Label(win2, text='This is a label')
# columns will widen to accommodate wider content
l.grid(row=1, column=0)


def butt_push():
  print("button was pushed")

win3 = Tk()
# create a packable frame widget within a window via the Frame class of tkinter
f = Frame(win3)
button1 = Button(f, text='One')
button2 = Button(f, text='two')
button3 = Button(f, text='three')
# align 3 buttons in one row
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
# use the configure() method on a widget to alter its parameters after creation
button1.configure(text='Uno')
# use the Button 'command' parameter to assign actions to buttons
button2.configure(command=butt_push)
# create a label and pack it at the top of win3
l = Label(win3, text='This label is over all buttons')
# no attribute needed as TOP is default
l.pack()
# aligns the 'f' frame at the top of win3
f.pack()

# use the 'sticky' parameter with grid() to position widgets within
# container cells

win4 = Tk()

# get user-input via the Entry class from tkinter
# a variable of tkinter's StringVar() class must be set to hold the string input
v = StringVar()
# creates the Entry widget, places it on win4 and assigns the text variable per above
e = Entry(win4, textvariable = v)
# places the entry widget at the top of win4
e.pack()
# sets the text in StringVar variable that will display in the Entry widget
v.set('This is set by the program')
# retrieves the value stored in 'v'
v.get()

win5 = Tk()

# use tkinter's Listbox class to create a menu-like box to display information
# creates a listbox, places it on win5 and limits the number of display lines to 3
lb = Listbox(win5, height=3)
# places list box at the top of its container, win5
lb.pack()
# adds 4 string items to the end of the current list
lb.insert(END, 'first entry')
lb.insert(END, 'second entry')
lb.insert(END, 'third entry')
lb.insert(END, 'fourth entry')

# add a scrollbar to a list box with the Scrollbar class from tkinter
# creates and positions scrollbar
sb = Scrollbar(win5, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)
# to bind the scrollbar to the listbox use the configure method
sb.configure(command=lb.yview)
# binds the listbox to the scrollbar with the configure method
lb.configure(yscrollcommand=sb.set)
# use the 'curselection()' method on the listbox object to get the 
# current selection returned as a tuple of its index as a string
lb.curselection()

# mainloop() must be called at the end to persist the window on screen
win1.mainloop()
win2.mainloop()




