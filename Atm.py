class Atm:
    def __init__(self, card_number, pin_number, balance):
        self.card_number = card_number
        self.pin_number = pin_number
        self.balance = balance

    def BalanceEnquiry():
        print(f"You have {str(balance)} in your bank account")
    
    def Withdraw(self):
        m = int(input("How much money do you want to withdraw?"))
        if m > self.balance:
            print("You do not have that much money in your account")
        else:
            print(f"You withdrew ${str(m)} from your account")

    def Details(self):
        print(f"Your credit card number is: {str(self.card_number)}\nYour pin number is: {str(self.pin_number)}\nBalance: ${str(self.balance)}")

cardNum = input("Enter your credit card number: ")
pinNum = input("Enter your pin number: ")
bal = int(input("Enter your balance: "))

atm = Atm(cardNum, pinNum, bal)

opt = input("What would you like to do? Your options are details, withdraw, balance: ")

if opt == "details":
    atm.Details()
elif opt == "withdraw":
    atm.Withdraw()
elif opt == "balance":
    atm.balance()
else:
    print("Thats not a valid option") 