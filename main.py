from MainAssignment_BMS.Admin import admin
from MainAssignment_BMS.AdminOperations import adminOperations
from MainAssignment_BMS.Movies import Movie

while True:
    print("****** Welcome to BookMyShow *******")
    print("1. Login")
    print("2. Register new Account")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("****** Welcome to Login Page ******")
        print("1. Admin Login")
        print("2. User Login")

        loginChoice = int(input("Enter your choice: "))

        if loginChoice == 1:
            admin = admin()
            admin.adminLogin()
            adminOperations()



    elif choice == 2:
        print("register user method call")
        # register user

    else:
        exit(0)
