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

customer_order = ""
balance = 0.0

## report, print resources and money
## when ordering check for enough resources
## when ordering check for how many coins of each type > here is $ in change enjoy your coffee
## if insufficient resource let customer know
## if not enough money is inserter refund it
## if transaction successful make the coffe and deduct resources.

def report():
    print("The coffee machine has the following resources:")
    for r in resources:
        print(f"  {r}: {resources[r]}")
    print(f"and the money balance is: {balance}")

def take_order():
    while True:
        order = input("What do you want to order (espresso/latte/cappuccino)? ").lower()
        if order in MENU or order == "off" or order == "report" :
            return order
        else:
            print("Please type in a valid drink.")

def check_resources(drink):
    enough_resources = True
    out_of = ""
    for ingridient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingridient] > resources[ingridient]:
            enough_resources = False
            out_of = ingridient
            return enough_resources, out_of
        else:
            return enough_resources, out_of
def update_resources(drink):
    for ingridient in MENU[drink]["ingredients"]:
        resources[ingridient] = resources[ingridient] - MENU[drink]["ingredients"][ingridient]
        #print(resources[ingridient])

def check_payment(drink):
    global balance
    price = MENU[drink]["cost"]
    quarters = input("How many quarters? ").strip() or "0"
    dimes = input("How many dimes? ").strip() or "0"
    nickles = input("How many nickles? ").strip() or "0"
    pennies = input("How many pennies? ").strip() or "0"
    payment = int(quarters)*0.25 + int(dimes)*0.1 + int(nickles)*0.05 + int(pennies)*0.01
    if payment >= price:
        balance = balance + price
        change = payment - price
        if change > 0:
            print(f"Here is {round(change,2)} in change")
    # print(round(payment,2))
    # print(balance)



while customer_order != "off":
    customer_order = take_order()
    if customer_order == "report":
        report()
    elif customer_order == "off":
        pass
    else:
        make_coffe, missing_ingridient = check_resources(customer_order)
        if make_coffe:
            check_payment(customer_order)
            update_resources(customer_order)
            print(f"Here is your {customer_order} enjoy !")
        else:
            print(f"Sorry there is not enough {missing_ingridient} :( ")