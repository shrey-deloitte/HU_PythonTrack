
class admin:
    __username = "admin"
    __password = "admin"

    def getUsername(self):
        username = self.__username
        return self.__username

    def getPassword(self):
        password = self.__password
        return self.__password

    def adminLogin(self):

        while True:
            userName = input("Enter Username: ")
            password = input("Enter Password: ")
            if userName == self.__username and password == self.__password:
                print("Login Successful! ")
                return

            else:
                print("Wrong Credentials! ")







