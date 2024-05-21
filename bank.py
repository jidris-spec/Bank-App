import os
class Bank:
    def __init__(self):
        self.account_details = {}

    def log_in(self):
        user = input("Enter your user name: ")
        password = input("Enter your password: ")

        with open("account_details.txt", "w") as file:
            file.write("12345\n6789")

        directory = r"C:\Users\User\OneDrive\Desktop\New folder (2)"
        
        if not os.path.exists(directory):
            print("Directory does not exist.")
            return

        if password == "12345":  
            print(f"Welcome {user}")
        else:
            print("Invalid credentials.")

    def deposit(self):
        Account_Name = input("Enter your Account Name: ")
        Amount = int(input("Enter the Amount you want to deposit: "))

        account_key = (Account_Name)
        if account_key in self.account_details: 
            self.account_details[account_key] += Amount
        else: 
            self.account_details[account_key] = Amount
            print(f"You have deposited {Amount} into this account name {Account_Name} ")
        with open("deposit_reciept.txt", "w") as file:
            file.write("your money has been successfully deposited to your account")
    
    def transfer(self):
        credited_amount =int(input("How much do you want to transfer "))
        print(f"{credited_amount} has been transferred from your account: ")
        with open("Transfer_reciept.txt", "w") as file:
            file.write("Transfer successfull")
    def start(self):
        while True:
            print("\n1. log_in\n2. deposit\n3.  Transfer\n4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.log_in()
            elif choice == "2":
                self.deposit()
            # elif choice == "3":
            #     self.account_balance()
            elif choice == "3":
                self.transfer()
            elif choice == "4":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


bank = Bank()
bank.start()






