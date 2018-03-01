from tkinter import *
from tkinter import ttk

root = Tk()

frame = Frame(root)
labletext = StringVar()
lable = Label(frame,textvariable=labletext)
button = Button(frame,text="click me")
labletext.set("ii am label")
lable.pack()
button.pack()
frame.pack()

root.mainloop()


