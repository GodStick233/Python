from tkinter import *
root = Tk()
group = LabelFrame(root, text="hello world", padx=5, pady=5)
group.pack(padx=10, pady=10)
LANGS =[
    ("Lua", 1),
    ("Java", 2),
    ("Python", 3),
    ("C++", 4),
]
v = IntVar()
for lang,num in LANGS :
    b = Radiobutton(group, text=lang, variable=v, value=num)
    b.pack(anchor=W)
root.mainloop()
