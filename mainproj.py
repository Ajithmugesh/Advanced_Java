from tkinter import *
from functools import partial
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, ttk
import pandas

def get_selected_file_name(file_menu):
    if check1.get()==0:
        filename = file_menu.get()
        label2.config( text = filename )
    elif check1.get()==1:
        '''for file in filelist:
            f1=file
            print("\n")
            messagebox.showinfo(master,text=file)'''
        label2.config( text = filelist )
        
   
def isCheck():
    if check1.get()==1:
        optmenu.config(state=DISABLED)
    elif check1.get()==0:
        optmenu.config(state=NORMAL)

master = tk.Tk()
master.geometry('400x400')
l1 = Label(master,text="MAXVY ",fg="orange")
l1.place(x=270,y=10,anchor="center")
l1.pack()
label2 = Label(master)
#label2.place(height=30,width=1, anchor="center")
l3=Label(master)


folder = os.path.realpath(r"C:\Users\user\AppData\Local\Programs\Python\Python38-32\tem")
filelist = [fname for fname in os.listdir(folder)]
allist = [fname for fname in os.listdir(folder)]
master.title('Select a file')
optmenu = ttk.Combobox(master, values=filelist, state='readonly')
optmenu.pack(fill='x') 

check1=IntVar()
checkme = Checkbutton(master, text='Run All',variable=check1,command = isCheck,onvalue=1,offvalue=0)


button_select = tk.Button(master, text="Run",
                          width=5,
                          height=1,
                          compound=tk.CENTER,
                         command=partial(get_selected_file_name, optmenu))


checkme.pack()
button_select.pack()
label2.pack()
l3.pack()
master.mainloop()
