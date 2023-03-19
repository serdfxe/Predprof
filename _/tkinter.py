from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Алькубьерре 3")

mainframe = ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)


task_lenght = IntVar()
remain_SH = IntVar()
remain_AF = IntVar()


window.mainloop()
