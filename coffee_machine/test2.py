import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# configure the style
style = ttk.Style()
style.theme_use('default')

style.configure('TButton', 
                background='#2ecc71', 
                foreground='#ffffff', 
                font=('Helvetica', 14, 'bold'), 
                padding=10, 
                width=15)

# create the button
button = ttk.Button(root, text="Click me!", command=lambda: print("Button clicked"))

button.pack(pady=10)

root.mainloop()
