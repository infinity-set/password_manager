from tkinter import *
from tkinter import messagebox
import datetime as date
import pandas
import os
import random as r
import pyperclip
import json
import sys


# ---------------------------- SEARCH FUNCTION ------------------------------- #

# Function to search for a website's information
def search_website():
    # Load password data from the JSON file
    search_dict = load_passwords_from_json("./json_passwords.json")

    # Get the entered website name from the entry field and capitalize it
    web_name = website_entry.get().title()

    # Check if the entered website name is empty
    if len(web_name) == 0:
        return  # Return if the name is empty

    # Check if the entered website name is present in the search dictionary
    if web_name in search_dict:
        # Extract website information from the dictionary
        web_info = search_dict[web_name]

        # Get email, username, and password from the website information, providing default values if missing
        email = web_info.get("email", "N/A")
        username = web_info.get("username", "N/A")
        password = web_info.get("password", "N/A")

        # Copy the password to clipboard for convenience
        pyperclip.copy(password)

        # Create a message with the retrieved information
        message = (
            f"Website: {web_name}\n"
            f"Username: {username}\n"
            f"Email: {email}\n"
            f"Password: {password}\n\n"
        )

        # Show an information dialog with the retrieved message
        messagebox.showinfo(title="Search Result", message=message)
    else:
        # Display a message if the website name was not found in the dictionary
        messagebox.showinfo(title="Search Result", message=f"No entry found for '{web_name}'.")


# Function to load passwords from a JSON file
def load_passwords_from_json(file_path):
    try:
        # Attempt to open and read the JSON file
        with open(file_path) as json_data:
            # Load the JSON content into a dictionary and return it
            return json.load(json_data)
    except FileNotFoundError:
        # If the file is not found, show an info message and return an empty dictionary
        messagebox.showinfo(title="Search Result", message="No password data found.")
        return {}
    except json.JSONDecodeError:
        # If there's an issue with JSON decoding, show an info message and return an empty dictionary
        messagebox.showinfo(title="Search Result", message="Data file is corrupt or improperly formatted.")
        return {}


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# This function generates a password and inserts it into the password entry field.
def generate_password():
    if len(password_entry.get()) == 0:
        # Define character sets for generating passwords
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '!#$%&()*+'

        # Generate password components based on specified counts
        password_list = [r.choice(letters) for _ in range(r.randint(8, 10))]
        password_list += [r.choice(symbols) for _ in range(r.randint(2, 4))]
        password_list += [r.choice(numbers) for _ in range(r.randint(2, 4))]

        # Shuffle the generated password list
        r.shuffle(password_list)

        # Create the final password string
        password = "".join(password_list)

        # Insert the generated password into the password entry field
        password_entry.insert(0, string=password)

        # Copy the generated password to the clipboard
        pyperclip.copy(password)
    else:
        # Clear the existing entry and regenerate the password
        password_entry.delete(0, END)
        generate_password()


# ---------------------------- SAVE PASSWORD ------------------------------- #

# This function displays a verification message to confirm the user's intention to save the entry.
def verify_entry(website, username, email, password):
    # Create the verification message using the entered data
    message = (
        f"Verify your entry:\n\n"
        f"Website: {website}\n"
        f"Username: {username}\n"
        f"Email: {email}\n"
        f"Password: {password}\n\n"
        f"Is it ok to save?"
    )

    # Display a yes-no dialog box with the verification message
    # The function returns True if the user clicks "Yes" and False if they click "No"
    return messagebox.askyesno(title="Verify", message=message)

# This function is responsible for saving the entered website information.
def save():
    # Gather data from the entry fields
    website, username, email, password, timestamp_string = gather_data()

    # Check if the entered data is valid
    if not is_data_valid(website, email, password, username):
        # Display error message for empty fields
        messagebox.showerror(title="Error", message="You cannot have empty fields.")
        return

    # Verify user's intention to save the entry
    ok_to_save = verify_entry(website, username, email, password)
    if not ok_to_save:
        # User chose not to save; return without further action
        return

    # Define a list of save functions and corresponding format names
    save_functions = [
        (save_to_csv, "CSV"),
        (save_to_text_file, "TEXT"),
        (save_to_json, "JSON")
    ]

    for save_function, format_name in save_functions:
        try:
            # Call the appropriate save function for each format
            save_function(website, username, email, password, timestamp_string)
            print(f"Saved {format_name}...\n")
        except:
            # Handle issues that may occur while saving
            messagebox.showwarning(title="Warning", message=f"Could not save {format_name}.")

    # Clear input fields and show success message
    clear_input_fields()
    messagebox.showinfo(title="Complete", message="Files are updated.")

# This function gathers data from the entry fields and generates a timestamp.
def gather_data():
    # Get the entered values from the entry fields
    website = website_entry.get().title()
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Get the current date and generate a timestamp string
    todays_date = date.datetime.now()
    timestamp_string = todays_date.strftime("%b-%d-%Y")

    # Return the gathered data and timestamp
    return website, username, email, password, timestamp_string



