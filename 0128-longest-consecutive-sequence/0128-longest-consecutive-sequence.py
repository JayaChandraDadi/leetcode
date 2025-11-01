class Solution(object):
    def longestConsecutive(self, nums):
        hashmap = set(nums)
        maxct = 0
        for el in hashmap:
            ct = 1
            if el-1 in hashmap:
                continue
            else:
                while el+1 in hashmap:
                    ct+=1
                    el+=1
            maxct = max(maxct,ct)
        return maxct
        