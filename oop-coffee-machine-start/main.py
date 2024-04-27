from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

#Create an instance of the Menu class
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


while is_on:
  choice = input(f"What would you like? ({menu.get_items()}): ")
  if choice == "off":
      is_on = False
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
