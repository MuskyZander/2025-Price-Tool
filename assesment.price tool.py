from locale import currency

import pandas


# Functions go here

def make_statements(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def instructions():
    print( """🛒 Welcome to the Price Comparison Tool!

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



    print("🛒 Price Comparison Tool")


def yes_no(question):
    """Check that users enter yes / y or no / n to a question"""
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")


def calculate_unit_price(weight_kg, cost):
    if weight_kg == 0:
        return 0
    return cost / weight_kg


# This converts grams to kilograms or millilitres to liters
def grams_to_kg(grams):
    return grams / 1000

# Function to convert millilitres to litres
def ml_to_litres(ml):
    return ml / 1000


def numb_check(prompt, allow_exit=True, min_value=0, max_value=100):
    """
    Asks the user to enter a number between min_value and max_value.
    The user can type 'xxx' to exit if allow_exit is True.
    """
    error = f"Please enter a number more than {min_value}"
    if max_value is not None:
        error += f" and less than or equal to {max_value}."

    while True:
        response = input(prompt).lower()

        # Allow user to exit if they type 'xxx'
        if allow_exit and response == "xxx":
            return response

        try:
            number = float(response)  # Try changing input to a number
            if number > min_value and number <= max_value:
                return number  # Return number if it's in the right range
            else:
                print(error)  # The Number is too small or too big
        except ValueError:
            print("Please enter a valid number.")  # Input wasn't a number

# Main routine goes here

# Instructions
show_instructions = yes_no("Do you want to read the instructions")
if show_instructions == "yes":
    instructions()


# Using numb_check instead of direct float conversion
budget = numb_check("Enter your budget between 0 and 100 ($): ")

# Ask the user what they want to convert
choice = input("What do you want to convert? Type 'g' for grams to kilograms or 'ml' for millilitres to litres: ").lower()

# Do the correct conversion based on the user's choice
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

# Price comparison/unit price
items = []
while True:
    name = input("\nEnter item name (or 'done' to finish): ").lower()
    if name.lower() == 'done':
        break

    # Using numb_check for weight and cost inputs
    weight_g = numb_check("Enter weight in grams: ")
    cost = numb_check("Enter cost ($): ")

    if weight_g is not None and cost is not None:
        weight_kg = grams_to_kg(weight_g)
        unit_price = calculate_unit_price(weight_kg, cost)

# --- Item Details ---
names = ["Apples", "Bananas", "Carrots"]
weight_g = [500, 1000, 750]     # weight in grams
costs = [3.50, 2.80, 4.20]      # cost in dollars

# --- Convert grams to kilograms ---
weight_kg = [w / 1000 for w in weight_g]

# --- Calculate unit price ($ per kg) ---
unit_price = [cost / kg for cost, kg in zip(costs, weight_kg)]

# --- Store in dictionary ---
items_dict = {
    "Item": names,
    "Weight (g)": weight_g,
    "Weight (kg)": weight_kg,
    "Cost ($)": costs,
    "Unit Price ($/kg)": unit_price
}

# --- Show the results ---
import pandas as pd

items_table = pd.DataFrame(items_dict)

# --- Show the best value item ---
best_value = items_table.iloc[0]
print(f"\n✅ Best value: {best_value['Item']} at ${best_value['Unit Price ($/kg)']:.2f} per kg")

print("\n📋 Price Comparison Table:")
print(items_table)

# --- Total cost ---
total = sum(costs)
print(f"\n💰 Total Cost: ${total:.2f}")
if items:
    # Find the cheapest item manually
    best_item = items[0]
    for item in items:
        if item['unit_price'] < best_item['unit_price']:
            best_item = item

    print(f"\n✅ Best value: {best_item['name']} - ${best_item['unit_price']:.2f} per kg")








