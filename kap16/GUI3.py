from tkinter import *
      
class Application(Frame):

    def __init__(self,master=None):
        meinLbl=Label(master,text=" Ein Kratzer?! Ihr Arm ist ab!")
        Frame.__init__(self, master)
        meinLbl.place(x=10,y=10)
   

root=Tk()
app=Application(master=root)
app.mainloop()
















