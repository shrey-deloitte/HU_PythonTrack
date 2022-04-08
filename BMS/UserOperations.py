from BMS.Movies import userList, tickets


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
        print("User added")


def bookTicket():
    seatsToBeBooked = int(input("Enter the no. of seats to be booked: "))
    if (seatsToBeBooked < tickets['total']):
        tickets['available'] -= seatsToBeBooked
        tickets['remaining'] += seatsToBeBooked
        print("Seats Booked")
    else:
        print("Seats not available")

def cancelTicket():
    seatsToBeCanceled=int(input("enter no. of tickets to be canceled: "))
    if(seatsToBeCanceled<tickets['available']):
        print("cancelling")


