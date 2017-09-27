import tkinter
def callback():
    var.set("hhhhhhha")
root = tkinter.Tk()
frame1=tkinter.Frame(root)
frame2=tkinter.Frame(root)
var = tkinter.StringVar()
var.set("wtffffffff")
textLabel = tkinter.Label(frame1, textvariable =var, justify =LEFT)
root.title("hello world")
table = tkinter.Label(root, text="hello world")
table.pack()
root.mainloop()
