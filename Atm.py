class Atm:
    def _init_(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def checkBalance(self):
        print("your balance is Rs50000")

    def withdraw(self,amount):
        newAmount=50000-amount
        print("left over amount is"+str(newAmount))

def main():
    cardnumber=input("enter your cardnumber")  
    pin=input("enter your pin")

    newUser=Atm (cardnumber,pin)
    print("choose your activity")
    print("1.check your blance 2.withdraw") 

    activity=int(input("enter your activity number"))   
    if(activity==1):
        newUser.checkBalance()
    elif(activity==2):
        amount=int(input("enter your amount"))
        newUser.withdraw(amount) 
    else:
        print("enter a valid number")

    if _name_ == "_main_":
        main()