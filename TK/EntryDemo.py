from tkinter import *

root = Tk()
Label(root, text="ID:").grid(row=0)
Label(root, text="Password:").grid(row=1)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    print("ID:%s" % e1.get())
    print("password: % s" % e2.get())
    e1.delete(0, END)
    e2.delete(0, END)


Button(root, text="OK", width=10 ,command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="Exit", width=10, command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)
root.mainloop()



