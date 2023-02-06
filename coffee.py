from main import MENU, resources


making_coffee = True
money = 0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

# TODO: 4. Check resources


def check_resources(item):
    """Returns True or False depending on if resources are available"""
    item_water = MENU[item]['ingredients']['water']
    item_coffee = MENU[item]['ingredients']['coffee']
    if item_water > water:
        print("Sorry, there is not enough water.")
        return False
    elif item_coffee > coffee:
        print("Sorry, there is not enough coffee.")
        return False
    elif item != 'espresso':
        item_milk = MENU[item]['ingredients']['milk']
        if item_milk > milk:
            print("Sorry, there is not enough milk.")
            return False
        else:
            return True
    else:
        return True


# TODO: 5. Process coins


def insert_coins():
    """Returns Total money inserted amount"""
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickels = input("How many nickels?: ")
    pennies = input("How many pennies?: ")
    total = (int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickels) * 0.05) + (int(pennies) * 0.01)
    return float(total)


# TODO: 7. Make Coffee

def make_drink(selection):
    """Deducts ingredients to make drink selection"""
    global water, coffee, milk
    water -= MENU[selection]['ingredients']['water']
    coffee -= MENU[selection]['ingredients']['coffee']
    if selection != 'espresso':
        milk -= MENU[selection]['ingredients']['milk']

# TODO: 1. Prompt User


while making_coffee:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink in MENU:
        has_resources = check_resources(drink)
        # print(f"Has resources: {has_resources}")
        if has_resources:
            # process coins
            # print("process coins")
            money_inserted = insert_coins()
            # TODO: 6. Transaction Check
            cost = MENU[drink]['cost']
            if money_inserted == cost:
                print(f"Here is your {drink.capitalize()}, Enjoy!")
                make_drink(drink)
                money += money_inserted
            elif money_inserted < cost:
                print("Sorry, that's not enough money. Money Refunded.")
            elif money_inserted > cost:
                change = money_inserted - cost
                print(f"Here is ${format(change, '.2f')} in change.")
                make_drink(drink)
                money += cost

        else:
            making_coffee = False

# TODO: 2. Enter "off" to turn off machine

    if drink == 'off':
        making_coffee = False

# TODO: 3. Print report
    if drink == 'report':
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${format(money, '.2f')}")







