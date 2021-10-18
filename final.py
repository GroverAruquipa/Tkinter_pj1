from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import numpy as np
import tkinter as tk
import tkinter as ttk
import tkinter.ttk as ttk


class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Plotting")
        self.geometry("1500x800")
        self.resizable(False, False)
        self.configure(bg = "white")
        
        
        


        ## COnfigurartion graphs
        fig = Figure(figsize = (8, 6), 
                 dpi = 100) 
       

        
    
        y = [i**2 for i in range(101)] 
  
    
        #plot1 = fig.add_subplot(111) 
        # Change tittle fig 
        
        plot1 = fig.add_subplot(2, 1, 1)
    
        plot1.plot(y) 

        x = np.array([0, 1, 2, 3])
        y = np.array([10, 20, 30, 40])
        
        plot1.set_title('Amplitude')
        plot1 = fig.add_subplot(2, 1, 2)
        plot1.set_title('Phase')
        plot1.plot(x,y)
        
        #Labelframe1
        self.labelFrame1 = LabelFrame(self, text = "Plotting", font = ("arial", 11, "bold"), bg = "red", fg = "black", width = 300, height = 750)
        self.labelFrame1.grid(row = 0, column = 0, padx=5, pady=10)

        #Labelframe2
        self.labelFrame2 = LabelFrame(self, text = "Bode Plot", font = ("arial", 15, "bold"), bg = "white", fg = "black", width = 800, height = 750)
        self.labelFrame2.grid(row = 0, column = 1, padx=5, pady=10)
        #################Controllerrs##################33
        ## add combobox
        ##Add label
        self.label1 = Label(self.labelFrame1, text = "Frequency base", font = ("arial", 10, "italic"), bg = "white", fg = "black")
        self.label1.place(x = 50, y = 40)
        self.combofreq = ttk.Combobox(self, text="Select Frequency", state="readonly")
        self.combofreq['values'] = ("10Hz", "100Hz", "50Hz", "1000Hz", "2000Hz")
        self.combofreq.current(0)
        #CHange size combobox
        self.combofreq.config(width = 10)
        self.combofreq.place(x = 180, y = 70) ### ITS IS CHANGING 30 PIXELES
        ##Add label
        self.label2 = Label(self.labelFrame1, text = "Decades", font = ("arial", 10, "italic"), bg = "white", fg = "black")
        self.label2.place(x = 50, y = 80)
        ##Add combobox
        self.combodec = ttk.Combobox(self, text="Select Decades", state="readonly")
        self.combodec['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        self.combodec.current(0)
        #CHange size combobox
        self.combodec.config(width = 10)
        self.combodec.place(x = 180, y = 110) ### ITS IS CHANGING 30 PIXELES
        ##Add label
        self.label3 = Label(self.labelFrame1, text = "Nropoints/decade", font = ("arial", 10, "italic"), bg = "white", fg = "black")
        self.label3.place(x = 50, y = 120)
        ##Add combobox
        self.combopoints = ttk.Combobox(self, text="Select Nropoints/decade", state="readonly")
        self.combopoints['values'] = ("10", "20", "30", "40", "50", "60", "70", "80", "90", "100")
        self.combopoints.current(0)
        #CHange size combobox
        self.combopoints.config(width = 10)
        self.combopoints.place(x = 180, y = 150) ### ITS IS CHANGING 30 PIXELES
        ## add button demand
        self.button1 = Button(self.labelFrame1, text = "Demand", font = ("arial", 10, "bold"), bg = "white", fg = "black")
        self.button1.place(x = 180, y = 170)
        ## Add label
        self.label4 = Label(self.labelFrame1, text = "Frequency1", font = ("arial", 10, "italic"), bg = "white", fg = "black")
        self.label4.place(x = 50, y = 250)
        #Add spinbox
        self.freq1 = Spinbox(self.labelFrame1, from_ = 0, to = 100, width = 10)
        self.freq1.place(x = 180, y = 250)
        ## Add label 2
        self.label5 = Label(self.labelFrame1, text = "Frequency2", font = ("arial", 10, "italic"), bg = "white", fg = "black")
        self.label5.place(x = 50, y = 280)
        #Add spinbox
        self.freq2 = Spinbox(self.labelFrame1, from_ = 0, to = 100, width = 10)
        self.freq2.place(x = 180, y = 280)
        ## add label nro points
        self.label6 = Label(self.labelFrame1, text = "Nropoints", font = ("arial", 10, "italic"), bg = "white", fg = "black")
        self.label6.place(x = 50, y = 310)
        #Add combobox
        self.combopoints2 = ttk.Combobox(self, text="Select Nropoints", state="readonly")
        self.combopoints2['values'] = ("10", "20", "30", "40", "50", "60", "70", "80", "90", "100")
        self.combopoints2.current(0)
        #CHange size combobox
        self.combopoints2.config(width = 10)
        self.combopoints2.place(x = 180, y = 340) ### ITS IS CHANGING 30 PIXELES

        ## add button demand2
        self.button2 = Button(self.labelFrame1, text = "Demand2", font = ("arial", 10, "bold"), bg = "white", fg = "black")
        self.button2.place(x = 180, y = 370)
        #############COnnection section################
        ##Add label
        self.label7 = Label(self.labelFrame1, text = "Generator", font = ("arial", 10, "italic"), bg = "white", fg = "black")
        self.label7.place(x = 50, y = 450)
        ##Add combobox
        self.combogen = ttk.Combobox(self, text="Select Generator", state="readonly")
        self.combogen['values'] = ("test")
        self.combogen.current(0)
        #CHange size combobox
        self.combogen.config(width = 10)
        self.combogen.place(x = 180, y = 480) ### ITS IS CHANGING 30 PIXELES

        ##Add label Generator
        self.label8 = Label(self.labelFrame1, text = "Generator", font = ("arial", 10, "italic"), bg = "white", fg = "black")
        self.label8.place(x = 50, y = 480)
        ##Add combobox
        self.combogen2 = ttk.Combobox(self, text="Select Generator", state="readonly")
        self.combogen2['values'] = ("test")
        self.combogen2.current(0)
        #CHange size combobox
        self.combogen2.config(width = 10)
        self.combogen2.place(x = 180, y = 510) ### ITS IS CHANGING 30 PIXELES
        ## Add button connect
        self.button3 = Button(self.labelFrame1, text = "Connect", font = ("arial", 10, "bold"), bg = "white", fg = "black")
        self.button3.place(x = 180, y = 540)
        ## Add label status
        self.label9 = Label(self.labelFrame1, text = "Status", font = ("arial", 12, "italic"), bg = "white", fg = "black")
        self.label9.place(x = 50, y = 600)






        
        ## Adding figures
        
        canvas = FigureCanvasTkAgg(fig, 
                               master = self.labelFrame2)   
        canvas.draw() 
    
        
        canvas.get_tk_widget().place(x = 0, 
                                     y = 0)
    
        
        toolbar = NavigationToolbar2Tk(canvas, 
                                    self.labelFrame2) 
        toolbar.update() 
    
        #canvas.get_tk_widget().place(x = 100, 
        #                            y = 200)
        canvas.get_tk_widget().pack(side = TOP, 
                                    fill = BOTH, 
                                    expand = True)
        
        
        #canvas.get_tk_widget().pack() 
  
        #window = Tk() 
        
        #window.title('Plotting in Tkinter') 
        
        #window.geometry("500x500")


        #self.plot()
  
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()


'''
def plot(): 
  
    
    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
  
    
    y = [i**2 for i in range(101)] 
  
    
    plot1 = fig.add_subplot(111) 
  
    
    plot1.plot(y) 
  
    
    
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    
    canvas.get_tk_widget().pack() 
  
    
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
  
    
    canvas.get_tk_widget().pack() 
  
window = Tk() 
  
window.title('Plotting in Tkinter') 
  
window.geometry("500x500") 
  
plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Plot") 
  
plot_button.pack() 
  
window.mainloop() 


'''