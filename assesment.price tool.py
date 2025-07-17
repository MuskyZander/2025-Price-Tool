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


def grams_to_kg(grams):
    return grams / 1000


def numb_check(prompt, allow_empty=False):
    """Checks users enter an integer that is more than zero (or the 'xxx' exit code)"""

    error = "Oops - please enter a integer more than zero."

    while True:
        response = input(prompt).lower()  # Changed 'question' to 'prompt'

        # check for the exit code
        if response == "xxx":
            return response

        try:
            # Change the response to an
            # integer and check that it's more than zero
            response = float(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine goes here

show_instructions = yes_no("Do you want to read the instructions")
if show_instructions == "yes":
    instructions()


# Using numb_check instead of direct float conversion
budget = numb_check("Enter your budget ($): ")

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