# This function checks the validity of the entered data.
def is_data_valid(website, email, password, username):
    # Check if all the entered fields have a length greater than 0
    # This ensures that none of the fields are empty or contain only spaces
    # If all conditions are met, the function returns True, indicating valid data
    return len(website) > 0 and len(email) > 0 and len(password) > 0 and len(username) > 0


# This function saves the entered data to a CSV file.
def save_to_csv(website, username, email, password, timestamp_string):
    # Create a dictionary with the entered data
    data = {
        "Website": [website],
        "Username": [username],
        "Email": [email],
        "Password": [password],
        "Date Created": [timestamp_string]
    }

    # Create a DataFrame using the dictionary
    password_dataframe = pandas.DataFrame(data)
    # Determine the mode for saving the CSV file (append if file exists, write if it doesn't)
    mode = "a" if os.path.isfile("password_doc.csv") else "w"

    # Save the DataFrame to the CSV file, and control whether to include the header
    # The header is included if the file is being created, and not included if the file exists
    password_dataframe.to_csv("password_doc.csv", mode=mode, header=not os.path.isfile("password_doc.csv"))



# This function saves the entered data to a text file.
def save_to_text_file(website, username, email, password, timestamp_string):
    # Open the text file in append mode
    with open("./data.txt", mode="a") as f:
        # Create the entry string with the entered data
        entry = (
            f"Website: {website}  ~  Username: {username}  ~  Email: {email}  ~   Password:|START|>{password}<|FINISH|  ~  Date Created: {timestamp_string}\n\n"
        )

        # Write the entry to the text file
        f.write(entry)



# This function saves the entered data to a JSON file.
def save_to_json(website, username, email, password, timestamp_string):
    # Create a dictionary for the new data entry
    new_data = {
        website: {
            "username": username,
            "email": email,
            "password": password,
            "date": timestamp_string
        }
    }

    try:
        # Try to open the JSON file for reading
        with open("./json_passwords.json", mode="r") as json_file:
            contents = json.load(json_file)
    except FileNotFoundError:
        # If the file doesn't exist, create it and write the new data
        with open("./json_passwords.json", mode="w") as json_file:
            json.dump(new_data, json_file, indent=4)
    else:
        # If the file exists, update its contents with the new data
        contents.update(new_data)
        with open("./json_passwords.json", mode="w") as json_file:
            json.dump(contents, json_file, indent=4)



# This function clears the input fields after data has been saved.
def clear_input_fields():
    # Delete the content of the input fields using their indexes
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    username_entry.delete(0, END)

# Function to exit the program
def exit_program():
    # Use the sys module to gracefully exit the program
    sys.exit()

# ---------------------------- UI SETUP ------------------------------- #

# UI setup function
window = Tk()
window.title("Password Manager")
window.minsize(width=420, height=440)
window.config(padx=20, pady=20, bg="black")

# Create a canvas for displaying the logo image
canvas = Canvas(width=210, height=220, bg="black", highlightthickness=0, highlightbackground="black")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(125, 110, image=lock_img)
canvas.grid(column=1, row=0)

# Create labels, entry fields, and buttons for various UI elements

# Website Label and Entry
website_label = Label(text="Website:", fg="white", bg="red", highlightthickness=1, highlightbackground="white")
website_label.grid(column=0, row=1, pady=1)
website_entry = Entry(width=31, highlightthickness=1, highlightbackground="black")
website_entry.grid(padx=20, column=1, row=1)

# Search Button
search_button = Button(text="Search", width=16, font=("Arial", 9, "bold"), fg="white", bg="red", command=search_website)
search_button.grid(column=2, row=1)

# Username Label and Entry
user_name_label = Label(text="Username:", fg="white", bg="red", highlightthickness=1, highlightbackground="white")
user_name_label.grid(column=0, row=2, pady=10)
username_entry = Entry(width=55, highlightthickness=1, highlightbackground="black")
username_entry.grid(column=1, row=2, columnspan=2)

# Email Label and Entry
email_username_label = Label(text="Email:", fg="white", bg="red", highlightthickness=1, highlightbackground="white")
email_username_label.grid(column=0, row=3)
email_entry = Entry(width=55, highlightthickness=1, highlightbackground="black")
email_entry.grid(column=1, row=3, columnspan=2)

# Password Label and Entry
password_label = Label(text="Password: ", fg="white", bg="red", highlightthickness=1, highlightbackground="white")
password_label.grid(column=0, row=4, pady=10)
password_entry = Entry(width=31, highlightthickness=1, highlightbackground="black")
password_entry.grid(column=1, row=4)

# Generate Password Button
generate_button = Button(text="Generate Password", font=("Arial", 9, "bold"), fg="white", bg="red", command=generate_password)
generate_button.grid(column=2, row=4, padx=10)

# Add Button
add_button = Button(padx=8, text="Add", font=("Arial", 9, "bold"), width=46, fg="white", bg="red", command=save)
add_button.grid(column=1, row=5, columnspan=2)

# Exit Button
quit_button = Button(padx=8, text="EXIT", font=("Arial", 9, "bold"), width=46, fg="white", bg="red", command=exit_program)
quit_button.grid(column=1, row=6, columnspan=2, pady=20)

# Start the main event loop for the GUI
window.mainloop()
