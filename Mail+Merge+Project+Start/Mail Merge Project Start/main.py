#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names = open("./Input/Names/invited_names.txt", "r")
names = invited_names.readlines()
# print(names)
invited_names.close()

# Iterate over the list and remove the newline characters from each string
new_name = [name.replace('\n', '') for name in names]

letter = open("./Input/Letters/starting_letter.txt", "r")
new_letter = letter.read()

for name in new_name:
    # Open the file for writing and create it if it doesn't exist
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as invite:
        # Write the original content to the file
        invite.write(new_letter)

    # Open the file for reading
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="r") as invite:
        # Read the content of the file
        contents = invite.read()

    # Replace "[name]" with the current name
    invitation_letter = contents.replace("[name]", name)

    # Open the file for writing
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as invite:
        # Write the modified content back to the file
        invite.write(invitation_letter)



