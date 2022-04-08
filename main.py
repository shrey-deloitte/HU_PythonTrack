from BMS.UserOperations import createUser
from BMS.login import login

while True:

    try:
        print("****** Welcome to BMS *******")
        print("1. Login")
        print("2. Register new Account")
        print("3. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(" ")
            print("****** Welcome to Login Page ******")
            print("1. Admin Login")
            print("2. User Login")
            login()

        elif choice == 2:  # register user
            print("")
            print("*** Registering new User ***")
            createUser()

        elif choice == 3:
            exit()

        else:
            print("Invalid input")

    except Exception as e:
        print("Something went wrong! :( --", e)

