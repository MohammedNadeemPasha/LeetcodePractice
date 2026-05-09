# Design a StockSpanner class.
#
# For each new stock price, return its span:
# the number of consecutive previous days, including today,
# where the price was <= today's price.
#
# ex:
# prices = [100, 80, 60, 70, 60, 75, 85]
# O/P -> [1, 1, 1, 2, 1, 4, 6]
#
# Idea:
# - Use a monotonic decreasing stack.
# - Store pairs: (price, span).
# - For each new price:
#   - Start span as 1 for today.
#   - While stack top price <= current price:
#       - Pop it and add its span to current span.
#   - Push (current price, current span).
#   - Return current span.
# - This works because popped smaller/equal prices are included
#   in today's consecutive span.

class StockSpanner:

    def __init__(self):
        self.stock=[]

    def next(self, price: int) -> int:
        if not self.stock:
            self.stock.append((price,1))
            return 1
        else:
            count=1
            while len(self.stock) and self.stock[-1][0]<=price:
                count+=self.stock.pop()[1]
            self.stock.append((price,count))
            return count
        
stockSpanner= StockSpanner()
print(stockSpanner.next(100))
print(stockSpanner.next(80))
print(stockSpanner.next(60))
print(stockSpanner.next(70))
print(stockSpanner.next(60))
print(stockSpanner.next(75))
print(stockSpanner.next(85)) # O/P -> [1,1,1,2,1,4,6]