class atm:
    def __init__(self, atmCard, pinNum):
        self.atmCard = atmCard
        self.pinNum = pinNum
    def CashWithdrawl(self):
        print("Please enter your credit card number to withdraw cash")
    def BalanceEnquire(self):
        print("Please enter your credit card number to view your balance")
card = atm("VisaCard", 3435)
print(card.pinNum)
print(card.atmCard)
card.CashWithdrawl()
card.BalanceEnquire()


