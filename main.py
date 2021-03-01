from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "login": login,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(login) == 0:
        messagebox.showerror(title="Oops", message="Please make sure to fill every fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading current data
                data = json.load(data_file)
        except FileNotFoundError:
            # json file doesn't exist, no data to read, creating the file with new_data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating existing data with new one
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # writing the file with all data
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        messagebox.showinfo(title="Success", message=f"The details for {website} have been saved.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, pady=2)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, pady=2)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW", pady=2)
website_entry.focus()

login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2, pady=2)
login_entry = Entry(width=35)
login_entry.grid(column=1, row=2, columnspan=2, sticky="EW", pady=2)
login_entry.insert(0, "krall@hotmail.com")


password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=2)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW", pady=2)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW", pady=2)

Add_button = Button(text="Add", width=35, command=save)
Add_button.grid(column=1, row=4, columnspan=2, sticky="EW", pady=2)

window.mainloop()
