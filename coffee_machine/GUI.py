import tkinter as tk
from tkinter import ttk, messagebox
from coffee_machine import make_coffee, refill_ingredients, ingredients, coffee_types

balance = 0

# Define the GUI window
window = tk.Tk()
window.title("Coffee Machine")
window.configure(background="#3d5069")

style = ttk.Style()
style.theme_use('default')

style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground='#FFFFFF', background='#E1B382',
                bordercolor='#FFFFFF', lightcolor='#502857', darkcolor='#3e4d5e', padding=10)

style.configure('TEntry', 
                background='#e6e6e6', 
                foreground='#101721', 
                font=('Helvetica', 14, 'bold'), 
                padding=10)

style.configure('TLabel',
                background='#e6e6e6', 
                foreground='#101721', 
                font=('Arial', 14), 
                padding=10)

# Define the widgets for the GUI





def add_money_callback():
    global balance
    try:
        amount = float(add_money_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    if amount < 0:
        messagebox.showerror("Error", "Please enter a positive number")
        return
    balance += amount
    balance_label.config(text="Balance: ${:.2f}".format(balance))



def update_cost_label(*args):
    selected_coffee_type = coffee_types.get(coffee_type_var.get())
    if selected_coffee_type:
        cost_label.config(text="Cost: ${:.2f}".format(selected_coffee_type["cost"]))
        make_coffee_button.config(state=tk.NORMAL)
    else:
        cost_label.config(text="Cost: $0")
        make_coffee_button.config(state=tk.DISABLED)



def update_balance(amount):
    global balance
    balance -= amount
    balance_label.config(text="Balance: ${:.2f}".format(balance))

def finish_purchase():
    global balance
    if balance > 0:
        messagebox.showinfo("Coffee Machine", "Here's your change: ${:.2f}".format(balance))
        balance = 0
        balance_label.config(text="Balance: ${:.2f}".format(balance))
    else:
        messagebox.showwarning("Coffee Machine", "There's no change to give.")


def make_coffee_callback():
    selected_coffee_type = coffee_types[coffee_type_var.get()]
    cost = make_coffee(selected_coffee_type)
    if cost:
        if balance < cost:
            messagebox.showerror("Error", "Not enough balance")
            return
        update_balance(cost)
        messagebox.showinfo("Coffee Machine", "Enjoy your coffee!")
        update_ingredients_labels()


def refill_callback():
    refill_ingredients()
    messagebox.showinfo("Coffee Machine", "Ingredients refilled.")
    update_ingredients_labels()

refill_button = ttk.Button(window, text="Refill ingredients", command=refill_callback)
refill_button.grid(row=7+len(ingredients), column=0, padx=10, pady=10, sticky='w')

def update_ingredients_labels():
    for i, ingredient in enumerate(ingredients):
        label_text = "{}: {}".format(ingredient.replace("_", " ").capitalize(), ingredients[ingredient])
        ingredients_labels[i].config(text=label_text)

ingredients_labels = []
for i, ingredient in enumerate(ingredients):
    label_text = "{}: {}".format(ingredient.replace("_", " ").capitalize(), ingredients[ingredient])
    ingredient_label = tk.Label(window, text=label_text)
    ingredient_label.grid(row=7, column=0+i, padx=2, pady=2, sticky='w')
    ingredients_labels.append(ingredient_label)
    
coffee_type_var = tk.StringVar(value=list(coffee_types.keys())[0])

title_label = ttk.Label(window, text="Select a coffee type:")
title_label.grid(row=0, column=0, columnspan=2, pady=5)

cost_label = ttk.Label(window, text="Cost: $0")
cost_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

coffee_type_option_menu = tk.OptionMenu(window, coffee_type_var, *coffee_types.keys(), command= update_cost_label)
coffee_type_option_menu.grid(row=1, column=1, padx=10, pady=5, sticky='w')

make_coffee_button = ttk.Button(window, text="Make coffee", state=tk.DISABLED)
make_coffee_button.config(command=lambda: make_coffee_callback())
make_coffee_button.grid(row=1, column=2, padx=10, pady=10, sticky='w')

balance_label = ttk.Label(window, text="Balance: $0")
balance_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

add_money_button = ttk.Button(window, text="Add Money", command=add_money_callback)
add_money_button.grid(row=2, column=2, padx=10, pady=5, sticky='w')

add_money_entry = ttk.Entry(window)
add_money_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')


finish_button = ttk.Button(window, text="Finish Purchase", command=finish_purchase)
finish_button.grid(row=6, column=0, padx=10, pady=10, sticky='w')

update_cost_label()
update_ingredients_labels()

window.mainloop()