class BankAccount:
    def __init__(self,name,pin,balance):
        self.__is_logged_in=False
        self.name=name
        self.__pin=pin
        self.__balance=balance
    def pin_verify(self,entered_pin):
        if entered_pin==self.__pin:
            self.__is_logged_in=True
            return f"Access Granted"
        else:
            self.__is_logged_in=False
            return f"Access Denied"
    def deposit(self,dep):
        if not self.__is_logged_in:
            return f"please Login First"
        if dep<=0:
            return f"Invalid Amount"
        else:
            self.__balance+=dep
            return f"Deposited money:{dep}"
    def withdraw(self,draw):
        if not self.__is_logged_in:
            return f"please Login First"
        else:
            if draw<=0:
                return f"Please enter a valid amount."
            elif draw<=self.__balance:
                self.__balance-=draw
                return f"Withdrawn:{draw}"
            else:
                return f"Insufficient Balance."
    def check_balance(self):
        if not self.__is_logged_in:
            return f"please Login First"
        else:
            return f"Total Balance is:{self.__balance}"
    def logout(self):
        self.__is_logged_in=False
        return f"Logged out"
def invalid_input():
    return f"Please! Enter a valid number."
def login(user):
    print("""Choices are:
press '1' for Deposit
press '2' for Withdraw
press '3' for Check Balance
press '4' for Logout""")
    while True:
        try:
            choice=int(input("Enter your choice:"))
        except ValueError:
            print(invalid_input())
            continue
        if choice==1:
            try:
                amt=int(input("Enter the amount:"))
                if amt<=0:
                    print("Please!Enter a valid amount.")
                else:
                    print(user.deposit(amt))
            except ValueError:
                print(invalid_input())
                continue
        elif choice==2:
            try:
                amt=int(input("Enter the amount:"))
                if amt<=0:
                    print("Please!Enter a valid amount.")
                else:
                    print(user.withdraw(amt))
            except ValueError:
                print(invalid_input())
                continue
        elif choice==3:
            print(user.check_balance())
        elif choice==4:
            print(user.logout())
            break
        else:
            print("Please enter a Valid choice.")
def pin_attempts(user):
    attempt=3
    print(f"Attempts left:{attempt}")
    try:
        pin1=int(input('Enter pin:'))
        while attempt!=1:
            status=user.pin_verify(pin1)
            print(f"Attempts left:{attempt-1}")
            if status!="Access Granted":
                try:
                    pin1=int(input('Wrong pin!Try entering again:'))
                except ValueError:
                    print(invalid_input())
                    continue
            else:
                return f"Correct pin"
            attempt-=1
        else:
            return f"Wrong pin"
    except ValueError:
        print(invalid_input())
b1=BankAccount("chahat madhwani",12345,2000000)  
b2=BankAccount("hardhik madhwani",67890,3000000) 
account=[b1,b2]
choice1=None
while choice1!=3:
    print("Main menu")
    print('''1. Login
2.Create Account
3.Exit''')
    try:
        choice1=int(input("Enter your choice:"))
        if choice1==1:
            name=input('Enter your name:')
            current_user=None
            for acc in account:
                if acc.name.lower()==name.lower():
                    current_user=acc
                    break
            if current_user is None:
                print("user not found.")
                continue
            else:
                state=pin_attempts(current_user)
                if state!="Correct pin":
                    print("Try Logging in again.")
                    continue
                else:
                    login(current_user)
        elif choice1==2:
            name=input("Enter your name:")
            for i in account:
                if i.name.lower()==name.lower():
                    print("Name Already Exists.")
                    name=input("Enter your name again:")
                    continue
            else:
                try:
                    pin=int(input("Enter Your pin:"))
                    initial_amount=int(input('Enter your initial amount:'))
                    new_user=BankAccount(name,pin,initial_amount)
                    account.append(new_user)
                    new_user.pin_verify(pin)
                    login(new_user)
                    continue
                except ValueError:
                    print(invalid_input())
                    continue
        elif choice1==3:
            print("Exiting...")
            break
        else:
            print("Please Enter a valid choice")
    except ValueError:
        print(invalid_input())
                                     
