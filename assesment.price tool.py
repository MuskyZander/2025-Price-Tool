def convert_grams_to_kg(weight_g):
    return weight_g / 1000


def yes_no(question):
    """Check that a users enter yes / y or no / n to a question"""
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


def get_valid_float(prompt, allow_empty=False):
    """Get a valid float input from the user"""
    while True:
        value = input(prompt)
        if not value and allow_empty:
            return None
        try:
            return float(value.replace('$', '').strip())
        except ValueError:
            print("Please enter a valid number.")


def grams_to_kg(grams):
    return grams / 1000


def calculate_unit_price(weight_kg, cost):
    return cost / weight_kg if weight_kg > 0 else 0


def main():
    instructions = """🛒 Welcome to the Price Comparison Tool!

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
    Type 'done' when you finish entering items."""

    show_instructions = yes_no("Would you like to see the instructions? (yes/no): ")
    if show_instructions == "yes":
        print(instructions)

    print("🛒 Price Comparison Tool")

    # Using get_valid_float instead of direct float conversion
    budget = get_valid_float("Enter your budget ($): ")

    items = []
    while True:
        name = input("\nEnter item name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        # Using get_valid_float for weight and cost inputs
        weight_g = get_valid_float("Enter weight in grams: ")
        cost = get_valid_float("Enter cost ($): ")

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

    # Optional: Find best value
    if items:
        best_item = min(items, key=lambda x: x['unit_price'])
        print(f"\n✅ Best value: {best_item['name']} at ${best_item['unit_price']:.2f}/kg")

        total_spent = sum(item['cost'] for item in items)
        print(f"💸 Total spent: ${total_spent:.2f}")
        if total_spent > budget:
            print(f"⚠️ Over budget by ${total_spent - budget:.2f}")
        else:
            print(f"✅ Within budget. Remaining: ${budget - total_spent:.2f}")


if __name__ == "__main__":
    main()

