from tkinter import *

root = Tk()
root.geometry("400x400")

mb = Menubutton(root, text="This is a menu")
mb.menu = Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label = "option 1", command=lambda: print("This is option 1"))
mb.menu.add_command(label = "option 2", command=lambda: print("This is option 2"))
mb.menu.add_command(label = "option 3", command=lambda: print("This is option 3"))
mb.menu.add_command(label = "option 4", command=lambda: print("This is option 4"))

mb.pack()



root.mainloop()