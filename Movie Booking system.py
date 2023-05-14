#create a Python projectwhich enable to make
"""Functionalities: movie selection, add movie
buy tickets(
    row and seat number, language, location, discount)
    show movie timing
    snack purchase
    row and seat no selection
    user registration
    login user
    show ticket history
)

1. register
2. login show/movie
3. add show/movie


#menu"""
enter  = True
while enter:
    print("Main Menu")
    print("1) Login")
    print("2) Regiter")
    print("3) Quit")
    val= input("Enter your choice 1-3")
    if val == "3":
        break
    elif val == '1':
        email = input("Enter your e-mail address")
        passwd = input("Enter your password")
        loginstatus = True
        if loginstatus ==False:
            print("invalid credentials!!")
        else:
            print("Logged out")
        while loginstatus:
            print("User Menu!")
            print("1) show all movie!!")
            


