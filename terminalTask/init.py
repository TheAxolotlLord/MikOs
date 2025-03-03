from userdata import *
import time
import os

# bold and italic varibles
boldstart = '\033[1m'
boldend = '\033[0m'
italicstart = '\x1B[3m'
italicend = '\x1B[23m'
# mail contents
mail_1 = {"sender": "teto", "receiver": "rin", "message": f"RUN BEFORE {italicstart}SHE{italicend} CATCHES YOU"}

# login function
def login():
    global logged_user
    global logged_pass
    print("Welcome to the MikOS!")
    time.sleep(1)
    username = input("Username: ").lower()
    for user in users_data:
        if user["user"] == username:
            password = input("Password: ").lower()
            if user["pass"] == password:
                logged_user = user["user"]
                logged_pass = user["pass"]
                os.system('cls||clear')
                main()
                return
            else:
                os.system('cls||clear')
                print("Incorrect Password.")
                return login()
    os.system('cls||clear')
    print("No Username Found.")
    return login()

# greet function
def main():
    print(f"Hello, {boldstart}{logged_user.title()}{boldend}!")
    print("Enter a command to continue.")
    commands()

def calc():
    print("Welcom to the Calc App!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplcation")
    print("4. Division")
    calc_input = input("")
    if calc_input == "1":
        while True:
            # some try-excepts so you wont enter a string
            try:
                num_1 = input(int("Enter your first number: "))
                break
            except ValueError:
                print("Please enter a number.")
            try:
                num_2 = input(int("Enter your second number: "))
                break
            except ValurError:
                print("Please enter a number.")
            ans = num_1 + num_2
            print(f"The answer is {ans}.")
            print("Sending you back to the terminal.")
            commands()
                
    elif calc_input == "2":
        print("so i havent coded that yet here's the terminal")
        commands()
    elif calc_input == "3":
        print("so i havent coded that yet here's the terminal")
        commands()
    elif calc_input == "4":
        print("so i havent coded that yet here's the terminal")
        commands()
    else:
        print("Command not found.")
        time.sleep(.4)
        print("Calculator exited.")
        commands()

# all the commands
def commands():
    user_input = input("> ")
    # i got bored here
    if user_input == "passwordget":
        print("Your password: " + logged_pass)
        # does this matter?
        return commands()
    elif user_input == "exit":
        user_input = input("Are you sure? (Y/N) ").upper()
        if user_input == "Y":
            # clears the system
            os.system('cls||clear')
            os._exit(0)
        elif user_input == "N":
            commands()
        else:
            print("Command not found.")
            commands()
    elif user_input == "help":
        # more like help me, am i right?
        print(f"This is the {boldstart}help{boldend} command.")
        print("exit: Exits MikOS.")
        print("help: This command.")
        print("passwordget: Obtains your password.")
        print("dir: Shows the files in the directory.")
        print("open: Opens a file or folder. To open a file not in the current folder, use a forward slash. (eg: Folder/file.txt)")
        print("logout: Log the user out.")
        print("calc: Opens the Calc App.")
        commands()
    elif user_input == "dir":
        print("Directory:")
        print(" "*4 + "mail.app")
        print(" "*4 + "terminal.app")
        print(" "*4 + "writer.app")
        print(" "*4 + "userdata.txt")
        print(" "*4 + "ReceivedMail")
        print(" "*4 + "SentMail")
        commands()
    elif user_input == "open mail.app":
        print("Sorry, but you can't do that right now.")
        commands()
    elif user_input == "open terminal.app":
        print("This application is already open.")
        commands()
    elif user_input == "open writer.app":
        print("Sorry, but you can't do that right now.")
        commands()
    elif user_input == "open userdata.txt":
        print(f"You must have the role {italicstart}SYS_OP{italicend} to do that.")
        commands()
    elif user_input == "open SentMail":
        # make function called openFolder(input)
        if logged_user == "teto":
            print("There is 1 item(s) in this folder:")
            print("untitled1.mail")
            commands()
        else:
            print("There is 1 item(s) in this folder:")
            print("[HIDDEN_ITEM]")
            commands()
    elif user_input == "open ReceivedMail":
        if logged_user == "rin":
            print("There is 1 item(s) in this folder:")
            print("untitled1.mail")
            commands()
        else:
            print("There is 1 item(s) in this folder:")
            print("[HIDDEN_ITEM]")
            commands()
    elif user_input == "open SentMail/untitled1.mail":
        if logged_user == "teto":
            print("You already sent that mail.")
            commands()
        else:
            print("Command not found.")
            commands()
    elif user_input == "open ReceivedMail/untitled1.mail":
        if logged_user == "rin":
            print("Mail Contents:")
            print("From: " + mail_1["sender"])
            print("To: " + mail_1["receiver"])
            print("Subject: " + mail_1["message"])
            commands()
        else:
            print("Command not found.")
            commands()
    elif user_input == "logout":
        os.system('cls||clear')
        login()
    elif user_input == "calc":
        calc()
    else:
        print("Command not found.")
        commands()

login()
