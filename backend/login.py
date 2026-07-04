def login():
    print("===== Login =====")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("Login Successful")
        return True
    else:
        print("Invalid Username or Password")
        return False