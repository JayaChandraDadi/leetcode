class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        n = len(nums)
        sum1 = 0
        ans = 0
        for i in range(n):
            sum1+=nums[i]
            rem = sum1 - k
            if rem in hashmap:
                ans+=hashmap[rem]
            if sum1 not in hashmap:
                hashmap[sum1] = 0
            hashmap[sum1]+=1
            if sum1==k:
                ans+=1
        return ans
            