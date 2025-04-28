class StockSpanner(object):
    def __init__(self):
        self.ind = -1
        self.st = []
    def next(self, price):
        self.ind+=1
        while self.st and self.st[-1][0]<=price:
            self.st.pop()
        if self.st:
            ans =  self.ind - self.st[-1][1]
        else:
            ans = self.ind-(-1)
        self.st.append([price,self.ind])
        return ans
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)