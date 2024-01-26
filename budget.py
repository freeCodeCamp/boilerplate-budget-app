class Category:
  def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
    total_spending = sum(spendings)

    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for spending in spendings:
            chart += "o" if spending >= i * total_spending / 100 else " "
        chart += "\n"

    chart += "    ----------\n"
    max_name_length = max(len(category.category) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            chart += category.category[i] if i < len(category.category) else " "
            chart += "  "
        chart += "\n"

    return chart  
