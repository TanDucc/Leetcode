from sortedcontainers import SortedDict

class StockPrice:
    def __init__(self):
        self.prices = SortedDict()
        self.count = SortedDict()
        self.max_timestamp = 0
        
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.prices:
            old_price = self.prices[timestamp]
            self.count[old_price] -= 1
            if self.count[old_price] == 0:
                del self.count[old_price]
        self.prices[timestamp] = price
        self.count[price] = self.count.get(price, 0) + 1
        self.max_timestamp = max(self.max_timestamp, timestamp)
        
    def current(self) -> int:
        return self.prices[self.max_timestamp]
    def maximum(self) -> int:
        return self.count.peekitem(-1)[0]
    def minimum(self) -> int:
        return self.count.peekitem(0)[0]
        
        