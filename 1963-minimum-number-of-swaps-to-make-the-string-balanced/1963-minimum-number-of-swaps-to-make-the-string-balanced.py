class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        open_count = 0
        close_count = 0
        swaps = 0
        for ch in s:
            if ch=='[':
                open_count+=1
            else:
                close_count+=1
            if close_count>open_count:
                close_count-=1
                open_count+=1
                swaps+=1
        return swaps