from tkinter import *
      
class Application(Frame):

    def __init__(self,master=None):
        t1 = 'Brian: Ihr seid alle Individuen!'
        t2 = 'Volk: Ja, wir sind alle Individuen!'
        t3 = 'Brian: Und ihr seid alle völlig verschieden!'
        t4 = 'Volk: Ja, wir sind alle völlig verschieden!'
        t5 = 'Einer: Ich nicht!'
        lbl1=Label(master,text=t1, bg="yellow")
        lbl2=Label(master,text=t2, bg="green")
        lbl3=Label(master,text=t3, bg="gray")
        lbl4=Label(master,text=t4, bg="white", fg="blue")
        lbl5=Label(master,text=t5, bg="orange")
        Frame.__init__(self, master)
        lbl1.pack()
        
   

root=Tk()
app=Application(master=root)
app.mainloop()
















