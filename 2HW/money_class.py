class exchanger(object):
    def __init__(self, quantity, currency="Rub"):
        self.quantity = quantity
        self.currency = currency

    def in_Rub(self):
        if self.currency == "Rub":
            return self.quantity
        if self.currency == "Usd":
            return self.quantity * 67
        if self.currency == "Eur":
            return self.quantity * 76
        if self.currency == "Cny":
            return self.quantity * 10
        if self.currency == "Btc":
            return self.quantity * 376000

    def back_in(self):
        if self.currency == "Rub":
            return exchanger(self.quantity)
        if self.currency == "Usd":
            return exchanger(self.quantity / 67)
        if self.currency == "Eur":
            return exchanger(self.quantity / 76)
        if self.currency == "Cny":
            return exchanger(self.quantity / 10)
        if self.currency == "Btc":
            return exchanger(self.quantity / 376000)

    def __str__(self):
        return "currency-{} value-{}".format(self.currency, self.quantity)

    def __repr__(self):
        return '{name:' + str(self.quantity) + ', age:' + str(self.currency) + '}'

    def __add__(self, other):
        if isinstance(other, exchanger):
            self.quantity = self.in_Rub() + other.in_Rub()
            return self.back_in()
        return exchanger(self.quantity + other)

    def __sub__(self, other):
        if isinstance(other, exchanger):
            self.quantity = self.in_Rub() - other.in_Rub()
            if self.quantity < 0:
                raise ValueError
            return self.back_in()
        if self.quantity < other:
            raise ValueError
        return exchanger(self.quantity - other)


a = exchanger(10)
b = exchanger(67)
c = a + b
print(c)
