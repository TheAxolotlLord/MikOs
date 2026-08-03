from userdata import *
import time
import os
import sys # it won't stop spitting errors unless i import sys (for some odd reason)

# file extensions reading
file_extensions_availiable = (".mkap",".txt","",".py",)
translated_extension = ("MikOS Application", "Read-Only Text File", "Folder", "System File")

# bold and italic varibles
boldstart = '\033[1m'
boldend = '\033[0m'
italicstart = '\x1B[3m'
italicend = '\x1B[23m'

# mail contents
inbox_teto1 = {"sender": "teto", "receiver": "rin", "message": f"RUN BEFORE {italicstart}SHE{italicend} CATCHES YOU"}

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
                if user["user"] == "john_doe":
                    twofa = input("Enter 2FA: ").lower()
                    if twofa == str(32 * user["UID"] * 100):
                        logged_user = user["user"]
                        logged_pass = user["pass"]
                        uid = user["UID"]
                        os.system('cls||clear')
                        main()    
                        return
                    else:
                        os.system('cls||clear')
                        print("HAHA! You can't just try to hack an Admin account like that! Or write down your backup codes. Please, bro.")
                        return login()
                logged_user = user["user"]
                logged_pass = user["pass"]
                uid = user["UID"]
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

# exit command
def exit_term():
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

# open app
def open_app(filename):
    # sets the filepath to the app that will be run
    path = os.path.join("cations", filename)

    # check if valid
    if not os.path.exists(path):
        print("App could not run. ERR: APP_NOT_FOUND")
        return
    # open with "r" as read
    with open(path, "r") as file:
        code = file.read()

    ### run it (i don't know what the namespaces are yet)
    namespace = {"__name__": "__main__"}
    exec(code, namespace)

# all the commands
def commands():
    user_input = input("> ")
    # i got bored here
    if user_input == "passwordget":
        print("Your password: " + logged_pass)
        # does this matter?
        return commands()
    elif user_input == "exit":
        exit_term()
    elif user_input == "help":
        # more like help me, am i right?
        print(f"This is the {boldstart}help{boldend} command.")
        print("exit: Exits MikOS.")
        print("help: This command.")
        print("passwordget: Obtains your password.")
        print("dir: Shows the files in the directory.")
        print("open: Opens a file or folder. To open a file not in the current folder, use a forward slash. (eg: Folder/file.txt)")
        print("logout: Log the user out.")
        commands()
    elif user_input == "dir":
        print("Directory:")
        for app_name in os.scandir("cations"):
            # make sure it's not the pycache
            if str(app_name) != "<DirEntry '__pycache__'>":
                # print the name, and get rid of the weird default directory garbage output stuff
                split_app = str(app_name)[11:(len(str(app_name)) - 2)]
                extension = os.path.splitext(split_app)[1]
                dedicated_ext = "File"
                for ext in file_extensions_availiable:
                    i = 0
                    if ext == extension:
                        dedicated_ext = translated_extension[i]
                        i += 1

                print(" "*4 + "'" + split_app + "' - " + dedicated_ext)  
        commands()
    # elif user_input == "open mail.mkap":
    #     print("Sorry, but you can't do that right now.")
    #     commands()
    # elif user_input == "open terminal.mkap":
    #     print("This application is already open.")
    #     commands()
    # elif user_input == "open writer.mkap":
    #     print("Sorry, but you can't do that right now.")
    #     commands()
    # elif user_input == "open userdata.py":
    #     print(f"You must have the role {italicstart}SYS_OP{italicend} to do that.")
    #     commands()
    # elif user_input == "open SentMail":
        # make function called openFolder(input)
    #     if logged_user == "teto":
    #         print("There is 1 item(s) in this folder:")
    #         print("untitled1.mail")
    #         commands()
    #     else:
    #         print("There is 1 item(s) in this folder:")
    #         print("[HIDDEN_ITEM]")
    #         commands()
    # elif user_input == "open ReceivedMail":
    #     if logged_user == "rin":
    #         print("There is 1 item(s) in this folder:")
    #         print("untitled1.mail")
    #         commands()
    #     else:
    #         print("There is 1 item(s) in this folder:")
    #         print("[HIDDEN_ITEM]")
    #         commands()
    # elif user_input == "open SentMail/untitled1.mail":
    #     if logged_user == "teto":
    #         print("You already sent that mail.")
    #         commands()
    #     else:
    #         print("Command not found.")
    #         commands()
    # elif user_input == "open ReceivedMail/untitled1.mail":
    #     if logged_user == "rin":
    #         print("Mail Contents:")
    #         print("From: " + inbox_teto1["sender"])
    #         print("To: " + inbox_teto1["receiver"])
    #         print("Subject: " + inbox_teto1["message"])
    #         commands()
    #     else:
    #         print("Command not found.")
    #         commands()
    elif user_input == "logout":
        os.system('cls||clear')
        login()
    elif user_input.startswith("open ") and user_input != "open ":
        open_app(user_input.split()[1])
        commands()
    else:
        print("Command not found.")
        commands()

login()
