from MainAssignment_BMS.Admin import admin
from MainAssignment_BMS.AdminOperations import adminOperations
from MainAssignment_BMS.User import User


def login():
    loginChoice = int(input("Enter your choice: "))

    if loginChoice == 1:
        admin1 = admin()
        admin1.adminLogin()
        adminOperations()

    elif loginChoice == 2:
        user1 = User()
        user1.userLogin()