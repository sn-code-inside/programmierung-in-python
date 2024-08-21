import tkinter as tk
from tkinter import messagebox

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Mehrere Lambda-Ausdrücke Beispiel")

# Funktionen für die Ereignisbehandlung
def show_message(message):
    messagebox.showinfo("Nachricht", message)

# Erstellen von drei Buttons mit unterschiedlichen Lambda-Ausdrücken
button1 = tk.Button(root, text="Button 1", command=lambda: show_message("Button 1 wurde geklickt"))
button1.pack(pady=10)

button2 = tk.Button(root, text="Button 2", command=lambda: show_message("Button 2 wurde geklickt"))
button2.pack(pady=10)

button3 = tk.Button(root, text="Button 3", command=lambda: show_message("Button 3 wurde geklickt"))
button3.pack(pady=10)

# Starten der tkinter Hauptloop
root.mainloop()
