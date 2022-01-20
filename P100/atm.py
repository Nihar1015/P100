class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def checkBalance(self):
        print("your balance is 50,000")

    def withdrawal(self, amount):
        newAmount = 50000 - amount
        print("you have withdrew" + str(amount) + ". Your remaining balance is" + str(newAmount))


def main():
    card_number = input("Insert your card number :-")
    pin_number = input("Insert your pin number :-")


    new_user = Atm(card_number, pin_number)

    print("Choose your activity")
    print("1.Balance Enquiry  2. Withdrawal")
    activity = int(input("enter the amount :-"))

    if(activity == 1):
        new_user.checkBalance()
    elif(activity == 2):
        amount = int(input("enter the amount :-"))
        new_user.withdrawal(amount)
    else:
        print("enter a valid number")

if __name__ == "__main__":
    main()


        
