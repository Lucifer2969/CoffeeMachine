import os

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
money = {
    "dollar": 0.0,
}
penny = 0
nickl = 0
dime = 0
quarter = 0
condition = True

def resource_status():
    """Updates current status of resource available"""
    for key in resources:
        print(f"{key}:{resources[key]}")

def resource_status_check(option):
    """Checks resource status if it is enough to dispense the coffee to the customer. """
    if option == "report":
        return resource_status()
    elif option == "espresso":
        if resources["water"] < MENU[option]["ingredients"]["water"]:
            return 'Sorry there is not enough water'
        elif resources["coffee"] < MENU[option]["ingredients"]["coffee"]:
            return 'Sorry there is not enough water'
        else:
            return True
    else:
        if resources["water"] < MENU[option]["ingredients"]["water"]:
            return 'Sorry there is not enough water'
        elif resources["milk"] < MENU[option]["ingredients"]["milk"]:
            return 'Sorry there is not enough milk'
        elif resources["coffee"] < MENU[option]["ingredients"]["coffee"]:
            return 'Sorry there is not enough water'
        else:
            return True

def resource_update(option):
    """Function to update the milk, water and coffee amount in dictonary"""
    if option != "espresso":
        resources ["water"] = resources ["water"] - MENU [option]["ingredients"]["water"]
        resources ["milk"] = resources ["milk"] - MENU [option]["ingredients"]["milk"]
        resources ["coffee"] = resources ["coffee"] - MENU [option]["ingredients"]["coffee"]
    else:
        resources ["water"] = resources ["water"] - MENU [option]["ingredients"]["water"]
        resources ["coffee"] = resources ["coffee"] - MENU [option]["ingredients"]["coffee"]


def insert_coin ():
    """Function to take coins input from the customer"""
    print("Please insert coins.")
    penny = float(input("How many pennies?: "))
    nickl = float(input("How many nickles?: "))
    dime = float(input("How many dimes?: "))
    quarter = float(input("How many quarters?: "))
    money["dollar"] = penny * 0.01 + nickl * 0.05 + dime * 0.1 + quarter * 0.25

def check_money(money_dic,option):
    """Function to check the status of money provided by the customer if it's enough 
    to dispense the coffee"""
    if money_dic["dollar"] < MENU [option]["cost"]:
        return "Sorry money not enough. Money refunded", 0
    else:
        re_amount = money_dic["dollar"] - MENU [option]["cost"]
        return True, re_amount

while condition:
    print("""Please select your choice
            1. Espresso
            2. Latte
            3. Cappuccino
            4. Report
            5. Off
        """)
    choice = input("What would you like😊: ").lower()

    if choice != "off":
        resource_state = resource_status_check(choice)
        if resource_state == True:
            insert_coin()
            money_status,return_amount = check_money(money,choice)
            if money_status == True:
                resource_update(choice)
                print (f"Here is your change ${return_amount}")
                print (f"Please enjoy your, 🍵{choice}" )
            else:
                print (money_status)
        else:
            print (resource_state)
    else:
        print ("Switching Off.........")
        condition = False
os.system("pause")    
