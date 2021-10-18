#!/usr/bin/env python3

'''
import sys
import pyvisa as visa 
#import tkinter as tk
#import tkinter.ttk as ttk
import pyvisa
#import visa 
#import time
rm=visa.ResourceManager("@py")
#rm=visa.ResourceManager()
#rm=pyvisa.get_instruments_list()
print("tHE DEVICES ARE")
print(rm.list_resources_info())
#usb = filter(lambda x: 'USB' in x, rm)

'''
import pyvisa as visa
rm = visa.ResourceManager('@py')
print(rm.list_resources())
'''
fen1=tk.Tk()
fen1.title("Test")
fen1.geometry("400x400")
fen1.after(5000,fen1.destroy)
tex1=tk.Label(fen1,text="Hello World", fg="red", bg="blue", padx=10, pady=10)
# put text in left
tex1.pack(side=tk.LEFT)
# PUt button
bout1=tk.Button(fen1,text="Quit", command=fen1.destroy)
bout1.pack(side=tk.RIGHT)


# Add combobox 
combo1=tk.ttk.Combobox(fen1, textvariable=tk.StringVar())
combo1.pack(side=tk.LEFT)


tex1.pack()




fen1.mainloop()
'''