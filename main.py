from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(5, 7)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    for i in range(nr_letters):
        password_list.append(random.choice(letters))
    for i in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for i in range(nr_numbers):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)

    password = " "
    for i in password_list:
        password += i


    password_entry.insert(0, password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = mail_user_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Ea MAGIA", message="BANDA CHUKI KI SABU JAKA FILL KARA RA PUA")
    else:
        is_ok = messagebox.askokcancel(title = website, message=f"There is a detail entered :\nEmail: {email}\nPassword: {password}\nis it ok to save")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                web_entry.delete(0, END)

                password_entry.delete(0, END)








# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

web_label = Label(text = "Website:")
web_label.grid(column = 0, row = 1)
web_entry = Entry(width = 35 )
web_entry.grid(column = 1, row = 1,columnspan = 2)

mail_user_label = Label(text = "Mail /Username:")
mail_user_label.grid(column = 0, row = 2)
mail_user_entry = Entry(width = 35)
mail_user_entry.insert(0,"rudraprasadhotta@gmail.com")

mail_user_entry.grid(column = 1, row = 2,columnspan = 2)
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

generate_button = Button(text = "Generate Password",command = password_generator)
generate_button.grid(column = 2, row = 3)
add_button = Button(text = "Add",width = 36, command = save)
add_button.grid(column = 1, row = 4,columnspan = 2)

canvas = Canvas( width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image( 100,100, image=lock_image )
canvas.grid(column = 1, row = 0)
window.mainloop()