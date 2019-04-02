
class Checkout:

    class Discount:

        def __init__(self, noItems, price):

            self.noItems = noItems
            self.price = price


    def __init__(self):

        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0

    def addItemPrice(self, item, price):

        self.prices[item] = price

    def addItem(self, item):

        if item not in self.prices:
            raise Exception("Bad Item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):

        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.noItems:
                total += self.calculateItemDiscountedTotal(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def calculateItemDiscountedTotal(self, item, cnt, discount):

        total = 0

        noDiscounts = cnt / discount.noItems
        total += noDiscounts * discount.price
        remaining = cnt % discount.noItems
        total += remaining * self.prices[item]

        return total

    def addDiscount(self, item, noItems, price):

        discount = self.Discount(noItems, price)
        self.discounts[item] = discount