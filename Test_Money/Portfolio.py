from Money import Money
import functools
import operator


class Portfolio:
    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke:
                failures.append(ke)
        if len(failures) == 0:
            return Money(total, currency)
        failureMessage = ",".join(f.args[0]for f in failures)
        raise Exception("Missing exchange rate(s):["+failureMessage+"]")
        total = functools.reduce(operator.add, map(
            lambda m: self.__convert(m, currency), self.moneys), 0)
        return Money(total, currency)

    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def __convert(self, aMoney, aCurrency):
        exchangeRates = {'EUR->USD': 1.2, 'USD->KRW': 1100}
        if aMoney.currency == aCurrency:
            return aMoney.amount
        else:
            key = aMoney.currency+'->'+aCurrency
            return aMoney.amount*exchangeRates[key]
