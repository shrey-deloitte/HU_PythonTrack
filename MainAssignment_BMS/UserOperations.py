from MainAssignment_BMS.Movies import userList


def createUser():
    user = {}
    username = input("Enter Username: ")
    user["username"] = username
    email = input("Enter Email: ")
    user["email"] = email
    phone = input("Enter Contact: ")
    user['contact'] = phone
    age = input("Enter Age: ")
    user['age'] = age
    password = input("enter Password: ")
    Repassword = input("enter Password again: ")
    if (password == Repassword):
        user["password"] = password
        userList.append(user)