import unittest
from Money import Money
from Portfolio import Portfolio


class TestMoney(unittest.TestCase):

    def testMultiplication(self):
        # 10 EUR * 2 = 20 EUR
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self):
        # 4002 KRW / 4 = 1000.5 KRW
        originalMoney = Money(4002, "KRW")
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision, originalMoney.divide(4))

    def testAddition(self):
        # 5 USD + 10 USD = 15 USD
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))


if __name__ == '__main__':
    unittest.main()
