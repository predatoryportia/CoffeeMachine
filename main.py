class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffe_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.available_resources = []

    def interaction(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "buy":
                self.buy_coffee()
            elif action == "fill":
                self.fill_machine()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.status()
                pass
            elif action == "exit":
                break

    def status(self):
        print(f"""
The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.coffe_beans} g of coffee beans
{self.disposable_cups} disposable cups
{self.money} of money
        """)

    def buy_coffee(self):
        self.available_resources = [self.water, self.water, self.coffe_beans, self.disposable_cups, self.money]
        necessary_resources = {1: [250, 0, 16, 1, 4],
                               2: [350, 75, 20, 1, 7],
                               3: [200, 100, 12, 1, 6]}

        ingredients = ["water", "milk", "coffee beans", "disposable cups", "money"]

        choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == "back":
            return
        else:
            choice = int(choice)

        for n in range(4):
            if necessary_resources[choice][n] > self.available_resources[n]:
                print(f"Sorry, not enough {ingredients[n]}!\n")
                return

        print("I have enough resources, making you a coffee!\n")
        self.water -= necessary_resources[choice][0]
        self.milk -= necessary_resources[choice][1]
        self.coffe_beans -= necessary_resources[choice][2]
        self.disposable_cups -= 1
        self.money += necessary_resources[choice][4]

    def fill_machine(self):
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffe_beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable cups you want to add:\n"))
        print()

    def take(self):
        print(f'\nI gave you {self.money}\n')
        self.money = 0
