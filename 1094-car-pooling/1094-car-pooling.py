class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        n = len(trips)
        maxdist = float('-inf')
        for i in range(n):
            maxdist = max(maxdist,trips[i][2])
        ans = [0]*(maxdist+2)
        for ct,start,end in trips:
            ans[start]+=ct
            ans[end]-=ct
        sum1 = 0
        for i in range(maxdist+1):
            ans[i]+=sum1
            if ans[i]>capacity:
                return False
            sum1 = ans[i]
        return True
