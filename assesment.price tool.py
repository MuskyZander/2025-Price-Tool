from locale import currency
import pandas as pd  # Used to create a nice formatted table

#  Functions go here

def make_statements(statement, decoration):
    """Adds decoration around a heading to make it stand out"""
    return f"{decoration * 3} {statement} {decoration * 3}"

def instructions():
    """Displays instructions for using the tool"""
    print("""🛒 Welcome to the Price Comparison Tool!

        This tool helps you:
        1. Compare prices of different items based on their weight
        2. Track your shopping budget
        3. Find the best value items
        4. Calculate price per kilogram

        The tool will ask you for:
        - Your shopping budget
        - Item names
        - Weight (in grams)
        - Costs (in dollars)

        You can enter as many items as you want.
        Type 'done' when you finish entering items.""")

def yes_no(question):
    """Asks the user a yes/no question and checks they give a valid answer"""
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")

def calculate_unit_price(weight_kg, cost):
    """Calculates price per kg (avoids division by zero)"""
    if weight_kg == 0:
        return 0
    return cost / weight_kg

def grams_to_kg(grams):
    """Converts grams to kilograms"""
    return grams / 1000

def ml_to_litres(ml):
    """Converts millilitres to litres"""
    return ml / 1000

def numb_check(prompt, allow_exit=True, min_value=0, max_value=10000):
    """
    Checks that the user enters a number in a valid range.
    Can allow the user to type 'xxx' to exit early if allow_exit is True.
    """
    error = f"Please enter a number more than {min_value}"
    if max_value is not None:
        error += f" and less than or equal to {max_value}."

    while True:
        response = input(prompt).lower()
        if allow_exit and response == "xxx":
            return response
        try:
            number = float(response)
            if min_value < number <= max_value:
                return number
            else:
                print(error)
        except ValueError:
            print("Please enter a valid number.")

#  Main routine starts here

# Ask if user wants instructions
show_instructions = yes_no("Do you want to read the instructions? ")
if show_instructions == "yes":
    instructions()

# Ask for shopping budget (between 0 and 100)
budget = numb_check("Enter your budget between 0 and 100 ($): ", min_value=0, max_value=100)

# Quick conversion tool for grams or millilitres
choice = input("What do you want to convert? Type 'g' for grams to kilograms or 'ml' for millilitres to litres: ").lower()
if choice == 'g':
    grams = float(input("Enter the number of grams: "))
    kg = grams_to_kg(grams)
    print(f"{grams} grams is {kg} kilograms.")
elif choice == 'ml':
    ml = float(input("Enter the number of millilitres: "))
    litres = ml_to_litres(ml)
    print(f"{ml} millilitres is {litres} litres.")
else:
    print("Sorry, that wasn't a valid choice. Please enter 'g' or 'ml' next time.")

import pandas as pd  # Used to create a nice formatted table

# --- Get item data ---
item_names = []       # Stores names of items
weights_grams = []    # Stores weights in grams
costs_dollars = []    # Store item costs
items = []            # Stores all item info for later comparison

while True:
    name = input("\nEnter item name (or 'done' to finish): ").lower()
    if name == 'done':
        break

    weight_g = numb_check("Enter weight in grams (0 - 10000): ")
    if weight_g == "xxx":
        break

    cost = numb_check("Enter cost ($) (0 - 10000): ")
    if cost == "xxx":
        break

    # Convert grams to kilograms and calculate unit price
    weight_kg = grams_to_kg(weight_g)
    unit_price = calculate_unit_price(weight_kg, cost)

    # Store values
    item_names.append(name)
    weights_grams.append(weight_g)
    costs_dollars.append(cost)
    items.append({
        'name': name,
        'weight_g': weight_g,
        'weight_kg': weight_kg,
        'cost': cost,
        'unit_price': unit_price
    })

# --- After data entry ---

# Check if any items were entered
if len(item_names) == 0:
    print("No items entered.")
else:
    # Convert weights to kg again for display purposes
    weights_kg = [round(g / 1000, 2) for g in weights_grams]
    price_per_kg = []

    # Calculate unit price for each item

    # Go through each item in the list using its position number
    for i in range(len(costs_dollars)):

        cost = costs_dollars[i]
        weight = weights_kg[i]
        price = cost / weight
        # Rounds the price per kg to 2 decimal points
        price_per_kg.append(round(price, 2))

    # Make a DataFrame table to display items
    table_data = {
        "Item": item_names,
        "Weight (g)": weights_grams,
        "Weight (kg)": weights_kg,
        "Cost ($)": costs_dollars,
        "Price per kg ($)": price_per_kg
    }

    # gets the list of each item so it can be displayed in a table format using pandas
    table = pd.DataFrame(table_data)

    # Show table
    print("\n📋 Price Comparison Table:")
    print(table)

    # Find the best value item from the list
    best_item = items[0]
    for item in items:
        if item['unit_price'] < best_item['unit_price']:
            best_item = item

    # Show the best value
    print(f"\n✅ Best value: {best_item['name'].title()} - ${best_item['unit_price']:.2f} per kg")








