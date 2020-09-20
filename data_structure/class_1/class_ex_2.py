class Invoice:
    vat = 0.17

    def print_item(self, name, price):
        print(f"{name}: {self.with_vat(price)}")

    def with_vat(self, price):
        return price * (1 + self.vat)


i = Invoice()
j = Invoice()

Invoice.vat = 0.10

i.print_item('iphone', 3000)
i.print_item('semsung', 120)


j.print_item('demo', 1000)