class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums)-1
        ans = 100
        while(low<=high):
            mid = (low+high)//2
            if nums[low]<=nums[mid]:
                ans = min(nums[low],ans)
                low = mid+1
            else:
                ans = min(nums[mid],ans)
                high = mid-1
        return ans
        