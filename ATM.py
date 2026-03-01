print("=================================")
print("          SIMPLE ATM             ")
print("=================================")

correct_pin = 1234
current_balance = 0

while True:
    input_pin = int(input("Enter your PIN: "))
    print("=================================")

    if input_pin == correct_pin:
        print("Successful... WELCOME TO THE ATM")
        logged_in = True
        print("=================================")


        while logged_in:
            print("\n[1] Check Balance")
            print("[2] Deposit")
            print("[3] Withdraw")
            print("[4] Exit")
            select_options = int(input("Select Options: "))
            print("=================================")

            if select_options == 1:
                print("Your balance is:", current_balance)
                print("=================================")


            elif select_options == 2:
                input_deposit = int(input("Enter amount you want to deposit: "))
                current_balance += input_deposit
                print("Deposit successful!")
                print("Your updated balance is:", current_balance)
                print("=================================")


            elif select_options == 3:
                input_withdraw = int(input("Enter amount you want to withdraw: "))
                if input_withdraw > current_balance:
                    print("Insufficient funds...")
                else:
                    current_balance -= input_withdraw
                    print("Successfully withdrawn:", input_withdraw)
                    print("Your updated balance is:", current_balance)
                print("=================================")


            elif select_options == 4:
                print("Thank you for using this ATM!")
                logged_in = False
                print("=================================")


            else:
                print("Invalid option! Please try again.")
                print("=================================")
    else:
        print("Wrong PIN! Try again...\n")









