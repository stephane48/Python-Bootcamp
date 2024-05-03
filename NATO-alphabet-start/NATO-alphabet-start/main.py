student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dict = {row[0]: row[1] for (index, row) in pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
phonetic_word = []

word = input("Enter a word: ").upper()
for letter in word:
    if letter in nato_dict:
        phonetic_word.append(nato_dict[letter])

print(phonetic_word)


# for letter in word:
#     print(letter)
#     print(nato_dict.items())
# new_word = word.split("")
# print(new_word)




















