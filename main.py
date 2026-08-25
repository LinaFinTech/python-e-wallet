from wallet import create_account, login
accounts = []

def main_menu():
    while True:
        print("=============================")
        print("       Python E-Wallet       ")
        print("=============================")

        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Please select an option (1-3): ")
        if choice == "1":
            new_account = create_account()
            accounts.append(new_account)
        elif choice == "2":
            login(accounts)
        elif choice == "3":
            print("Thank you for using Python E-Wallet")
            break
        else:
            print("Please select an option (1-3): ")



main_menu()


