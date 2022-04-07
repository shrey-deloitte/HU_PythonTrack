class User:
    user={}
    username=""
    password=""

    def createUser(self):
        username=input("Enter Username: ")
        password=input("enter Password: ")
        Repassword=input("enter Password again: ")

        if password==Repassword:
            username=username
            password=password

