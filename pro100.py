class Atm(object):
    def __init__(self,number,pin):
        self.number=number
        self.pin = pin
    def cashWithdrawal(self):
        print("Beep..... Cash withdrawed.")
        print("Thank you!")
    def balanceEnquiry(self):
        print("Your problem will be solved.")
        print("Sorryyyy")
    def checkingBalance(self):
        print("Your balance is $100,000,000")
        print("Millionaire!!")
    def transferMoney(self):
        print("Transaction successful.")
        print("To whom?")
    def billPayment(self):
        print("Bill paid.")
        print("Was that an electricity bill?")

user1 = Atm(1234567812345678,0000)
print(user1.balanceEnquiry())
print(user1.cashWithdrawal())
print(user1.checkingBalance())
print(user1.transferMoney())
print(user1.billPayment())