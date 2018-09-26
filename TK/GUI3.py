from tkinter import *

root = Tk()
Girls = ["Mary", "Mack", "Bob"]
v = []
for girl in Girls:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v)
    b.pack(anchor=W)
root.mainloop()