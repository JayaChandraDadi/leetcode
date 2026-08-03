from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        visited = [False]*n
        nums = list(s)
        q = deque()
        q.append(0)
        farthest = 0
        while(q):
            index = q.popleft()
            if index==n-1:
                return True
            min1 = max(index + minJump,farthest+1)
            max1 = min(index + maxJump,n-1)
            for j in range(min1,max1+1):
                if nums[j]=='0':
                    q.append(j)
            farthest = max(farthest,max1)
        return False
