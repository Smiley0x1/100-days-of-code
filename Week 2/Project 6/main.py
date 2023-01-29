from tkinter import *
from tkinter import ttk
import network
import scan
#logic

def run():
    '''scan.main()
    network.main()'''
    
#title and launch of application
root = Tk()
root.title("Scanners")

#spaces elements
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
run()