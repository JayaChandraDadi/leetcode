class Solution(object):
    def singleNonDuplicate(self, nums):
        low = 0
        n = len(nums)
        high = len(nums)-1
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        while(low<=high):
            mid = (low+high)//2
            if mid<n and mid>0:
                if nums[mid-1]!=nums[mid]!=nums[mid+1]:
                    return nums[mid]
                elif mid%2==0:
                    if nums[mid]==nums[mid-1]:
                        high = mid-1
                    else:
                        low = mid+1
                else:
                    if nums[mid]==nums[mid+1]:
                        high = mid-1
                    else:
                        low = mid+1