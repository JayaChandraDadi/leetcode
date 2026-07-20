class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        n = len(nums)
        high = n-1
        while(low<=high):
            mid = (low + high)//2
            if nums[mid] < nums[high]:
                high = mid 
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high-=1
        return nums[low]