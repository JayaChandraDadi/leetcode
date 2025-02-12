class Solution(object):
    def twoSum(self, a, target):
        presum = {}
        for i in range(len(a)):
            rem = target-a[i]
            if rem in presum:
                return [presum[rem],i]
            else:
                presum[a[i]] = i
    