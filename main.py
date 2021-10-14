# Programmer: Landon Harter
# Date: 10/12/2021
# Program: Bank Transaction
import datetime
import sys

import login

username = ""

def checkpin(pin : str):
    pinLength = len(pin)

    if pinLength != 4:
        return False

    if pin.isnumeric() is False:
        return False

    return True


def requestpin():
    pin = input("Enter pin: ")

    if pin == login.retrievepin(username): return True

    return False


def printseparator():
    print("\n*************************************************\n")


print("Welcome to PythonBank\nLet's take a moment to set up your account.\n")

loginOrRegister = input("Login or register? [l/r]: ")

if loginOrRegister == "r":
    firstName = input("What is your first name: ")
    lastName = input("What is your last name: ")
    username = input("What would you like your username to be: ")
    password = input("What would you like your password to be: ")

    printseparator()

    print(f"\nWelcome to Cash R Us, {firstName} {lastName}, we will now need to set up security pin on your account.\n")

    printseparator()

    pin = ""
    while checkpin(pin) is False:
        pin = input("Please choose a 4 digit security pin: ")

        if checkpin(pin) is False: print("Pin is invalid, make sure it is 4 numbers.")

    login.registeruser(username, password, pin, firstName, lastName)

elif loginOrRegister == "l":
  username = input("Username: ")
  password = input("Password: ")

  loggedIn = login.loginuser(username, password)
  if loggedIn is False:
    print("Failed to log in.")
    sys.exit(0)

  print("Logged in!")

else:
    print("That is not a valid answer.")
    sys.exit(0)

printseparator()

havemoney = True

print("Use the help command to see all commands. \n")

inBank = True
amountOfMoney : float = login.retrievemoney(username)

while inBank:
    atm = input("ATM> ")

    if atm == "quit":
        login.log(username, f"User quit the ATM at {datetime.date.today().ctime()}")

        inBank = False
        break

    printseparator()

    if atm == "help":
        print("deposit - Deposits a specified amount of money into your account")
        print("withdraw - Withdraws a specified amount of money from your account")
        print("balance - Provides your current balance")
        print("quit - Exits the ATM terminal")

    elif atm == "deposit":
        if requestpin():
            amountToDeposit = input("Amount to deposit: ")

            if amountToDeposit.isnumeric() is False and amountToDeposit.__contains__(".") is False:
                print("Amount is invalid.")
            else:
                amountToDepositf = float(amountToDeposit)
                amountOfMoney += amountToDepositf

                login.writemoney(username, amountOfMoney)
                login.log(username, f"User deposited {amountToDepositf} at {datetime.date.today().ctime()}")

                print(f"Balance: ${amountOfMoney}")

    elif atm == "withdraw":
        if requestpin():
            amountToWithdraw = input("Amount to withdraw: ")

            if amountToWithdraw.isnumeric() is False and amountToDeposit.__contains__(".") is False:
                print("Amount is invalid.")
            else:
                amountToWithdrawf = float(amountToWithdraw)
                amountOfMoney -= amountToWithdrawf

                login.writemoney(username, amountOfMoney)
                login.log(username, f"User withdrew {amountToWithdrawf} at {datetime.date.today().ctime()}")

                print(f"Balance: ${amountOfMoney}")

    elif atm == "balance":
        login.log(username, f"User checked balance at {datetime.date.today().ctime()}")
        print(f"Balance: {amountOfMoney}")

    else:
        print("Invalid command.")

    printseparator()
