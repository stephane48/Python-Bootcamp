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


# Function to check if there are enough resources
def resources_check():
    if coffe_type == "espresso":
        if resources['water'] >= MENU["espresso"]["ingredients"]["water"]:
            return True
        else:
            print("Sorry there is not enough water")
            return False
        if resources['coffee'] >= MENU["espresso"]["ingredients"]["coffee"]:
            return True
        else:
            print("Sorry there is not enough coffee")
            return False
    elif coffe_type == "latte":
        if resources['water'] >= MENU["latte"]["ingredients"]["water"]:
            return True
        else:
            print("Sorry there is not enough water")
            return False
        if resources['milk'] >= MENU["latte"]["ingredients"]["milk"]:
            return True
        else:
            print("Sorry there is not enough milk")
            return False
        if resources['coffee'] >= MENU["latte"]["ingredients"]["coffee"]:
            return True
        else:
            print("Sorry there is not enough coffee")
            return False
    elif coffe_type == "cappuccino":
        if resources['water'] >= MENU["cappuccino"]["ingredients"]["water"]:
            return True
        else:
            print("Sorry there is not enough water")
            return False
        if resources['milk'] >= MENU["cappuccino"]["ingredients"]["milk"]:
            return True
        else:
            print("Sorry there is not enough milk")
            return False
        if resources['coffee'] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            return True
        else:
            print("Sorry there is not enough coffee")
            return False


def transaction(coffe_type, money, user_price):
    if user_price < MENU[coffe_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif user_price >= MENU[coffe_type]["cost"]:
        money += MENU[coffe_type]["cost"]
        resources["money"] = money
        refund = user_price - MENU[coffe_type]["cost"]
        print(f"Here is ${round(refund, 2)} in change")
        return True


def deduction_resources(coffe_type):
    resources['water'] = resources['water'] - MENU[coffe_type]["ingredients"]["water"]
    if coffe_type != "espresso":
        resources['milk'] = resources['milk'] - MENU[coffe_type]["ingredients"]["milk"]
    resources['coffee'] = resources['coffee'] - MENU[coffe_type]["ingredients"]["coffee"]
    return resources


# print(MENU['espresso']['ingredients'])
# for value in resources:
#   print(value)

end_the_machine = False
resources['money'] = 0

while end_the_machine is False:
    coffe_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffe_type == "off":
        end_the_machine = True

    elif coffe_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif coffe_type == "espresso":
        if resources_check():
            print("Please insert coins.")
            quater = float(input("How many quaters?: "))
            dime = float(input("How many dimes?: "))
            nickle = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            user_price = quater * 0.25 + dime * 0.1 + nickle * 0.05 + pennies * 0.01
            if transaction(coffe_type, resources['money'], user_price):
                deduction_resources(coffe_type)
                print(f"Here is your {coffe_type}. Enjoy!")
    elif coffe_type == "latte":
        if resources_check():
            print("Please insert coins.")
            quater = float(input("How many quaters?: "))
            dime = float(input("How many dimes?: "))
            nickle = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            user_price = quater * 0.25 + dime * 0.1 + nickle * 0.05 + pennies * 0.01
            if transaction(coffe_type, resources['money'], user_price):
                deduction_resources(coffe_type)
                print(f"Here is your {coffe_type}. Enjoy!")
    elif coffe_type == "cappuccino":
        if resources_check():
            print("Please insert coins.")
            quater = float(input("How many quaters?: "))
            dime = float(input("How many dimes?: "))
            nickle = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            user_price = quater * 0.25 + dime * 0.1 + nickle * 0.05 + pennies * 0.01
            if transaction(coffe_type, resources['money'], user_price):
                deduction_resources(coffe_type)
                print(f"Here is your {coffe_type}. Enjoy!")

# print(resources)

