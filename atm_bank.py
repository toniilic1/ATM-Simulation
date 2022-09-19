import time

identity = input("Your name: ")

while True:
    try:
        current_bal = int(input("Your current balance: "))
    except ValueError:
        print('Error; your current balance must be a number.')
        continue
    break

class ATM:
    def set_card(self):
        print("You have successfully inserted your bank card in the ATM!")
        print("Loading... Please Wait")
        n = 0
        while 5 > n:
            print("...")
            time.sleep(0.5)
            n = n + 1

        print("Success!")
        time.sleep(0.5)

    def withdraw(self):
        amount = input("How much would you like to withdraw from your account?: ")
        while int(amount) > int(user.balance):
            print("ERROR! You may not exceed the limit of your balance, please try a different amount.")
            amount = input("How much would you like to withdraw from your account?: ")
        return amount


class Card:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


user = Card(identity, current_bal)

insert = input("Would you like to insert your card in the ATM?(Yes/No): ")

while insert not in ("Yes", "No", "YES", "NO"):

        print("You have to answer the question with Yes or No, please try again.")
        insert = input("Would you like to insert your card in the ATM?(Yes/No): ")

if insert == "Yes" or "YES":
    bank = ATM()
    bank.set_card()
    w_amount = bank.withdraw()
    print("You have taken exactly:",w_amount,"$ out of your account and your remaining balance is:",user.balance - int(w_amount),"$")


elif insert == "No" or "NO":
    print("You have chosen not to insert your card in the ATM and walk away...")