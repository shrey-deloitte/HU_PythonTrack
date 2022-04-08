from BMS.Admin import admin
from BMS.AdminOperations import adminOperations
from BMS.User import User


def login():
    loginChoice = int(input("Enter your choice: "))

    if loginChoice == 1:
        admin1 = admin()
        admin1.adminLogin()
        adminOperations()

    elif loginChoice == 2:
        user1 = User()
        user1.userLogin()
