# simple login system with dictionary

database = {}

def checker(x):
    return x in database.keys()
#for login
def login():
    x = input("Username:")
    if not checker(x):
        return 0
    y = input("Password: ")
    if y == database[x]["password"]:
        return x
    else:
        return -1
#for register
def fun2():
    x = input("Username:")
    if checker(x):
        return -1
    y = input("New Password: ")
    z = input("Now enter your secrete phrase for safekeeping: ")
    database[x] = {"password": y, "secret": z}
    return 1
def printingOutAllChoicesAndReturnUserChoice():
    print("\nWhat would you like to do?")
    print("1) Login ")
    print("2) Register")
    print("3) Exit\n")
    v = int(input("> "))
    print("")
    return v
while True: #loop runs forever till break
    c = printingOutAllChoicesAndReturnUserChoice()
    match c:
        case 1:

            s = fun2()
            if s == 0:
                print("error: username not found")
            elif s == -1:
                print("error: incorrect password")
            else:
                print(f"\nWelcome back, {s}!")
                print("Your secret phrase is:")
                print(database[s]["secret"])
            continue
        case 2:
            s=login()
            if s == 1:
                print("\nSuccessfuly Registered!")
            elif s==-1:
                print("error: username already exists")
            continue
        case 3:
            print("Thank You")
            break
        case _:
            print("error: invalid input")
