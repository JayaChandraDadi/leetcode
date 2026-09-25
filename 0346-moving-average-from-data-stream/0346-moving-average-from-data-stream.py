from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum1 = 0
        self.q = deque()
    def next(self, val: int) -> float:
        self.sum1+=val
        self.q.append(val)
        while(len(self.q)>self.size):
            num = self.q.popleft()
            self.sum1-=num
        
        return self.sum1/len(self.q)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)