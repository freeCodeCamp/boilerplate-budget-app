class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = list()
    
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'desciption': description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'desciption': description})
            return True
        return False
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']

        return balance
        
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        elif amount <= balance:
            return True






def create_spend_chart(categories):
    ...