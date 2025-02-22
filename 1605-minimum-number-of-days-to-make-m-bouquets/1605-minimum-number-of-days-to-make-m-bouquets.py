class Solution(object):
    def bq(self,bloomDay,k,day):
        ct = 0
        bqct = 0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=day:
                ct+=1
            else:
                bqct+=(ct//k)
                ct = 0
        bqct+=(ct//k)
        return bqct
    def minDays(self, bloomDay, m, k):
        low = min(bloomDay)
        high = max(bloomDay)
        if m*k>len(bloomDay):
            return -1
        while(low<=high):
            mid = (low+high)//2
            x = self.bq(bloomDay,k,mid)
            if x>=m:
                high = mid-1
            else:
                low = mid+1
        return low