
class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return "{} {}".format(self.amount, self.currency)

    def __gt__(self, other):
        return self.wallet_value > other.wallet_value

    def __lt__(self, other):
        return self.wallet_value < other.wallet_value

    def __ge__(self, other):
        return self.wallet_value >= other.wallet_value

    def __le__(self, other):
        return self.wallet_value <= other.wallet_value

    def __add__(self, other):
        return self.wallet_value + other.wallet_value

    def __sub__(self, other):
        return self.wallet_value - other.wallet_value

    def __eq__(self, other):
        return self.wallet_value == other.wallet_value

    def __ne__(self, other):
        return self.wallet_value != other.wallet_value

    def __mul__(self, other):
        return self.wallet_value * other.wallet_value

    @property
    def wallet_value(self):
        if self.currency == "USD":
            return self.amount * 1
        elif self.currency == "JPY":
            return self.amount * 110.762
        elif self.currency == "EUR":
            return self.amount * 1.11363
        elif self.currency == "BTC":
            return self.amount * 534.015

    @wallet_value.getter
    def wallet_value(self):
        return self.amount


rayn_money = Money(1, "JPY")
hep_money = Money(50, "USD")
davis_money = Money(25, "BTC")
eileen_money = Money(30, "EUR")


# what i want to work:
fat_wallet = rayn_money + hep_money * davis_money - eileen_money
print(fat_wallet)

# this works but only with manual intervention
big_wallet = Money(1, "JPY").wallet_value + Money(50, "USD").wallet_value - Money(25, "BTC").wallet_value
print(big_wallet)



# big_wallet = rayn_money + hep_money + davis_money

# this doesn't work
# bad_wallet = property.wallet_value(rayn_money, hep_money, davis_money, eileen_money)
# print(bad_wallet)

# Money(100.00, "USD") + Money(56.32, "EUR") + Money(1.2, "BTC") + Money(8, "USD")

# this puts values in a list, but doesn't do math
loop_wallet = [rayn_money, hep_money, davis_money, eileen_money]
big_wallet_values = []
for item in loop_wallet:
    big_wallet_values.append(item.wallet_value)
print(big_wallet_values)
