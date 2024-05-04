from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    # Retrieve text from Entry widgets
    website = website_input.get()
    email_or_username = email_or_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email_or_username,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            # If the file doesn't exist, create it and write new data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear entry fields
            website_input.delete(0, 'end')
            # email_or_username_input.delete(0, 'end')
            password_input.delete(0, 'end')


# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)  #half of the width and height
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()  #this is to place the cursor on this entry

email_or_username_label = Label(text="Email/Username:")
email_or_username_label.grid(column=0, row=2)

email_or_username_input = Entry(width=35)
email_or_username_input.grid(column=1, row=2, columnspan=2)
email_or_username_input.insert(0, "stephanekamdem09@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
