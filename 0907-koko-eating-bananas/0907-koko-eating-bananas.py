import math
class Solution(object):
    def hours(self,piles,speed):
        hours = 0
        for pile in piles:
            hours+=((pile+speed-1)//speed)
        return hours
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        ans = 0
        while(low<=high):
            mid = (low+high)//2
            k = self.hours(piles,mid)
            if k>h:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        return ans