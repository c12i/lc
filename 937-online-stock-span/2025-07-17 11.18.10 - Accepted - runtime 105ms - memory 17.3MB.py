class StockSpanner(object):

    def __init__(self):
        self.prices = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1

        while self.prices and self.prices[-1][0] <= price:
            _,  prev_span = self.prices.pop()
            span += prev_span

        self.prices.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""
n numbers
amortised time: m .next --> 

["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

prices = [100, 85]
counts = [1,    6]

[[],[32],[82],[73],[99],[91], [100], [78], [54], 100]

count = 9
prices = [100]
counts = [9]

"""