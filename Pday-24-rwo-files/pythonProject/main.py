# Open the file my_file.txt, with this method
# we do not have to remember to close our file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing inside a file, but it will override the previous content
with open("baba_file.txt", mode="r") as file:
    file.write("New text.")

# Writing into a file without overriding its content
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")


# with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
#     names = invited_names.readlines()
#     for name in names:
#         print(name)

# invited_names = open("./Input/Names/invited_names.txt", "r")
# names = invited_names.readline()
# # for name in names:
# print(names)

# for name in names:
#     print(names)
    # letter = open(f"./Input/Letters/letter_for_{name}.txt", "w")
    # replace_name = str(letter)
    # new_letter = replace_name.replace("[name]", names[0])
    # letter.close()
