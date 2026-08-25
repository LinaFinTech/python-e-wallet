def create_account():
    while True:
        name = input("Please enter your name: ")

        if name.strip() != "":
            break
        else:
            print("Please enter a valid name")

    while True:
        email = input("Please enter your email: ").strip()

        if email.strip() != "" and "@" in email and "." in email and len(email) > 7:
            break
        else:
            print("Please enter a valid email")

    while True:
        password = input("Please enter your password: ")

        if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
            break
        else:
            print("Password must contain at least 8 characters, one uppercase letter, one lowercase letter, and one digit.")


    account = {
        "name": name,
        "email": email,
        "password": password,
        "balance": 0.00
    }

    print("Account created successfully")
    return account

def login(accounts):
    email = input("Please enter your email: ").strip()
    password = input("Please enter your password: ")
    for account in accounts:
        if account["email"] == email and account["password"] == password:
            print("Login successful")
            print("Welcome " + account["name"])
            return account

    print("Invalid email and/or password.")
    return None
