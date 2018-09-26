from tkinter import  *

root = Tk()
root.title("hello world")
v = IntVar()
Radiobutton(root, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Two", variable=v, value=2).pack(anchor=W)
Radiobutton(root, text="Three", variable=v, value=3).pack(anchor=W)
l = Label(root, textvariable=v)
l.pack()
root.mainloop()
