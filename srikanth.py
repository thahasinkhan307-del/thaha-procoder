#T0 create the BankAccount class
class bank:
    def __init__(self):
        self.bal=0 #Initialize balance to 0
        print("Welcome to the SBI")

    def deposit(self):
        amount=float(input("Enter the amount to be deposited:"))
        self.bal+=amount

    def withdraw(self):
        amount=float(input("Enter the amount to be withdraw:"))
        if self.bal>=amount:
         self.bal-=amount
         print("\nYour withdraw:",amount)
        else:
         print("\nInsufficient balance:")


     
#drive code
s = bank()
s.deposit()
s.withdraw()
