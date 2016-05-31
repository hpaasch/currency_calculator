
class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

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

    def __add__(self, other):
        return self.wallet_value() + other.wallet_value()

    def __sub__(self, other):
        return self.wallet_value() - other.wallet_value()

    def __eq__(self, other):
        return self.wallet_value() == other.wallet_value()

    def __ne__(self, other):
        return self.wallet_value() != other.wallet_value()

    def __mul__(self, other):
        return self.wallet_value() * other.wallet_value()

    def wallet_value(self):
        if self.currency == "USD":
            return self.amount * 1
        elif self.currency == "JPY":
            return self.amount * 110.762
        elif self.currency == "EUR":
            return self.amount * 1.11363
        elif self.currency == "BTC":
            return self.amount * 534.015


rayn_money = Money(1, "JPY")
hep_money = Money(50, "USD")
davis_money = Money(25, "BTC")
eileen_money = Money(30, "EUR")

print("HEP put in {} {}. It's worth ${} American.".format(hep_money.amount, hep_money.currency,
                                                    hep_money.wallet_value()))
print("Rayn put in {} {}. It's worth ${} American.".format(rayn_money.amount, rayn_money.currency,
                                                    rayn_money.wallet_value()))
print("Davis put in {} {}. It's worth ${} American.".format(davis_money.amount, davis_money.currency,
                                                          davis_money.wallet_value()))
print("Eileen put in {} {}. It's worth ${} American.".format(eileen_money.amount, eileen_money.currency,
                                                            eileen_money.wallet_value()))
print("HEP less than Rayn?", hep_money < rayn_money)
print("HEP greater than Davis?", hep_money > davis_money)
print("HEP greater than or equal to Eileen?", hep_money >= eileen_money)
print("HEP less than or equal to Eileen?", hep_money <= eileen_money)
print("HEP added to Rayn: ${} American.".format(hep_money + rayn_money))
print("HEP subtracted from Davis: ${} American.".format(davis_money - hep_money))
print("Davis equal to Rayn?", (davis_money == rayn_money))
print("Eileen not equal to Davis?", eileen_money != davis_money)
print("Rayn multiplied by Eileen: ${} American.".format(rayn_money * eileen_money))
