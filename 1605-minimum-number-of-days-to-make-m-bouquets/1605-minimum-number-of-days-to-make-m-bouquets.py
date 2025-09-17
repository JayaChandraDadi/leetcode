class Solution(object):
    def boquets(self,bloomDay,k,day):
        ct = 0
        bq = 0
        for i in range(len(bloomDay)):
            if day>=bloomDay[i]:
                ct+=1
                if ct==k:
                    bq+=1
                    ct = 0
            else:
                ct = 0
        return bq
    def minDays(self, bloomDay, m, k):
        low = min(bloomDay)
        high = max(bloomDay)
        if m*k>len(bloomDay):
            return -1
        while(low<=high):
            mid = (low+high)//2
            bq = self.boquets(bloomDay,k,mid)
            if bq<m:
                low = mid+1
            else:
                high = mid-1
        return low
