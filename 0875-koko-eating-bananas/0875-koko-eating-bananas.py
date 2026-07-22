import math
class Solution:
    def eating(self,piles,k):
        hours = 0
        for i in range(len(piles)):
            hours+= math.ceil(piles[i]/k)
        return hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while(low<=high):
            mid = (low + high)//2
            hours = self.eating(piles,mid)
            if hours<=h:
                high = mid - 1
            else:
                low = mid + 1
        return low