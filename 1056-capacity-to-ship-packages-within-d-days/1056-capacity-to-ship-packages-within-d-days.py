class Solution(object):
    def capacity(self,weights,cap):
        d = 1
        sum1 = 0
        for i in range(len(weights)):
            sum1+=weights[i]
            if sum1>cap:
                d+=1
                sum1 = weights[i]
        return d

    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        while(low<=high):
            mid = (low+high)//2
            d = self.capacity(weights,mid)
            if d<=days:
                high = mid-1
            else:
                low = mid+1
        return low
        
        