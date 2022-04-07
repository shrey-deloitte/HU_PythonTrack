from MainAssignment_BMS.Movies import userList


class User:

    def userLogin(self):
        print(" ")
        print("****** Welcome User ******* ")
        username = input("Enter Username: ")
        password = input("enter Password: ")
        try:
            for user in userList:
                if (user['username'] == username and user['password'] == password):
                    print("loggedin! :)")
                else:
                    print("user not found")
        except:
            print("Something went wrong :(")



