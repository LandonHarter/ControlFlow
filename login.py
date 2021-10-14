import datetime
import os

def registeruser(username : str, password : str, pin : str, firstName : str, lastName : str):
    if os.path.exists(f"Users/{username}/"):
        return False

    os.mkdir(f"Users/{username}/")

    writevariable(f"Users/{username}/password.bankdata", password)
    writevariable(f"Users/{username}/pin.bankdata", pin)
    writevariable(f"Users/{username}/money.bankdata", "0.00")
    writevariable(f"Users/{username}/information.bankdata", f"{firstName} {lastName}")
    writevariable(f"Users/{username}/log.banklog", f"User created at {datetime.date.today().ctime()}\n")

def loginuser(username : str, password : str):
    if os.path.exists(f"Users/{username}/") is False:
        return False

    if password == readvariable(f"Users/{username}/password.bankdata"):
        log(username, f"User logged in at {datetime.date.today().ctime()}")
        return True
    else:
        return False

def retrievepin(username : str):
    if os.path.exists(f"Users/{username}/") is False:
        return None

    with open(f"Users/{username}/pin.bankdata", "r") as file:
        return file.read()

    return None

def retrievemoney(username : str):
    if os.path.exists(f"Users/{username}/") is False:
        return 0

    with open(f"Users/{username}/money.bankdata", "r") as file:
        return float(file.read())

    return 0

def writemoney(username : str, amountOfMoney : float):
    writevariable(f"Users/{username}/money.bankdata", str(amountOfMoney))

def writevariable(variablePath : str, data : str):
    with open(variablePath, "w") as file:
        file.write(data)

def readvariable(variablePath : str):
    with open(variablePath, "r") as file:
        return file.read()

    return None

def log(username : str, log : str):
    with open(f"Users/{username}/log.banklog", "a") as file:
        file.write(f"{log}\n")