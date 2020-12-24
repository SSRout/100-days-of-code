#Coffe Machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 10,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15,
    }
}

profit=0

resources={
    "water":300,
    "milk":200,
    "coffee":100
}

def is_resource_sufficient(order_ingredients):
    """Return true or false"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry not Enough {item} to Make Coffee.")
            return False
    return True

def process_coins():
    """Return Calculated Coins"""
    print("Please inseet Coins")
    total=int(input("Insert coins "))
    return total

def is_transaction_success(money_received,drink_cost):
    """Return true when payament accepted or false"""
    if money_received>=drink_cost:
        chnage=round(money_received-drink_cost,2)
        print(F"Extra changes here ₹{chnage}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Not Enough money for coffee")
        return False

def make_coffee(drink_name,order_ingreints):
    """deduct required ingredients"""
    for item in order_ingreints:
        resources[item]-=order_ingreints[item]
    print("Brewd Coffee")




is_on=True
while is_on:
    choice=input("What would you like?(espresso/latte/cappuccino)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water : {resources['water']}l")
        print(f"Milk: {resources['milk']}l")
        print(f"coffee : {resources['coffee']}g")
        print(f"Money : ₹{profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payement=process_coins()
            if is_transaction_success(payement,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
