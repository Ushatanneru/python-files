class bank:
    def __init__(self,account_no):
        self.account_no=account_no
    def check_bank_balance(self,balance):
        self.balance=balance
        print(self.balance)
    def display_deposite(self,deposite):
        self.deposite=deposite
        if(deposite>=1000):
            try:
                print("Amount will be deposited")
            except :
                print("invalid input")
            else:
                print("Ammount will not be deposited")






obj=bank(408909)
obj.check_bank_balance(200)
obj.display_deposite(100)




