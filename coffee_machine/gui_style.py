import tkinter as tk
from tkinter import ttk


def set_style():
    style = ttk.Style()

    # Define the style for the labels
    style.configure("TLabel", font=("Helvetica", 14), foreground="#1a1a1a", background="#d9d9d9")

    # Define the style for the option menu
    style.configure("TMenubutton", font=("Helvetica", 14), foreground="#fff", background="#1a1a1a", padding=8)

    # Define the style for the buttons
    style.configure("TButton", font=("Helvetica", 14), foreground="#fff", background="#1a1a1a", padding=10)

    # Define the style for the frames
    style.configure("TFrame", background="#d9d9d9", borderwidth=0)

    # Define the style for the window
    style.configure(".", background="#d9d9d9")
