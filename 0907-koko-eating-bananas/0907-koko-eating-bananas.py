class Solution(object):
    def func(self,k,piles):
        total = 0
        for pile in piles:
            total+=(pile+k-1)//k
        return total
    def minEatingSpeed(self, piles, h):
        low = 1
        high =max(piles)
        while(low<=high):
            mid = (low+high)//2
            req_time = self.func(mid,piles)
            if req_time<=h:
                high = mid-1
            else:
                low = mid+1
        return low
        