# Programmer: Landon Harter
# Date: 10/12/2021
# Program: Bank Transaction

def checkpin(pin : str):
  pinLength = len(pin)

  if pinLength != 4:
    return False

  if pin.isnumeric() is False:
    return False

  return True

def requestpin(validPin : str):
  pin = input("Enter pin: ")

  if pin == validPin: return True

  return False

def printseparator():
  print("\n*************************************************\n")

print("Welcome to PythonBank\nLet's take a moment to set up your account.\n")

# Set up account and a security pin
firstName = input("What is your first name: ")
lastName = input("What is your last name: ")

printseparator()

print(f"\nWelcome to Cash R Us {firstName} {lastName}, we will now need to set up security pin on your account.\n")

printseparator()

pin = ""
while checkpin(pin) is False:
  pin = input("Please choose a 4 digit security pin: ")

  if checkpin(pin) is False: print("Pin is invalid, make sure it is 4 numbers.")

havemoney = True

print(f"\nThank you {firstName}, we see that you set your pin to {pin}")

printseparator()

print("Use the help command to see all commands. \n")

inBank = True
amountOfMoney : float = 0.00

while inBank:
  atm = input("ATM>")

  if atm == "quit":
    inBank = False
    break

  printseparator()

  if atm == "help":
    print("deposit - Deposits a specified amount of money into your account")
    print("withdraw - Withdraws a specified amount of money from your account")
    print("balance - Provides your current balance")
    print("quit - Exits the ATM terminal")

  elif atm == "deposit":
    if requestpin(pin):
      amountToDeposit = input("Amount to deposit: ")

      if amountToDeposit.isnumeric() is False and amountToDeposit.__contains__(".") is False:
        print("Amount is invalid.")
      else:
        amountToDepositf = float(amountToDeposit)
        amountOfMoney += amountToDepositf
        print(f"Balance: ${amountOfMoney}")

  elif atm == "withdraw":
    if requestpin(pin):
      amountToWithdraw = input("Amount to withdraw: ")

      if amountToWithdraw.isnumeric() is False and amountToDeposit.__contains__(".") is False:
        print("Amount is invalid.")
      else:
        amountToWithdrawf = float(amountToWithdraw)
        amountOfMoney -= amountToWithdrawf
        print(f"Balance: ${amountOfMoney}")

  elif atm == "balance":
    print(f"Balance: {amountOfMoney}")

  else:
      print("Invalid command.")

  printseparator()