class StockSpanner:

    def __init__(self):
        self.st = []
        self.count = 0
    def next(self, price: int) -> int:
        self.count+=1
        while self.st and self.st[-1][0]<=price:
            self.st.pop()
        min_time = 0
        if self.st:
            min_time = self.st[-1][1]
        self.st.append([price,self.count])
        return self.count - min_time
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)