class Solution(object):
    def longestConsecutive(self, nums):
        maxcount = 0
        ct = 0
        hashmap = set(nums)
        n = len(nums)
        for it in hashmap:
            if it-1 in hashmap:
                continue
            else:
                start = it
                ct = 1
                while it+1 in hashmap:
                    ct+=1
                    it+=1
            maxcount = max(maxcount,ct)
        return maxcount