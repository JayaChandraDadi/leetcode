import random
class Solution:

    def __init__(self, w: list[int]):
        self.sum1 = 0
        self.prefix = []
        for i in range(len(w)):
            self.sum1+=w[i]
            self.prefix.append(self.sum1)
    def pickIndex(self) -> int:
        num = random.randint(1,self.sum1)
        low = 0
        high = len(self.prefix) - 1
        while(low<=high):
            mid = (low + high)//2
            if self.prefix[mid]>=num:
                high = mid - 1
            else:
                low = mid + 1
        return low
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()