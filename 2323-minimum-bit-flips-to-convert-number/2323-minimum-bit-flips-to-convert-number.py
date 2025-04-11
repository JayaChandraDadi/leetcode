class Solution(object):
    def minBitFlips(self, start, goal):
        ans = start^goal
        ct = 0
        while(ans!=0):
            ans = (ans)&(ans-1)
            ct+=1
        return ct
        
        