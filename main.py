from tkinter import *

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {login} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)



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
