#Bank operation using OOP

class Bank:
    bankname="Bangladesh Bank"
    branch="Mohammadpur, Dhaka"

    #create account
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0 # set account balance to 0.0
        print(f'Hello {self.username} congrats! your account created successfully! ')



print(f'Welcome to {Bank.bankname} , {Bank.branch}')
#collect user data for account creation
username=input('Enter Your name :')
pan=input('Enter PAN card number : ')
address=input('Enter Your address : ')