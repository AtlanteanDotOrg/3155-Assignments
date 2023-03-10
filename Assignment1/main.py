# Data #
import sys

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}


# Complete functions #

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources
        self.input = input("What would you like to order today? (small/medium/large/off/report): ")
        while self.input == "report":
            for x, y in resources.items():
                print(x, ": ", y)
            self.input = input("What would you like to order today? (small/medium/large/off/report): ")
        if self.input == "off":
            print("Closing Up")
            sys.exit()

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for x, y in ingredients["ingredients"].items():
            for z, w in resources.items():
                if x == z:
                    if y > w:
                        print("Insufficient", z, "cancelling order.")
                        return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = input("How many Dollar Coins?: ")
        half_dollars = input("How many Half Dollars?: ")
        quarters = input("How many Quarters?: ")
        nickles = input("How many Nickles?: ")
        total = (float(dollars) * 1) + (float(half_dollars) * 0.5) + (float(quarters) * 0.25) + (float(nickles) * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if cost < coins:
            print("Insufficient funds, cancelling order.")
            return False
        change = round(cost - coins, 2)
        print("Thank you for purchasing! Here is your change: $", change)
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for resource_name, resource_amt in order_ingredients.items():
            for ingredient_name, ingredient_amt, in sandwich_size["ingredients"].items():
                if resource_name == ingredient_name:
                    ingredient_value = ingredient_amt
                    current_value = resource_amt
                    total = current_value - ingredient_value
                    order_ingredients[resource_name] = total

# Make an instance of SandwichMachine class and write the rest of the codes #

running = True
while running:
    sandwich_shop = SandwichMachine(resources)
    if sandwich_shop.check_resources(recipes[sandwich_shop.input]):
        money_input = sandwich_shop.process_coins()
        if sandwich_shop.transaction_result(recipes[sandwich_shop.input]["cost"], money_input):
            sandwich_shop.make_sandwich(recipes[sandwich_shop.input], resources)
    for x in resources.values():
        if x == 0:
            running = False
print("Closing, need to restock.")
