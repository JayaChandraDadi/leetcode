class Solution(object):
    def pivotArray(self, nums, pivot):
       i = 0
       n = len(nums)
       j = n-1
       res = [0]*n
       left = 0
       right = n-1
       while(i<n and j>=0):
        if nums[i]<pivot:
            res[left] = nums[i]
            left+=1
        if nums[j]>pivot:
            res[right] = nums[j]
            right-=1
        i+=1
        j-=1
       while(left<=right):
        res[left] = pivot
        left+=1
       return res
