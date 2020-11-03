FOUR = 4
FIVE_SPACES = "     "
FIVE = 5
TEN = 10
PERCENT = 100


class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        funds_available = self.check_funds(amount)
        if funds_available:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        available_amount = 0
        for item in self.ledger:
            available_amount += item["amount"]
        return available_amount

    def transfer(self, amount, other_category):
        funds_available = self.check_funds(amount)
        if funds_available:
            self.withdraw(amount, f"Transfer to {other_category.category}")
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def get_total_withdrawals(self):
        total_withdrawals = 0
        for item in self.ledger:
            item_amount = item["amount"]
            if item_amount < 0:
                total_withdrawals += -item_amount
        return total_withdrawals

    def __str__(self):
        my_string = f"{self.category}".center(30, "*")
        category_total = 0
        for item in self.ledger:
            category_total += item["amount"]
            item_description = item["description"]
            item_amount = item["amount"]
            formatted_amount = "{:.2f}".format(item_amount).rjust(7)
            if len(item_description) > 23:
                my_string += f"\n{item_description[0:23]}{formatted_amount}"
            else:
                format_item_desc = item_description.ljust(23)
                my_string += f"\n{format_item_desc}{formatted_amount}"
        formatted_category_total = "{:.2f}".format(category_total)
        my_string += f"\nTotal: {formatted_category_total}"
        return my_string


def get_expenditure(categories):
    tot_expense = 0
    for category in categories:
        tot_expense += category.get_total_withdrawals()
    return tot_expense


def get_round_to_ten(value):
    temp = value
    if temp % TEN < FIVE:
        temp = temp - (temp % TEN)
    else:
        temp = temp + (TEN - (temp % TEN))
    return temp


def find_longest_category(categories):
    length = 0
    for category in categories:
        if len(category.category) > length:
            length = len(category.category)
    return length


def print_category_names(categories):
    formatted_categories = ""
    longest_category = find_longest_category(categories)
    j = 0
    while j < longest_category:
        current_line = ""
        for category in categories:
            good_category_name = category.category.capitalize()
            if j < len(category.category):
                if categories[0] == category:
                    current_line += f"     {good_category_name[j]}"
                elif categories[-1] == category:
                    if j != longest_category - 1:
                        current_line += f"  {good_category_name[j]}  \n"
                    else:
                        current_line += f"  {good_category_name[j]}  "
                else:
                    current_line += f"  {good_category_name[j]}"
            else:
                if categories[0] == category:
                    current_line += f"      "
                elif categories[-1] == category:
                    current_line += f"   \n"
                else:
                    current_line += f"   "
        formatted_categories += current_line
        j += 1

    return formatted_categories


def create_spend_chart(categories):
    total_expenditure_categories = get_expenditure(categories)
    percentage_string = "Percentage spent by category\n"
    percent = PERCENT
    bar_char = "o"
    line_length = 0
    while percent >= 0:
        percent_string = str(percent) + "| "
        if len(percent_string) < 5:
            percent_string = percent_string.rjust(5, " ")
        for category in categories:
            category_percent = \
                get_round_to_ten(int(PERCENT * (category.get_total_withdrawals() / total_expenditure_categories)))
            if percent > category_percent:
                percent_string += "   "
            else:
                percent_string += f"{bar_char}  "

        percentage_string += (percent_string + "\n")
        if percent == PERCENT:
            line_length = len(percent_string)
        percent -= 10
    underlined = "-" * (line_length - FOUR)
    underlined = underlined.rjust(line_length, " ")
    percentage_string += underlined
    category_names = print_category_names(categories)

    return percentage_string + "\n" + category_names


if __name__ == "__main__":
    food_category = Category("food")
    entertainment_category = Category("entertainment")
    business_category = Category("business")
    food_category.deposit(900, "deposit")
    entertainment_category.deposit(900, "deposit")
    business_category.deposit(900, "deposit")
    food_category.withdraw(105.55)
    entertainment_category.withdraw(33.40)
    business_category.withdraw(10.99)
    print(create_spend_chart([business_category, food_category, entertainment_category]))
