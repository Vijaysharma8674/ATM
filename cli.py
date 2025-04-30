
from   atm_module import ATM

class ATMApp:
   def __init__(self):
       self.atm=ATM()


   def start(self):
       print("\nWelcome to The ATM System..")

       while True:
           print("="*50)
           print("\n1. Create new account")
           print("="*50)
           print("\n2. Login to existing account")
           print("="*50)
           print("\n3. Exit")
           print("="*50)
           choice=input("Choose Any Option:")
           print("="*50)

           if choice =='1':
               self.create_account()
           elif choice =='2':
               self.login()
           elif choice =='3':
               self.exit()
           else:
               print("Invalid Option ..Pls Try again...")

   def create_account(self):
       try:

           account_number=input("Enter a 3-digit account number:")
           print("-"*50)
           if not (account_number.isdigit() and len(account_number)==3):
               raise ValueError("Account number must be exactly 3 digits")
           if self.atm.account_exists(account_number,):
                print("Account already exists ! ")
                return

           pin=input("Create a 4-digit PIN:")
           print("="*50)
           if not(pin.isdigit() and len(pin)==4):
               raise ValueError("PIN Must Be Exactly 4 digits:")
           if self.atm.create_account(account_number,pin):
               print("Account Created Successfully...")
           else:
               print("Failed to Create Account...")

       except ValueError as ve:
           print(f"Error:{ve}")


   def login(self):
       try:
           print("="*50)
           account_number = input("Enter a 3-digit account number.")
           if not (account_number.isdigit() and len(account_number) == 3):
               raise ValueError("Account number must be 3 digits:")
           if not self.atm.account_exists(account_number ):
               print("Account already exists ! ")
               return

           print("-"*50)
           pin = input("Enter a 4-digit PIN:")
           print("="*50)
           if not (pin.isdigit() and len(pin) == 4):
               raise ValueError("PIN must be 4 digits:")
           if self.atm.verify_pin(account_number,pin):
               print("-"*50)
               print("Login Successful...")
               print("*"*50)
               self.main_menu(account_number)
           else:
               print("Failed to Create Account...")

       except ValueError as ve:
           print(f"Error:{ve}")


   def main_menu(self, account_number):
       while True:
           print("-"*50)
           print("\n----ATM Main Menu----")
           print("-"*50)
           print("="*50)
           print("\t1. Check Balance")
           print("="*50)
           print("\t2. Withdraw Balance")
           print("="*50)
           print("\t3. Deposit Balance")
           print("="*50)
           print("\t4. Exit")
           print("="*50)
           choice=input("Choose an Option:")
           print("="*50)


           if choice == '1':
               balance = self.atm.get_balance(account_number)
               print(f"Your balance is: {balance}")


           elif choice == '2':

             try:

                amount = float(input("Enter amount to withdraw:"))
                if self.atm.withdraw(account_number, amount):
                    print('withdraw successfully')
                else:
                    print(" Insufficient balance..")

             except ValueError:
                       print("Invalid input.please enter a number..")

           elif choice =='3':
               try:
                   amount = float(input("Enter amount to deposit:"))
                   if self.atm.deposit(account_number, amount):
                       print('deposited successfully')
                   else:
                       print("withdraw Failed..")

               except ValueError:
                   print("Invalid input.please enter a number..")

           elif choice == '4':
               print("Thanks for visit my project..")
               break
           else:
               print("Invalid Choice--pls Try again..")

   def exit(self):
       print("\nThank you for using our ATM..")
       self.atm.close()
       exit()

if __name__ == "__main__":
  app=ATMApp()
  app.start()


