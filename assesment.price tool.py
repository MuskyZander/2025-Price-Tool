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

import pandas as pd  # Used to create a nice table

# --- Empty lists to store item info ---
item_names = []
weights_grams = []
costs_dollars = []

# --- Ask the user to enter item info ---
while True:
    name = input("Enter item name (or 'done' to finish): ")
    if name.lower() == "done":
        break

    try:
        weight = float(input("Enter weight in grams (0 - 10000): "))
        cost = float(input("Enter cost in dollars (0 - 10000): "))

        # Check that weight and cost are in the right range
        if not (0 < weight <= 10000):
            print(" Weight must be between 0 and 10,000 grams.")
            continue
        if not (0 < cost <= 10000):
            print(" Cost must be between $0 and $10,000.")
            continue

    except ValueError:
        print("Please enter numbers only for weight and cost.")
        continue

    # Save the information to the lists
    item_names.append(name)
    weights_grams.append(weight)
    costs_dollars.append(cost)

# --- Check if any items were entered ---
if len(item_names) == 0:
    print("No items entered.")
else:
    # Convert grams to kilograms and round to 2 decimal places
    weights_kg = [round(g / 1000, 2) for g in weights_grams]

    # 
   price_per_kg = []

 #this goes through the items in your list one at a time gets the cost weight,price,and rounds the price to 2 decimal places
for i in range(len(costs_dollars)):
    cost = costs_dollars[i]
    weight = weights_kg[i]
    price = cost / weight
    price_per_kg.append(round(price, 2))

    # Create a table (DataFrame)
    table_data = {
        "Item": item_names,
        "Weight (g)": weights_grams,
        "Weight (kg)": weights_kg,
        "Cost ($)": costs_dollars,
        "Price per kg ($)": price_per_kg
    }

    # Make the table and sort it
    table = pd.DataFrame(table_data)
    
    #This line sorts the table from cheapest to most expensive 
    table = table.sort_values(by="Price per kg ($)")
    
    # It resets the row numbers etc by dropping row 1,2,3
    table = table.reset_index(drop=True)

    # Show the table
    print("\n📋 Price Comparison Table:")
    print(table)

    # Show the best-value item
    print(f"\n✅ Best value: {best_item['Item']} at ${best_item['Price per kg ($)']:.2f} per kg")

    # Find the cheapest item manually
    best_item = items[0]
    for item in items:
        if item['unit_price'] < best_item['unit_price']:
            best_item = item

    print(f"\n✅ Best value: {best_item['name']} - ${best_item['unit_price']:.2f} per kg")








