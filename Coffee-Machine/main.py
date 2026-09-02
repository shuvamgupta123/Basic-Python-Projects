from data import menu, resources
profit = 0
dataToIgnore = ["water", "milk", "coffee", "report", "off"]

while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee == "off":
        print("Turning off the coffee machine. Goodbye!")
        break

    if coffee == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")

    if coffee not in dataToIgnore:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")

    if coffee in menu:
        drink = menu[coffee]                    #{all drinks}
        ingredients = drink["ingredients"]      #{all ingredients for the selected drink}

        for ingredient in ingredients:
            if ingredients[ingredient] > resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                break