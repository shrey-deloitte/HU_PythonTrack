from MainAssignment_BMS.Movies import Movie


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

    def createMovie(self):
        title = input("Enter the name of Movie: ")
        Movie.Title = title
        Genre = input("Enter the Genre of Movie: ")
        Movie.Genre = Genre
        Length = input("Enter the Length of Movie: ")
        Movie.Length = Length
        Cast = input("Enter the Cast of Movie: ")
        Movie.Cast = Cast
        Director = input("Enter the Director of Movie: ")
        Movie.Director = Director
        AdminRating = input("Enter the AdminRating of Movie: ")
        Movie.AdminRating = AdminRating
        Timings = input("Enter the Timings of Movie: ")
        Movie.Timings = Timings
        UserRating = input("Enter the UserRating of Movie: ")
        Movie.UserRating = UserRating

    def showMovie(self):
        print(Movie.Title)

        print(Movie.Genre)

        print(Movie.Length)

        print(Movie.Title)

        print(Movie.Title)

        print(Movie.Title)

        print(Movie.Title)

        print(Movie.Title)



