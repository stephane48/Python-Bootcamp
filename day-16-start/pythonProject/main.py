# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("Coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)

from prettytable import PrettyTable

#Here we are creating the object
table = PrettyTable()

#Add info into a table
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"


print(table)



