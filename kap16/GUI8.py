from tkinter import *

class Application(Frame):
   
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Label(master, text="Nachname").grid(row=0)
        Label(master, text="Vorname").grid(row=1)
        Label(master, text="Die Eingabe").grid(row=2)
        self.lbl1 = Label(master, bg="yellow", fg="blue")
        self.lbl1.grid(row=2, column=1)
        self.nname = Entry(master)
        self.vname = Entry(master)
        Button(master, text='OK', width=20, command=lambda: self.action()).grid(row=3, column=0)
        Button(master, text='Abbrechen', width=20, command=root.destroy).grid(row=3, column=1)
        self.nname.grid(row=0, column=1)
        self.vname.grid(row=1, column=1)

    def action(self):
        self.lbl1.config(text=self.vname.get() + ", " + self.nname.get())

root = Tk()
app = Application(master=root)
app.mainloop()
















