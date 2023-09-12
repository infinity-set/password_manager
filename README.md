# Password Manager GUI

![Password Manager Logo](https://github.com/infinity-set/password_manager/assets/142350896/3da99247-e0d5-4ac9-b9ee-c489dc39784f)

This is a simple password manager application built using the Tkinter library in Python. The application allows you to manage website information including website names, usernames, emails, and passwords. It provides features such as searching for stored website information, generating passwords, and saving entered data to different formats.

## Table of Contents

- [Features](#features)
- [Why Use This Script?](#why-use-this-script)
- [Languages and Utilities Used](#languages-and-utilities-used)
- [Environments Used](#environments-used)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Program Walk-Through](#program-walk-through)

## Features

- **Search Function:** You can search for stored website information using the website name. The application retrieves and displays the corresponding username, email, and password if the website entry is found.

- **Password Generator:** You can generate secure passwords using the password generator feature. The generated password can be copied to the clipboard for ease of use.

- **Data Saving:** The application allows you to save entered website information. You can verify the entered data before saving. The saved data can be stored in three different formats: CSV, text file, and JSON.

## Why Use This Script?

The Password Manager script offers a convenient solution for individuals looking to manage their website credentials and access them securely. Here are a few reasons why you might consider using this script:

- **Simplified Management**: With the Password Manager, you can centralize all your website login details in one place, making it easier to locate and access your credentials whenever you need them.

- **Secure Password Generation**: The built-in password generator allows you to create strong and secure passwords tailored to your preferences. You can ensure that your online accounts are protected with complex passwords that are harder to crack.

- **Clipboard Convenience**: Searching for website information using the script's 'Search' feature not only retrieves the necessary details but also automatically copies the password to your clipboard. This streamlined process eliminates the hassle of manually typing or copying passwords, enhancing both efficiency and security.

- **Multiple Formats for Data Storage**: The script provides the flexibility to save your entered data in various formats, including CSV, text files, and JSON. This allows you to choose the format that best suits your preferences and needs.

- **User-Friendly Interface**: The graphical user interface (GUI) created with Tkinter ensures a user-friendly experience. You don't need to be an expert in programming or command-line interfaces to utilize the script effectively.

- **Customizable Entries**: The script lets you store not only website names, usernames, and passwords but also additional information such as email addresses. This level of customization ensures that you can store comprehensive website details in one place.

- **Offline Access**: Unlike some online password managers, this script provides you with offline access to your stored credentials. This can be especially helpful in scenarios where you don't have internet connectivity.

- **Open Source and Customizable**: The script is open-source, meaning you can modify and extend its functionality according to your specific requirements. Whether you want to add new features or tailor it to your workflow, you have the freedom to do so.

By using this script, you can streamline your password management process, enhance the security of your online accounts, and enjoy the convenience of easy and quick access to your credentials.


## Languages and Utilities Used

- **Python**
- **PyCharm**

[<img align="center" alt="PyCharm Icon" width="50px" src="https://upload.wikimedia.org/wikipedia/commons/1/1d/PyCharm_Icon.svg" />][pycharm]
[<img align="left" alt="Python Icon" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" />][python]

[pycharm]: https://www.jetbrains.com/pycharm/
[python]: https://www.python.org/

## Environments Used

- **Windows 10**

[<img align="left" alt="Microsoft Icon" width="35px" src="https://upload.wikimedia.org/wikipedia/commons/3/34/Windows_logo_-_2012_derivative.svg" />][windows]

[windows]: https://www.microsoft.com/
<br /><br />

## Dependencies

The Password Manager application relies on the following Python libraries:

- **Tkinter:** Tkinter is the standard GUI library that comes bundled with Python. It provides the necessary tools to create graphical user interfaces for desktop applications.

- **datetime:** The datetime module is used for working with dates and times. It's used in the application to generate timestamps for saved entries.

- **pandas:** The pandas library is used to work with data in tabular form. It's used to create and manage data in CSV format.

- **os:** The os module provides a way to interact with the operating system. In the application, it's used to check if files exist before saving data.

- **random:** The random module is used to generate random values, such as generating random characters for passwords.

- **pyperclip:** The pyperclip library allows copying and pasting text to and from the clipboard. It's used to copy generated passwords to the clipboard for user convenience.

- **json:** The json module is used to work with JSON (JavaScript Object Notation) data. In the application, it's used to load and save password data in JSON format.

- **sys:** The sys module provides access to some variables used or maintained by the Python interpreter. It's used to gracefully exit the program when the user chooses to quit.

## Usage

1. Run the script ***password_manager.py*** using a Python interpreter.
2. The application window will open, displaying the GUI for the password manager.
3. Enter website information including website name, username, email, and password.
4. Use the "Generate Password" button to generate a secure password if needed.
5. Click the "Add" button to save the entered data. You will be asked to verify the entered data before saving.
6. Utilize the "Search" button to retrieve stored website information. Upon a successful search, the password will be seamlessly **copied** to the clipboard, requiring ***only a paste action*** for easy use.


## Program Walk-Through

<p align="center">
<b>Launch PyCharm and Run the file "key_logger.py":</b>
<br/>  
<br/>
<img src="https://github.com/infinity-set/password_manager/assets/142350896/a700e033-7962-430c-90a6-c683dc548c3e" height="80%" width="80%" alt="Run PyCharm File"/>
<br />
<br />
<b>Fill in fields. Click "Generate Password". Click "Add". Verify your entry and accept:</b>
<br/>
<br/>
<img src="https://github.com/infinity-set/password_manager/assets/142350896/7268f7ef-cc19-4f0d-becd-0cf03fb52cfc" height="80%" width="80%" alt="Encryption Steps"/>
<br />
<br />
<b>Terminal will print if file format updates were succesfull:</b>
<br/>
<br/>
<img src="https://github.com/infinity-set/password_manager/assets/142350896/1b42d023-2a24-4c45-9fc0-bbe69ce73417" height="80%" width="80%" alt="Encryption/Decryption Key"/>
<br/>  
<br />
<b>Three file formats are creatd in the same directory, text, JSON, and CSV:</b>
<br/>
<br/>
<img src="https://github.com/infinity-set/password_manager/assets/142350896/43e917ba-89a2-49e4-9efa-cb405b812a0e" height="80%" width="80%" alt="Encryption Steps"/>
<br />
<br />
<b>Text file sample:</b>
<br/>
<br/>
<img src="https://github.com/infinity-set/password_manager/assets/142350896/dd6c66ab-4760-4726-8c07-266a3b6ca17b" height="80%" width="80%" alt="Encryption Steps"/>
<br />
<br />
<b>JSON file sample:</b>
<br/>
<br/>
<img src="https://github.com/infinity-set/password_manager/assets/142350896/88f9a41b-4c1a-4dde-9c81-ff6404f9ccdf" height="80%" width="80%" alt="Encryption Steps"/>
<br />
<br />
<b>CSV file sample:</b>
<br/>
<br/>
<img src="https://github.com/infinity-set/password_manager/assets/142350896/863963c5-af73-4f87-b5ea-8b3c2dc4a469" height="80%" width="80%" alt="Encryption Steps"/>
<br />
<br />
<b>Passwords are instantly copied to your clipboard upon successful search. <i></i>Simply paste where desired</i>:</b>
<br/>
<br/>
<img src="https://github.com/infinity-set/password_manager/assets/142350896/9a9b861e-9542-42a2-be85-bbea473c1175" height="80%" width="80%" alt="Encryption Steps"/>
<br />
<br />
<b>Click "Exit" to end program:</b>
<br/>
<br/>
<img src="https://github.com/infinity-set/infinity-set/assets/142350896/5cdcbd7a-54ee-4e5f-8e59-86cd9b2dfd16" height="80%" width="80%" alt="Encryption Steps"/>
  
</p>
