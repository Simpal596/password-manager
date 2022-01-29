from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letter + password_symbol + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    input_password.delete(0, END)
    input_password.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = input_website.get()
    email = input_email.get()
    passw = input_password.get()
    if len(website) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showwarning(title="oops!!!", message="All entries are mandatory.\n Don't left any entry blank")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"email: {email}\npassword: {passw}\nIs it ok?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"Website: {website} | email: {email} | Password: {passw}\n")
            input_website.delete(0, END)
            input_website.focus()
            input_email.delete(0, END)
            input_email.insert(0, "Abhishektiw596@gmail.com")
            input_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200,)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=logo_image)
canvas.grid(row=0, column=1)

# label
label_website = Label(text="Website")
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username")
label_email.grid(row=2, column=0)
label_password = Label(text="password")
label_password.grid(row=3, column=0)

# entry
input_website = Entry(width=35)
input_website.focus()
input_website.grid(row=1, column=1, columnspan=2)
input_email = Entry(width=35)
input_email.insert(0, "Abhishektiw596@gmail.com")
input_email.grid(row=2, column=1, columnspan=2)
input_password = Entry(width=26)
input_password.grid(row=3, column=1, sticky="E")

# buttons
button_generatepass = Button(text="Generate Password", command=pass_generator)
button_generatepass.grid(row=3, column=2)
button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)
window.mainloop()
