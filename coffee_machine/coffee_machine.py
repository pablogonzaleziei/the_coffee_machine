# coffee_machine.py

ingredients = {
    "water": 500,
    "coffee_beans": 100,
    "milk": 200,
    "cups": 5
}

coffee_types = {
    "espresso": {"water": 50, "coffee_beans": 20, "milk": 0, "cost": 2.5},
    "latte": {"water": 100, "coffee_beans": 20, "milk": 50, "cost": 3.0},
    "cappuccino": {"water": 100, "coffee_beans": 20, "milk": 100, "cost": 3.5}
}

def make_coffee(coffee_type):
    """
    Function to make a cup of coffee.
    """
    global ingredients
    water_needed = coffee_type["water"]
    coffee_beans_needed = coffee_type["coffee_beans"]
    milk_needed = coffee_type["milk"]
    cost = coffee_type["cost"]

    enough_ingredients = all(ingredients.get(ingredient, 0) >= quantity for ingredient, quantity in coffee_type.items() if ingredient != "cost")

    if enough_ingredients:
        print("Making coffee...")
        for ingredient, quantity in coffee_type.items():
            if ingredient != "cost":
                ingredients[ingredient] -= quantity
        print("Enjoy your coffee!")
        return cost
    else:
        print("Sorry, not enough ingredients.")
        return None

def refill_ingredients():
    global ingredients
    ingredients = {
        "water": 500,
        "coffee_beans": 100,
        "milk": 200,
        "cups": 5
    }
    print("Ingredients refilled.")
