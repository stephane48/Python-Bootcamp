# Open the file my_file.txt, with this method
# we do not have to remember to close our file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing inside a file, but it will override the previous content
with open("new_file.txt", mode="w") as file:
    file.write("New text.")

# Writing into a file without overriding its content
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")
