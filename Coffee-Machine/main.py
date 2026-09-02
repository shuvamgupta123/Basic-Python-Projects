from data import menu, resources
profit = 0
dataToIgnore = ["cappuccino", "latte", "espresso", "report", "off"]
amount = 0
a = True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10 
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(payment, cost):
    if payment >= cost:
        return True
    else:
        return False

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
                a = False
                print(f"Sorry, there is not enough {ingredient}.")
                break
        if a == True:
            amount = menu[coffee]["cost"]
            print(f"The cost of {coffee} is ${amount}.")
            payment = process_coins()
            if is_transaction_successful(payment, amount):
                change = round(payment - amount, 2)
                print(f"Here is ${change} in change.")
                profit += amount
                for ingredient in ingredients:
                    resources[ingredient] -= ingredients[ingredient]
                print(f"Here is your {coffee}. Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")