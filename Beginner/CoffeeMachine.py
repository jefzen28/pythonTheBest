# MENU: different drinks a user can order
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# resources: the remaining materials available
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# profit: amount of money made
profit = 0


def report():
    """prints the remaining water, milk, and coffee, and profit"""
    print(f"Water:\t{resources['water']}ml")
    print(f"Milk:\t{resources['milk']}ml")
    print(f"Coffee:\t{resources['coffee']}g")
    print(f"Money:\t${profit}")


def sufficient(drink):
    """returns True if there is enough resources to make the drink, False otherwise"""
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def process_money():
    """asks user to enter amount of coins to pay, returns total amount"""
    print("Please insert coins")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# choice: user input
choice = ''
while not choice == 'off':
    choice = input(f"What would you like? (espresso-${MENU['espresso']['cost']} / latte-${MENU['latte']['cost']} / cappuccino-${MENU['cappuccino']['cost']}): ").lower()
    if choice == 'report':
        report()
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if sufficient(choice):
            money = process_money()
            if money < MENU[choice]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += MENU[choice]['cost']
                print(f"Here is ${round((money - MENU[choice]['cost']), 2)} in change")
                for ingredient in MENU[choice]['ingredients']:
                    resources[ingredient] -= MENU[choice]['ingredients'][ingredient]
                print(f"Here is you {choice}. Enjoy!")
