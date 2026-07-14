class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        operations = 0
        for i in range(k):
            if blocks[i]=='W':
                operations+=1
        minoperations = operations
        l = 0
        r = k
        while(r<len(blocks)):
            if blocks[r]=='W':
                operations+=1
            if blocks[l]=='W':
                operations-=1
            r+=1
            l+=1
            minoperations = min(minoperations,operations)
        return minoperations