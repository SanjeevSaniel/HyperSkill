MONEY = 550
WATER = 400
MILK = 540
COFFEE_BEANS = 120
DISPOSABLE_CUPS = 9


def action_message(water, milk, coffee_beans, disposable_cups, money):
    print("Write action(buy, fill, take, remaining, exit):")
    action = input()
    print()

    if action == "exit":
        return
    elif action != "exit":
        if action == "remaining":
            print("The coffee machine has:")
            print(f"{water} of water")
            print(f"{milk} of milk")
            print(f"{coffee_beans} of coffee beans")
            print(f"{disposable_cups} of disposable cups")
            if money != 0:
                print(f"${money} of money")
            else:
                print(f"{money} of money")

        elif action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            response = input()
            if response == "back":
                exit

            elif response == "1":
                if (water >= 250) and (coffee_beans >= 16) and (disposable_cups >= 1):
                    print("I have enough resources, making you a coffee!")
                    print()
                    water -= 250
                    coffee_beans -= 16
                    disposable_cups -= 1
                    money += 4
                else:
                    if water < 250:
                        print("Sorry, not enough water!")
                    elif coffee_beans < 16:
                        print("Sorry, not enough coffee beans!")
                    elif disposable_cups < 1:
                        print("Sorry, not enough disposable cups!")

            elif response == "2":
                if (water >= 350) and (milk >= 75) and (coffee_beans >= 20) and (disposable_cups >= 1):
                    print("I have enough resources, making you a coffee!")
                    water -= 350
                    milk -= 75
                    coffee_beans -= 20
                    disposable_cups -= 1
                    money += 7
                else:
                    if water < 350:
                        print("Sorry, not enough water!")
                    elif milk < 75:
                        print("Sorry, not enough milk!")
                    elif coffee_beans < 20:
                        print("Sorry, not enough coffee beans!")
                    elif disposable_cups < 1:
                        print("Sorry, not enough disposable cups!")

            elif response == "3":
                if (water >= 200) and (milk >= 100) and (coffee_beans >= 12) and (disposable_cups >= 1):
                    print("I have enough resources, making you a coffee!")
                    water -= 200
                    milk -= 100
                    coffee_beans -= 12
                    disposable_cups -= 1
                    money += 6
                else:
                    if water < 200:
                        print("Sorry, not enough water!")
                    elif milk < 100:
                        print("Sorry, not enough milk!")
                    elif coffee_beans < 12:
                        print("Sorry, not enough coffee beans!")
                    elif disposable_cups < 1:
                        print("Sorry, not enough disposable cups!")

        elif action == "fill":
            print("Write how many ml of water do you want to add:")
            water += int(input())
            print("Write how many ml of milk do you want to add:")
            milk += int(input())
            print("Write how many grams of coffee beans do you want to add:")
            coffee_beans += int(input())
            print("Write how many disposable cups of coffee do you want to add:")
            disposable_cups += int(input())

        elif action == "take":
            print(f"I gave you ${money}")
            money -= money
            print()
        action_message(water, milk, coffee_beans, disposable_cups, money)


action_message(WATER, MILK, COFFEE_BEANS, DISPOSABLE_CUPS, MONEY)
