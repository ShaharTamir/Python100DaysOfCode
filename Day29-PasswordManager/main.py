from tkinter import *
from tkinter import messagebox
import password_generator
import json

COLOR = "white"
CANVAS_HEIGHT = 200
CANVAS_WIDTH = 200
IMG_HEIGHT = 100
IMG_WIDTH = 100
LONG_WIDTH = 40
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_password():
    new_password = password_generator.gen_password(n_letters=8, n_numbers=2, n_symbols=3)
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    password_entry.clipboard_clear()
    password_entry.clipboard_append(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_entries():
    entries = [web_entry, password_entry]
    for entry in entries:
        entry.delete(0, END)
    web_entry.focus()


def validate_data(*args):
    invalid = ""
    for arg in args:
        if arg == invalid:
            return False
    return True


def verify_before_adding_data(website, email, password):
    summary_str = f"These are the details entered: \n\
Email: {email}\nPassword: {password}\nIs it ok to save?"
    is_ok = messagebox.askokcancel(title=website, message=summary_str)
    return is_ok


def save_password():
    website = web_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()

    if validate_data(website, email, password):
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        if verify_before_adding_data(website, email, password):
            all_data = None
            try:
                with open("saved_passwords.json", "r") as pass_file:
                    all_data = json.load(pass_file)
                    all_data.update(new_data)
            except FileNotFoundError:
                all_data = new_data
            finally:
                with open("saved_passwords.json", "w") as pass_file:
                    json.dump(all_data, pass_file, indent=4)

            clear_entries()

    else:
        error_string = "*All fields are required!"
        messagebox.showerror(message=error_string)


# ------------------------- SEARCH PASSWORD --------------------------- #
def search_password():
    website = web_entry.get()

    if validate_data(website):
        try:
            with open("saved_passwords.json", "r") as pass_file:
                data = json.load(pass_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found!")
        else:
            if website in data:
                web_data = data[website]
                info_str = f"Email: {web_data['email']}\nPassword: {web_data['password']}"
                messagebox.showinfo(message=info_str, title=website)
            else:
                messagebox.showerror(title="Error", message="Website not found!")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(pady=20, padx=20, background=COLOR)

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=COLOR, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
logo = canvas.create_image(IMG_WIDTH, IMG_HEIGHT, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:", bg=COLOR)
web_label.grid(row=1, column=0)
user_name_label = Label(text="Email/Username:", bg=COLOR, padx=5)
user_name_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=COLOR)
password_label.grid(row=3, column=0)
error_label = Label(text="", bg=COLOR, fg="red", font=("ariel", 10, "bold"))
error_label.grid(row=5, column=1, columnspan=2)

# Entries
web_entry = Entry(width=23)
web_entry.grid(row=1, column=1, columnspan=1)
user_name_entry = Entry(width=LONG_WIDTH)
user_name_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, padx=1, command=search_password)
search_button.grid(row=1, column=2, sticky=W)
gen_password_button = Button(text="Generate Password", padx=1, command=gen_password)
gen_password_button.grid(row=3, column=2, sticky=W)
add_button = Button(text="Add", width=LONG_WIDTH - 2, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

web_entry.focus()
user_name_entry.insert(END, "shahar1360@gmail.com")
window.mainloop()
