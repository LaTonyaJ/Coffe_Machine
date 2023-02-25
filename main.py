from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
making_coffee = True

while making_coffee:
    pick = input(f"What would you like '{menu.get_items()}'? ")

    if pick == "off":
        making_coffee = False
    elif pick == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(pick)
        if coffee_maker.is_resource_sufficient(drink):
            # money_machine.process_coins()
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


