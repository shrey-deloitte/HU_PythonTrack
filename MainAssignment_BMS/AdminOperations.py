def addMovie():
    print("adding movie")


def editMovie():
    print("editing movie ")


def deleteMovie():
    print("deleting movie")


def logout():
    print("logout ")


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
