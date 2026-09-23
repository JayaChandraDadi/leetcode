class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target==0:
            return len(nums)
        hashmap = {}
        l = 0
        r = 0
        sum1 = 0
        maxlen = 0
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1==target:
                maxlen = i+1
            rem = sum1 - target
            if rem in hashmap:
                maxlen = max(maxlen,i - hashmap[rem])
            hashmap[sum1] = i
        if maxlen==0 and target!=0:
            return -1
        return len(nums) - maxlen