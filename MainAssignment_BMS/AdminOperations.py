from MainAssignment_BMS.Movies import movieList
from MainAssignment_BMS.welcomePage import welcome


def addMovie():
    print(" ")
    print("")
    print("adding movie")
    print("")
    movie_dic = {}
    title = input("Enter the name of Movie: ")
    movie_dic['Title'] = title

    Genre = input("Enter the Genre of Movie: ")
    movie_dic["Genre"] = Genre

    Length = input("Enter the Length of Movie: ")
    movie_dic["Length"] = Length

    Cast = input("Enter the Cast of Movie: ")
    movie_dic["Cast"] = Cast

    Director = input("Enter the Director of Movie: ")
    movie_dic["Director"] = Director

    AdminRating = input("Enter the AdminRating of Movie: ")
    movie_dic["AdminRating"] = AdminRating

    Timings = input("Enter the Timings of Movie: ")
    movie_dic["Timings"] = Timings

    UserRating = input("Enter the UserRating of Movie: ")
    movie_dic["UserRating"] = UserRating

    movieList.append(movie_dic)

    print("new movie added", movie_dic)
    print(movieList)

    adminOperations()


def editMovie():
    print("")
    print("")
    print("Editing movie ")
    editChoice = input("Enter which movie you want to edit: ")
    for item in movieList:
        t = item.get("Title")
        if t != editChoice:
            print("Invalid choice! please provide correct details")
            editMovie()
        else:
            print(" ")
            print("1. Title")
            print("2. Genre")
            print("3. Length")
            print("4. Cast")
            print("5. Director")
            print("6. AdminRating")
            print("7. Timings")
            print("8. UserRating")
            eleChoice = int(input("which element you want to update: "))
            try:
                if (eleChoice == 1):
                    newTitle = input("enter new title: ")
                    item['Title'] = newTitle
                elif (eleChoice == 2):
                    newGenre = input("enter new genre: ")
                    item["Genre"] = newGenre
                elif (eleChoice == 3):
                    newLength = input("Enter new length: ")
                    item["Length"] = newLength
                elif (eleChoice == 4):
                    newCast = input("Enter new cast: ")
                    item["Cast"] = newCast
                elif (eleChoice == 5):
                    newDirector = input("Enter new director: ")
                    item["Director"] = newDirector
                elif (eleChoice == 6):
                    newAdminRating = input("Enter new AdminRating: ")
                    item["AdminRating"] = newAdminRating
                elif (eleChoice == 7):
                    newTimings = input("Enter new Timings: ")
                    item["Timings"] = newTimings
                elif (eleChoice == 8):
                    newUserRating = input("Enter new UserRating: ")
                    item["UserRating"] = newUserRating
                else:
                    print("Invalid Choice!")
            except:
                print("Something went wrong !")
            print(movieList)
            print("Updated! ")
            return adminOperations()





def deleteMovie():
    print("Delete movie")
    delete=input("which movie you want to delete: ")
    index=0
    for item in movieList:
        t = item.get("Title")
        if(t!= delete):
            print("Movie not found! ")
            print(movieList)
            deleteMovie()

        else:

            movieList.pop(index)
            print(movieList)
            print("movie deleted!")
            return adminOperations()



def logout():
    print("Logged Out")
    return welcome()


def adminOperations():
    print("****** Welcome Admin ******* ")
    print("1. Add New Movie Info ")
    print("2. Edit Movie Info ")
    print("3. Delete Movies ")
    print("4. Logout ")

    adminChoice = int(input("Enter your choice: "))

    if adminChoice == 1:
        addMovie()

    elif adminChoice == 2:
        editMovie()

    elif adminChoice == 3:
        deleteMovie()

    elif adminChoice == 4:
        logout()

    else:
        print("Invalid input!")
