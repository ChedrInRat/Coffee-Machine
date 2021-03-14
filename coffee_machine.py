espresso = {"water": 250, "milk": 0, "coffee_beans": 16, "price": 4}
latte = {"water": 350, "milk": 75, "coffee_beans": 20, "price": 7}
cappuccino = {"water": 200, "milk": 100, "coffee_beans": 12, "price": 6}

coffee = {"espresso": espresso, "latte": latte, "cappuccino": cappuccino}

coffee_machine = {"water": 400, "milk": 540, "coffee_beans": 120, "money": 550, "disposable_cups": 9}


def remaining():
    print("\nThe coffee machine has:\n"
          f"{coffee_machine['water']} of water\n"
          f"{coffee_machine['milk']} of milk\n"
          f"{coffee_machine['coffee_beans']} of coffee beans\n"
          f"{coffee_machine['disposable_cups']} of disposable cups\n"
          f"{coffee_machine['money']} of money")


def fill():
    global coffee_machine
    print("Write how many ml of water do you want to add:")
    coffee_machine["water"] += int(input())
    print("Write how many ml of milk do you want to add:")
    coffee_machine["milk"] += int(input())
    print("Write how many ml of coffee beans do you want to add:")
    coffee_machine["coffee_beans"] += int(input())
    print("Write how many ml of disposable_cups do you want to add:")
    coffee_machine["disposable_cups"] += int(input())


def buy():
    global coffee, coffee_machine
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    client_coffee = input()
    if client_coffee == '1':
        client_coffee = "espresso"
    elif client_coffee == '2':
        client_coffee = "latte"
    elif client_coffee == '3':
        client_coffee = "cappuccino"

    if client_coffee in coffee.keys():

        if coffee[client_coffee]["water"] < coffee_machine["water"]:
            coffee_machine["water"] -= coffee[client_coffee]["water"]
            coffee_machine["milk"] -= coffee[client_coffee]["milk"]
            coffee_machine["coffee_beans"] -= coffee[client_coffee]["coffee_beans"]
            coffee_machine["money"] += coffee[client_coffee]["price"]
            coffee_machine["disposable_cups"] -= 1
            print("I have enough resources, making you a coffee!")
        else:
            print("Sorry, not enough water!")

    else:
        print("Invalid input")


def take():
    global coffee_machine
    print(f"I gave you {coffee_machine['money']}")
    coffee_machine['money'] = 0


def user_input():
    global action
    print("Write action (buy, fill, take, remaining, exit):")
    act = input()
    if act in action.keys():
        action[act]()


action = {"fill": fill, "buy": buy, "take": take, "remaining": remaining, "exit": exit}


def start():
    user_input()


while True:
    start()
