class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int: 
        if nums=='':
            return 0
        l = 0
        r = 0 
        hashmap = {}
        maxlen = float('-inf')
        while(r<len(nums)):
            if nums[r] in hashmap:
                if l<=hashmap[nums[r]]:
                    l = hashmap[nums[r]] + 1
            hashmap[nums[r]] = r
            maxlen = max(maxlen,r-l+1)
            r+=1
        return maxlen
