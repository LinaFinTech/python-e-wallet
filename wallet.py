def create_account():
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    account = {
        "name": name,
        "email": email,
        "password": password,
        "balance": 0.00
    }

    print("Account created successfully")
    return account

