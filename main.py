from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

coffee = True
while coffee:
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}: ")
    drink = user_choice

    if user_choice == "off":
        coffee = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if (coffee_maker.is_resource_sufficient(drink)
                and money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)