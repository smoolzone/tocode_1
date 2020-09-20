class Summer:

    def __init__(self):
        self.total_value = 0

    def add(self, *values):
        self.total_value += sum(values)

    def print_total(self):
        print(self.total_value)
        

class ClientBill:
    def __init__(self, name):
        self.client_name = name
        self.drinks_list = []
        self.total_bill = 0

    def add_drink(self, drink_name, drink_price):
        self.drinks_list += drink_name
        self.total_bill += drink_price

    def current_bill(self):
        print(self.total_bill)

    def full_bill(self):
        print(self.drinks_list)
        print(self.total_bill)