"""Banking System Using"""
import unittest

class User():
    """
    Holds details aboult an user and show user details
    """
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender =gender

    def show_details(self):
        """
        Show user details
        """
        print("User Profile Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
class Bank(User):
    """
    Stores details aboult the account balance and allows for deposit,withdraw,views,balance
    """
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        """
        User input your amount to deposit in your account
        """
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f'Account balance has been updated : € {self.balance}')


    def withdraw(self,amount):
        """this method using ammount and balance to withdraw money"""
        self.amount = amount
        if self.amount > self.balance:
            print(f'Insufficient Funds | Balance Avaliable : € {self.balance}')
        else:
            self.balance = self.balance - self.amount
            print(f'Account balance has been updated : € {self.balance}')

    def view_balance(self):
        """
        view details user and balance score
        """
        self.show_details()
        print(f'Account balance has been updated : € {self.balance}')


lucas = Bank("lucas",16,"Male")

class UserDetails(unittest.TestCase):
    """
    Test Case of Balance
    """
    def test_user(self):
        """Test balance and running deposit,withdraw and view_balance fucntions"""
        self.assertEqual(lucas.balance,0)
        lucas.deposit(100)
        lucas.withdraw(100)
        lucas.view_balance()

if __name__ =='__main__':
    unittest.main()
