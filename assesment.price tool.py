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
        - Weights (in grams)
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


# This converts grams to kilograms or millilitres to litres
def grams_to_kg(grams):
    return grams / 1000

# Function to convert millilitres to litres
def ml_to_litres(ml):
    return ml / 1000


def numb_check(prompt, allow_exit=True):
    """
    Checks that the user enters a number more than 0.
    Allows 'xxx' as an exit code if allow_exit is True.
    """

    error = "❌ Please enter a number more than zero."

    while True:
        response = input(prompt).lower()

        # Check for the exit code (if allowed)
        if allow_exit and response == "xxx":
            return response

        try:
            response = float(response)  # Try to turn input into a number
            if response > 0:
                return response  # Valid input
            else:
                print(error)  # Number is not more than zero
        except ValueError:
            print(error)  # Input wasn't a number

# Main routine goes here

# Instructions
show_instructions = yes_no("Do you want to read the instructions")
if show_instructions == "yes":
    instructions()


# Using numb_check instead of direct float conversion
budget = numb_check("Enter your budget ($): ")

# Ask the user what they want to convert
print("What do you want to convert?")
print("Type 'g' for grams to kilograms")
print("Type 'ml' for millilitres to litres")
choice = input("Enter your choice: ").lower()

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
    print("Sorry, that wasn't a valid choice. Please enter 'g' or 'ml'.")

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

        items.append({
            'name': name,
            'weight_g': weight_g,
            'weight_kg': weight_kg,
            'cost': cost,
            'unit_price': unit_price
        })

print("\n📋 Comparison Results:")
print("{:<15} {:>10} {:>10} {:>10} {:>15}".format("Item", "Weight (g)", "Weight (kg)", "Cost ($)",
                                                  "Unit Price ($/kg)"))
print("-" * 60)
for item in items:
    print("{:<15} {:>10.1f} {:>10.3f} {:>10.2f} {:>15.2f}".format(
        item['name'], item['weight_g'], item['weight_kg'], item['cost'], item['unit_price']
    ))

if items:
    # Find the cheapest item manually
    best_item = items[0]
    for item in items:
        if item['unit_price'] < best_item['unit_price']:
            best_item = item

    print(f"\n✅ Best value: {best_item['name']} - ${best_item['unit_price']:.2f} per kg")








