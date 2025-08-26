class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        hashmap = set(nums)
        for it in hashmap:
            ct = 0
            for i in range(n):
                if it==nums[i]:
                    ct+=1
            if ct>n//2:
                return it
        return -1