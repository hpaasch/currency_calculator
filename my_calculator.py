
# Implement >= > <= < + - == != * operator overloads.

# example >>> Money(100.00, "USD") + Money(56.32, "EUR")
# output in USD

# currency_list = ["USD", "JPY", "EUR", "BTC"]


class Money:

    def __init__(self, amount, currency):
        # could seek input for the amount and currency
        self.amount = amount
        self.currency = currency
        # self.wallet = amount * currency  # this will be the amount * us currency equivalent

    def __str__(self):
        return "{} {}".format(self.amount, self.currency)

    def __gt__(self, other):
        return self.wallet_value() > other.wallet_value()

    def __lt__(self, other):
        return self.wallet_value() < other.wallet_value()

    def __ge__(self, other):
        return self.wallet_value() >= other.wallet_value()

    def __le__(self, other):
        return self.wallet_value() <= other.wallet_value()

    def wallet_value(self):
        if self.currency == "USD":
            self.amount *= 1
        elif self.currency == "JPY":
            self.amount *= 110.762
        elif self.currency == "EUR":
            self.amount *= 1.11363
        elif self.currency == "BTC":
            self.amount *= 534.015
        return self.amount




rayn_money = Money(200, "JPY")
hep_money = Money(100, "USD")
print(hep_money)
print(rayn_money)
print(hep_money < rayn_money)
print(hep_money > rayn_money)
print(hep_money >= rayn_money)
print(hep_money <= rayn_money)





