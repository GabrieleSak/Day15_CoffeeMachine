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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


# TODO: 1. User prompt “What would you like? (espresso/latte/cappuccino):”
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
# TODO: 3. Print report
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.


def check_resources(product):
    enough_ingredients = True
    for ingredient in MENU[product]['ingredients'].keys():
        if resources[ingredient] < MENU[product]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            enough_ingredients = False
        return enough_ingredients


def report():
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${money}")

def coin_process():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    sum_of_coins = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return sum_of_coins



turn_off = False

while not turn_off:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        report()
    elif choice == "off":
        turn_off = True
    elif check_resources(choice):
        sum_of_coins = coin_process()
        cost = MENU[choice]['cost']
        if sum_of_coins < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            money += cost
            change = round(sum_of_coins - cost, 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {choice} ☕. Enjoy!")
            for ingredient in MENU[choice]['ingredients'].keys():
                resources[ingredient] -= MENU[choice]['ingredients'][ingredient]


