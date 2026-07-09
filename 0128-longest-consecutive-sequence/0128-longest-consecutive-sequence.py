class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        maxct = 0
        for num in hashmap:
            if num-1 in hashmap:
                continue
            else:
                ct = 1
                x = num
                while x+1 in hashmap:
                    ct+=1
                    x+=1
                maxct = max(maxct,ct)
        return maxct