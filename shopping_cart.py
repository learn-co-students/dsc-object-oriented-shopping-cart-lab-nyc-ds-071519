from dsc_stats import Dsc_Stats

class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
      

    def add_item(self, name, price, quantity=1):
        self.items.append((Item(name, price), quantity))
        self.total += price*quantity
        return self.total


    def mean_item_price(self):
        prices = [item[0].price for item in self.items for _ in range(item[1])]
        return Dsc_Stats.calc_mean(prices)


    def median_item_price(self):
        prices = [item[0].price for item in self.items for _ in range(item[1])]
        return Dsc_Stats.calc_med(prices)


    def apply_discount(self):
        if self.employee_discount is None:
            return "Sorry, there is no discount to apply to your cart :("
        return self.total * (1-(self.employee_discount/100))


    def void_last_item(self):
        if len(self.items) == 0:
            return "There are no items in your cart!"
        last_item = self.items.pop()
        self.total -= last_item[0].price*last_item[1]
