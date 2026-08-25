from wallet import create_account

def main_menu():
    print("=============================")
    print("       Python E-Wallet       ")
    print("=============================")

    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Please select an option (1-3): "))
    if choice == 1:
        create_account()

main_menu()


